const filter = document.querySelector('.vh')
const filterIcon = document.querySelector('.click')
const close = document.querySelector('.fa-xmark')
const filterMenu = document.querySelector('.categoryListMainFilter')
const body = document.querySelector('body')

const cursor1 = document.querySelector('.oyin').onmouseenter = fun1
const cursor2 = document.querySelector('.notebook').onmouseenter = fun2
const cursor3 = document.querySelector('.gajed').onmouseenter = fun3
const cursor4 = document.querySelector('.audio').onmouseenter = fun4

const text1 = document.querySelector('.geymerlar')
const text2 = document.querySelector('.noutbuk')
const text3 = document.querySelector('.telefon')
const text4 = document.querySelector('.televizor')


function fun1(){
    text1.style.display = 'block'
    text2.style.display = 'none'
    text3.style.display = 'none'
    text4.style.display = 'none'
}

function fun2(){
    text2.style.display = 'block'
    text1.style.display = 'none'
    text3.style.display = 'none'
    text4.style.display = 'none'
}

function fun3(){
    text3.style.display = 'block'
    text1.style.display = 'none'
    text2.style.display = 'none'
    text4.style.display = 'none'
}

function fun4(){
    text4.style.display = 'block'
    text1.style.display = 'none'
    text2.style.display = 'none'
    text3.style.display = 'none'
}





filterIcon.onclick = () => {
    filterMenu.classList.add('filterMenu')
    filter.classList.add('vhh')
    filter.classList.remove('none')
    body.classList.add('overflow')
}
close.onclick = () => {
    filterMenu.classList.remove('filterMenu')
    filter.classList.add('none')
    filter.classList.remove('vhh')
    body.classList.remove('overflow')
}

filter.onclick = () => {
    filterMenu.classList.remove('filterMenu')
    filter.classList.add('none')
    filter.classList.remove('vhh')
    body.classList.remove('overflow')
}