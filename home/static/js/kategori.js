const filter = document.querySelector('.vh')
const filterIcon = document.querySelector('.click')
const close = document.querySelector('.fa-xmark')
const filterMenu = document.querySelector('.categoryListMainFilter')
const body = document.querySelector('body')

const cursor1 = document.querySelector('.title1').onmouseenter = fun1
const cursor2 = document.querySelector('.title2').onmouseenter = fun2
const hover1 = document.querySelector('.hover1')
const hover2 = document.querySelector('.hover2')
const hover3 = document.querySelector('.hover3')
const hover4 = document.querySelector('.hover4')
const cursor3 = document.querySelector('.title3').onmouseenter = fun3
const cursor4 = document.querySelector('.title4').onmouseenter = fun4

const text1 = document.querySelector('.geymerlar')
const text2 = document.querySelector('.noutbuk')
const text3 = document.querySelector('.telefon')
const text4 = document.querySelector('.televizor')


function fun1() {
    text1.style.display = 'flex'
    hover1.classList.add('hoverTitle')
    hover2.classList.remove('hoverTitle')
    hover3.classList.remove('hoverTitle')
    hover4.classList.remove('hoverTitle')
    text2.style.display = 'none'
    text3.style.display = 'none'
    text4.style.display = 'none'
}

function fun2() {
    text2.style.display = 'flex'
    text1.style.display = 'none'
    text3.style.display = 'none'
    text4.style.display = 'none'
    hover1.classList.remove('hoverTitle')
    hover2.classList.add('hoverTitle')
    hover3.classList.remove('hoverTitle')
    hover4.classList.remove('hoverTitle')
}

function fun3() {
    text3.style.display = 'flex'
    text1.style.display = 'none'
    text2.style.display = 'none'
    text4.style.display = 'none'
    hover1.classList.remove('hoverTitle')
    hover2.classList.remove('hoverTitle')
    hover3.classList.add('hoverTitle')
    hover4.classList.remove('hoverTitle')
}

function fun4() {
    text4.style.display = 'flex'
    text1.style.display = 'none'
    text2.style.display = 'none'
    text3.style.display = 'none'
    hover1.classList.remove('hoverTitle')
    hover2.classList.remove('hoverTitle')
    hover3.classList.remove('hoverTitle')
    hover4.classList.add('hoverTitle')
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
