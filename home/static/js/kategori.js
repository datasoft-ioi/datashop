const body = document.querySelector('.body')
const filter = document.querySelector('.vh')
const filterIcon = document.querySelector('.click')
const close = document.querySelector('.fa-xmark')
const filterMenu = document.querySelector('.categoryListMainFilter')








filterIcon.onclick = () => {
    filterMenu.classList.add('filterMenu')
    filter.classList.add('vhh')
    filter.classList.remove('none')

}
close.onclick = () => {
    filterMenu.classList.remove('filterMenu')
    filter.classList.add('none')
    filter.classList.remove('vhh')

}

filter.onclick = () => {
    filterMenu.classList.remove('filterMenu')
    filter.classList.add('none')
    filter.classList.remove('vhh')

}