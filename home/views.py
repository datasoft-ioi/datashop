from django.shortcuts import render, get_object_or_404


import json
import random
import requests

from order.models import Saqlangan, SaqlanganForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation

from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactMessage, FAQ, SettingLang, Language, Banner
from datashop import settings
from product.models import Category, Brands, Product, Images, Comment, Variants, CategoryLang, ProductFuture # ProductLang
from user.models import UserProfile

#bot
from ipware.ip import get_client_ip
from django.conf import settings
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
import telegram
import requests



URL = settings.BOT_URL
# my_token = "6143344105:AAHxL9pG02HE0XzJfeeHrfCMSKNpAVqO4bU
my_token = settings.BOT_TOKEN
# my_chat_id = "984573662"
my_chat_id = settings.BOT_CHAT_ID

message = "Nagap!"


class LazyEncode(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, dict):
            return str(obj)
        return super().default(obj)


def bot(request, msg, chat_id=my_chat_id, token=my_token):
    bot=telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)


def alibek(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST.get("name")
            email = str(request.POST.get("email"))
            subject = str(request.POST.get("subject"))
            message = str(request.POST.get("message"))

            msg = f"Ism: {name}\n Email: {email}\n Subject: {subject}\n Message: {message}"
            # print(form)
            # return HttpResponse('Siz Yutgazdingiz')
        bot(request, msg)
        
    form = ContactForm()

    cateory = Category.objects.filter(parent=None)
    context = {
        "cateory": cateory,
        "form": form,
    }

    return render(request, 'alibek.html', context)

def index(request):
    # if not request.session.has_key('currency'):
    #     request.session['currency'] = settings.DEFAULT_CURRENCY

    # if request.user.is_anonymous():
    #     pass

    # else:
    #     pass

    form = ContactForm()


    if request.user.is_anonymous:
        bot(request, str(get_client_ip(request)))
    else:
        bot(request, serialize('json', User.objects.filter(username=request.user), cls=LazyEncode))
    category = Category.objects.filter(parent=None)

    setting = Setting.objects.get(pk=1)
    products_latest = Product.objects.filter(category__title="Noutbuk").order_by('-id')[:10]  # last 5 products
    laptops_product = Product.objects.filter(category__title="Monitor").order_by('-id')[:10] # last 5
    products = Product.objects.all()
    #laptop 

    # >>>>>>>>>>>>>>>> M U L T I   L A N G U G A E >>>>>> START
    defaultlang = settings.LANGUAGE_CODE[0:2]
    # currentlang = "request.LANGUAGE_CODE[0:2]"

    # if defaultlang != currentlang:
    #     setting = SettingLang.objects.get(lang=currentlang)
    #     products_latest = Product.objects.raw(
    #         'SELECT p.id,p.price, l.title, l.description,l.slug  '
    #         'FROM product_product as p '
    #         'LEFT JOIN product_productlang as l '
    #         'ON p.id = l.product_id '
    #         'WHERE  l.lang=%s ORDER BY p.id DESC LIMIT 4', [currentlang])

    products_slider = Product.objects.all().order_by('id')[:4]  #first 4 products


    products_picked = Product.objects.all().order_by('?')[:4]   #Random selected 4 products
 

    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(parent=categoryID)

    else:
        product = Product.objects.all()
    category_lates = Category.objects.filter(parent=None).order_by('?')[:4] #Random selected




    page="home"
    context={'setting':setting,
            'page':page,
            'form':form,
            #  'product':product,
            'products': products,
            'products_slider': products_slider,
            'products_latest': products_latest,
            'products_picked': products_picked,
            'category':category,
            'category_lates':category_lates,
            "laptops_product": laptops_product,
            "brand_img": Brands.objects.all().order_by('?')[:8],

            "banner": Banner.objects.all().order_by('-id')[:8],

            # mobile cat noutbuk
            "noutbuk_mob_cat": Category.objects.filter(title="Noutbuklar")[:1],

            # kategoriya sidebars
            "cat_noutbuklar": Category.objects.filter(title="Noutbuklar"),
            "kompyuter_qurilmalari": Category.objects.filter(title="Kompyuter qurilmalari"),
            "nb_uchun_sumka_va_ryukzaklar": Category.objects.filter(title="Noutbuk uchun sumka va ryukzaklar"),
            "monoblok": Category.objects.filter(title="Monoblok"),
            "proektorlar": Category.objects.filter(title="Proektorlar"),
            "stol_usti_kompyuterlari": Category.objects.filter(title="Stol usti kompyuterlari"),
            "monitorlar": Category.objects.filter(title="Monitorlar"),
            "klaviatura_va_sichqoncha": Category.objects.filter(title="Klaviatura va Sichqoncha"),
            "ofis_jihozlari": Category.objects.filter(title="Ofis jihozlari"),
            "printerlar_va_kfmlar": Category.objects.filter(title="Printerlar va KFMlar uchun moslamalar"),
            "tizim_uskunalari": Category.objects.filter(title="Tizim uskunalari"),
            "monitorlar_uchun_kronshteyn ": Category.objects.filter(title="Monitorlar uchun kronshteyn va tagkursilar"),
            "videogaolish ": Category.objects.filter(title="Videogaolish"),
            "boshqa_aksessuarlar ": Category.objects.filter(title="Boshqa aksessuarlar"),

            #mobile category by category
            "monitor": Category.objects.filter(title="Monitor")[:1],
            "smartphone": Category.objects.filter(title="Smartfon")[:1],
            "noutbuk": Category.objects.filter(title="Noutbuk")[:1],
        
            #Desktop contents
            "cat_by_noutbuk": Product.objects.filter(category__title="Noutbuklar").order_by('-id')[:10],
            "cat_by_aksesuar": Product.objects.filter(category__parent=(36)).order_by('?')[:10],
            "cat_by_monitor": Product.objects.filter(category__title="Monitorlar").order_by('-id')[:10],


        }

    return render(request,'index.html',context)

def all_products(request):
    context = {
        "full_products": Product.objects.all().order_by('?'),
    }
    return render(request, 'all_prod.html', context)


def profil(request):

    context = {
        "profil": User.objects.all()
    }

    return render(request, 'profil.html')

def full_cat_products(request, id, slug):

    context = {
        "full_products": Product.objects.filter(category_id=id),
    }

    return render(request, 'full_cat_prod.html', context)

def selectlanguage(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl= request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY]=lang
        #return HttpResponse(lang)
        return HttpResponseRedirect("/"+lang)

def aboutus(request):
    #category = categoryTree(0,'',currentlang)
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)

    context={'setting':setting}
    return render(request, 'about.html', context)

def contactus(request):
    currentlang = request.LANGUAGE_CODE[0:2]
    #category = categoryTree(0,'',currentlang)
    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')

    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)

    form = ContactForm
    context={'setting':setting,'form':form  }
    return render(request, 'contactus.html', context)

def category_products(request,id,slug):
    defaultlang = settings.LANGUAGE_CODE[0:2]
    # currentlang = request.LANGUAGE_CODE[0:2]
    catdata = Category.objects.get(pk=id)
    category = Category.objects.filter(parent=None)

    random_prod = Product.objects.filter(category__parent=id).order_by('?')[:3]

    cat_fil = Category.objects.filter(pk=id)
    products = Product.objects.all() 

    if slug:
        categorys = get_object_or_404(Category, slug=slug)
        products = products.filter(category=categorys)
        
    # if defaultlang != currentlang:
    #     try:
    #         products = Product.objects.raw(
    #             'SELECT p.id,p.price,p.amount,p.image,p.variant,l.title, l.keywords, l.description,l.slug,l.detail '
    #             'FROM product_product as p '
    #             'LEFT JOIN product_productlang as l '
    #             'ON p.id = l.product_id '
    #             'WHERE p.category_id=%s and l.lang=%s', [id, currentlang])
    #     except:
    #         pass
    #     catdata = CategoryLang.objects.get(category_id=id, lang=currentlang)

    context={'products': products,
             'category':category,
             'random_prod':random_prod,

             # kategoriya sidebars
            "cat_noutbuklar": Category.objects.filter(title="Noutbuklar"),

            'catdata':catdata,
            'cat_fil':cat_fil,

             # kategoriya sidebars
            "cat_noutbuklar": Category.objects.filter(title="Noutbuklar"),
            "kompyuter_qurilmalari": Category.objects.filter(title="Kompyuter qurilmalari"),
            "nb_uchun_sumka_va_ryukzaklar": Category.objects.filter(title="Noutbuk uchun sumka va ryukzaklar"),
            "monoblok": Category.objects.filter(title="Monoblok"),
            "proektorlar": Category.objects.filter(title="Proektorlar"),
            "stol_usti_kompyuterlari": Category.objects.filter(title="Stol usti kompyuterlari"),
            "monitorlar": Category.objects.filter(title="Monitorlar"),
            "klaviatura_va_sichqoncha": Category.objects.filter(title="Klaviatura va Sichqoncha"),
            "ofis_jihozlari": Category.objects.filter(title="Ofis jihozlari"),
            "printerlar_va_kfmlar": Category.objects.filter(title="Printerlar va KFMlar uchun moslamalar"),
            "tizim_uskunalari": Category.objects.filter(title="Tizim uskunalari"),
            "monitorlar_uchun_kronshteyn ": Category.objects.filter(title="Monitorlar uchun kronshteyn va tagkursilar"),
            "videogaolish ": Category.objects.filter(title="Videogaolish"),
            "boshqa_aksessuarlar ": Category.objects.filter(title="Boshqa aksessuarlar"),
            }
    return render(request,'categoryList.html',context)

def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title +" > " + rs.category.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def product_detail(request,id,slug):
    query = request.GET.get('q')
    # >>>>>>>>>>>>>>>> M U L T I   L A N G U G A E >>>>>> START
    defaultlang = settings.LANGUAGE_CODE[0:2] #en-EN
    # currentlang = request.LANGUAGE_CODE[0:2]
    #category = categoryTree(0, '', currentlang)
    category = Category.objects.filter(parent=None)

    product = Product.objects.get(pk=id)

    # if defaultlang != currentlang:
    #     try:
    #         prolang =  Product.objects.raw('SELECT p.id,p.price,p.amount,p.image,p.variant,l.title, l.keywords, l.description,l.slug,l.detail '
    #                                       'FROM product_product as p '
    #                                       'INNER JOIN product_productlang as l '
    #                                       'ON p.id = l.product_id '
    #                                       'WHERE p.id=%s and l.lang=%s',[id,currentlang])
    #         product=prolang[0]
    #     except:
    #         pass
    # <<<<<<<<<< M U L T I   L A N G U G A E <<<<<<<<<<<<<<< end

    images = Images.objects.filter(product_id=id)
    futers = ProductFuture.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id,status='True')
    context = {'product': product,'category': category,
               'images': images, 'comments': comments,
               'futers': futers,
                # kategoriya sidebars
                "cat_noutbuklar": Category.objects.filter(title="Noutbuklar"),
                "kompyuter_qurilmalari": Category.objects.filter(title="Kompyuter qurilmalari"),
                "nb_uchun_sumka_va_ryukzaklar": Category.objects.filter(title="Noutbuk uchun sumka va ryukzaklar"),
                "monoblok": Category.objects.filter(title="Monoblok"),
                "proektorlar": Category.objects.filter(title="Proektorlar"),
                "stol_usti_kompyuterlari": Category.objects.filter(title="Stol usti kompyuterlari"),
                "monitorlar": Category.objects.filter(title="Monitorlar"),
                "klaviatura_va_sichqoncha": Category.objects.filter(title="Klaviatura va Sichqoncha"),
                "ofis_jihozlari": Category.objects.filter(title="Ofis jihozlari"),
                "printerlar_va_kfmlar": Category.objects.filter(title="Printerlar va KFMlar uchun moslamalar"),
                "tizim_uskunalari": Category.objects.filter(title="Tizim uskunalari"),
                "monitorlar_uchun_kronshteyn ": Category.objects.filter(title="Monitorlar uchun kronshteyn va tagkursilar"),
                "videogaolish ": Category.objects.filter(title="Videogaolish"),
                "boshqa_aksessuarlar ": Category.objects.filter(title="Boshqa aksessuarlar"),
               }
    if product.variant !="None": # Product have variants
        if request.method == 'POST': #if we select color
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id) #selected product by click color radio
            colors = Variants.objects.filter(product_id=id,size_id=variant.size_id )
            sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id',[id])
            query += variant.title+' Size:' +str(variant.size) +' Color:' +str(variant.color)
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id,size_id=variants[0].size_id )
            sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id',[id])
            variant =Variants.objects.get(id=variants[0].id)
        context.update({'sizes': sizes, 'colors': colors,
                        'variant': variant,'query': query,
                        })
    return render(request,'productdtl.html',context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)


def faq(request):
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]

    if defaultlang==currentlang:
        faq = FAQ.objects.filter(status="True",lang=defaultlang).order_by("ordernumber")
    else:
        faq = FAQ.objects.filter(status="True",lang=currentlang).order_by("ordernumber")

    context = {
        'faq': faq,
    }
    return render(request, 'faq.html', context)


def selectcurrency(request):
    lasturl = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  # check post
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(lasturl)

@login_required(login_url='/login') # Check login
def savelangcur(request):
    lasturl = request.META.get('HTTP_REFERER')
    curren_user = request.user
    language=Language.objects.get(code=request.LANGUAGE_CODE[0:2])
    #Save to User profile database
    data = UserProfile.objects.get(user_id=curren_user.id )
    data.language_id = language.id
    data.currency_id = request.session['currency']
    data.save()  # save data
    return HttpResponseRedirect(lasturl)

@login_required(login_url='/login')
def addtosaqlangan(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id)

    if product.variant != 'None':
        variantid = request.POST.get('variantid')  # from variant add to cart
        checkinvariant = Saqlangan.objects.filter(variant_id=variantid, user_id=current_user.id)  # Check product in shopcart
        if checkinvariant:
            control = 1 # The product is in the cart
        else:
            control = 1 # The product is not in the cart"""
    else:
        checkinproduct = Saqlangan.objects.filter(product_id=id, user_id=current_user.id) # Check product in shopcart
        if checkinproduct:
            control = 1 
        else:
            control = 1 # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = SaqlanganForm(request.POST)
        if form.is_valid():
            if control==1: # Update  shopcart
                if product.variant == 'None':
                    data = Saqlangan.objects.get(product_id=id, user_id=current_user.id)
                else:
                    data = Saqlangan.objects.get(product_id=id, user_id=current_user.id)
                data.save()  # save data
            else : # Inser to Shopcart
                data = Saqlangan()
                data.user_id = current_user.id
                data.product_id =id
                # data.variant_id = variantid
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Maxsulot Saqlandii ")
        return HttpResponseRedirect(url)

    # else: # if there is no post
    #     if control == 1:  # Update  shopcart
    #         data = Saqlangan.objects.get(product_id=id, user_id=current_user.id)
    #         data.quantity += 1
    #         data.save()  #
    #     else:  #  Inser to Shopcart
    #         data = Saqlangan()  # model ile bağlantı kur
    #         data.user_id = current_user.id
    #         data.product_id = id
    #         data.quantity = 1
    #         data.variant_id =None
    #         data.save()  #
    #     messages.success(request, "Maxsulot Saqlandi")
    #     return HttpResponseRedirect(url)


    

def saqlanganlar(request):
    category = Category.objects.filter(parent=None)
    current_user = request.user
    saqlangan = Saqlangan.objects.filter(user_id=current_user.id)
    
    
    context = {

        "category": category,
        "saqlangan": saqlangan,

        # kategoriya sidebars
        "cat_noutbuklar": Category.objects.filter(title="Noutbuklar"),
        "kompyuter_qurilmalari": Category.objects.filter(title="Kompyuter qurilmalari"),
        "nb_uchun_sumka_va_ryukzaklar": Category.objects.filter(title="Noutbuk uchun sumka va ryukzaklar"),
        "monoblok": Category.objects.filter(title="Monoblok"),
        "proektorlar": Category.objects.filter(title="Proektorlar"),
        "stol_usti_kompyuterlari": Category.objects.filter(title="Stol usti kompyuterlari"),
        "monitorlar": Category.objects.filter(title="Monitorlar"),
        "klaviatura_va_sichqoncha": Category.objects.filter(title="Klaviatura va Sichqoncha"),
        "ofis_jihozlari": Category.objects.filter(title="Ofis jihozlari"),
        "printerlar_va_kfmlar": Category.objects.filter(title="Printerlar va KFMlar uchun moslamalar"),
        "tizim_uskunalari": Category.objects.filter(title="Tizim uskunalari"),
        "monitorlar_uchun_kronshteyn ": Category.objects.filter(title="Monitorlar uchun kronshteyn va tagkursilar"),
        "videogaolish ": Category.objects.filter(title="Videogaolish"),
        "boshqa_aksessuarlar ": Category.objects.filter(title="Boshqa aksessuarlar"),

    }

    return render(request, 'saqlanganlar.html', context)

