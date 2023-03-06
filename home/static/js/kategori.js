const filter = document.querySelector('.vh')
const filterIcon = document.querySelector('.click')
const close = document.querySelector('.fa-xmark')
const filterMenu = document.querySelector('.categoryListMainFilter')
const body = document.querySelector('body')

const aksesuar = document.querySelector('.aksesuar').onmouseenter = fun1
const elektronika = document.querySelector('.elektronika').onmouseenter = fun2
const text2 = document.querySelector('.victus')
const text1 = document.querySelector('.notebook')


function fun1(){
    text2.style.display = 'block'
    text1.style.display = 'none'

}

function fun2(){
    text1.style.display = 'block'
    text2.style.display = 'none'
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