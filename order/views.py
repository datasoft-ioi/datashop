from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.views import bot, LazyEncode
from django.core.serializers import serialize


# Create your views here.
from django.utils.crypto import get_random_string

from order.models import ShopCart, ShopCartForm, OrderForm, Order, OrderProduct
from product.models import Category, Product, Variants
from user.models import UserProfile


def index(request):
    return HttpResponse ("Order Page")

@login_required(login_url='/login') # Check login
def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id)

    if product.variant != 'None':
        variantid = request.POST.get('variantid')  # from variant add to cart
        checkinvariant = ShopCart.objects.filter(variant_id=variantid, user_id=current_user.id)  # Check product in shopcart
        if checkinvariant:
            control = 1 # The product is in the cart
        else:
            control = 0 # The product is not in the cart"""
    else:
        checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id) # Check product in shopcart
        if checkinproduct:
            control = 1 # The product is in the cart
        else:
            control = 0 # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1: # Update  shopcart
                if product.variant == 'None':
                    data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                else:
                    data = ShopCart.objects.get(product_id=id, variant_id=variantid, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else : # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id =id
                # data.variant_id = variantid
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Maxsulot Savatga qoshildi ")
        return HttpResponseRedirect(url)

    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()  #
        else:  #  Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.variant_id =None
            data.save()  #
        messages.success(request, "Maxsulot Savatga qoshildi")
        return HttpResponseRedirect(url)


def shopcart(request):
    category = Category.objects.filter(parent=None)
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    #return HttpResponse(str(total))
    context={'shopcart': shopcart,
             'category':category,
             'total': total,

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
    return render(request,'shopcart_products.html',context)



@login_required(login_url='/login') # Check login
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect("/shopcart")


def orderproduct(request):
    category = Category.objects.filter(parent=None)
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        #return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            # ..............

            data = Order()
            data.first_name = form.cleaned_data['first_name'] #get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode= get_random_string(5).upper() # random cod
            data.code =  ordercode
            data.save() #


            for rs in shopcart:
                global send_to_bot
                send_to_bot = rs.product.price
                detail = OrderProduct()
                detail.order_id     = data.id # Order Id
                detail.product_id   = rs.product_id
                detail.user_id      = current_user.id
                detail.quantity     = rs.quantity
                if rs.product.variant == 'None':
                    detail.price    = rs.product.price
                else:
                    detail.price = rs.variant.price
                detail.variant_id   = rs.variant_id
                detail.amount        = rs.amount
                detail.save()
                # ***Reduce quantity of sold product from Amount of Product
                if  rs.product.variant=='None':
                    product = Product.objects.get(id=rs.product_id)
                    product.amount -= rs.quantity
                    product.save()
                else:
                    variant = Variants.objects.get(id=rs.product_id)
                    variant.quantity -= rs.quantity
                    variant.save()
                #************ <> *****************
            # msg = ""
            # msg += form.cleaned_data['first_name'] #get product quantity from form
            # msg += form.cleaned_data['last_name']
            # msg += form.cleaned_data['address']
            # msg += form.cleaned_data['city']
            # msg += form.cleaned_data['phone']
            # msg += request.META.get('REMOTE_ADDR')

            prod_img = ""
            msg = f"❗️❗️❗️ <b>Mahsulotga buyurtma</b>\n\n"

            msg += f"Ismi: {send_to_bot}\n\n"
            msg += f"Familiyasi: {send_to_bot}\n\n"
            # msg += f"Maxsulot nomi: {send_to_bot.product.title}\n\n"
            # msg += f"Maxsulot narxi: ${send_to_bot.product.price}\n\n"

            

            bot(request, msg)
            ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
            request.session['cart_items']=0
            messages.success(request, "Your Order has been completed. Thank you ")
            return render(request, 'Order_Completed.html',{'ordercode':ordercode,'category': category,'total': total, 'shopcart': shopcart,})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               }

    return render(request, 'Order_Form.html', context)