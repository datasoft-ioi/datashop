const filter = document.querySelector('.vh')
const filterIcon = document.querySelector('.click')
const close = document.querySelector('.fa-xmark')
const filterMenu = document.querySelector('.categoryListMainFilter')
const body = document.querySelector('body')







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