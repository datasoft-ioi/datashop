const katalok1 = document.querySelector('.kiyim').onmouseenter = katlogOpen
const katalok2 = document.querySelector('.kasesuar').onmouseenter = katlogOpen2
const katalok1Text = document.querySelector('.kiyimText')
const katalok2Text = document.querySelector('.aksesuarText')


function katlogOpen(){
    katalok1Text.style.display = 'block'
    katalok2Text.style.display = 'none'

}

function katlogOpen2(){
    katalok1Text.style.display = 'none'
    katalok2Text.style.display = 'block'

}

