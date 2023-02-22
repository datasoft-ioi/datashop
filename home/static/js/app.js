const kategory = document.querySelector(".kategory")
const kategoryBtn = document.querySelector("#kategoryBtn")
const navbar = document.querySelector('nav')
const profil = document.querySelector('.profilBox')
const profilBtn = document.querySelector('.profilBtn')
const closeKategory = document.querySelector('.closeKategory')
const closeProfil = document.querySelector('.closeProfil')
const kategoryBtnRes = document.querySelector('.kategoryBtn')
const massageBar = document.querySelector('.massageBar')
const dtlPriceInfoPriceBtn1 = document.querySelector('.dtlPriceInfoPriceBtn1')
const plus = document.querySelector('.plus')
const minus = document.querySelector('.minus')
const countNumber = document.querySelector('.countNumber')
const kategoryLinksLeftTitle = document.querySelector('.kategoryLinksLeftTitle')
const kategoryLinksLeftRight = document.querySelector('.kategoryLinksLeftRight')



let korOnOff = false
let profilShow = false

kategoryBtn.onclick = () => {
    if (korOnOff == false) {
        korOnOff = true
        navbar.classList.add('noneBox')
        kategory.classList.add('kategoryOn')
        closeKategory.classList.add('closeKategoryOn')
    }else{
        korOnOff = false
        kategory.classList.remove('kategoryOn')
        navbar.classList.remove('noneBox')
        closeKategory.classList.remove('closeKategoryOn')
    }
}
kategoryBtnRes.onclick = () => {
    if (korOnOff == false) {
        korOnOff = true
        navbar.classList.add('noneBox')
        kategory.classList.add('kategoryOn')
        closeKategory.classList.add('closeKategoryOn')
    }else{
        korOnOff = false
        kategory.classList.remove('kategoryOn')
        navbar.classList.remove('noneBox')
        closeKategory.classList.remove('closeKategoryOn')
    }
}
profilBtn.onclick = () => {
    if (profilShow == false) {
        profilShow = true
        profil.classList.add('profilOn')
        closeKategory.classList.add('closeKategoryOn')
    }else {
        profilShow = false
        profil.classList.remove('profilOn')
    }
} 

closeKategory.onclick = () => {
    korOnOff = false
    kategory.classList.remove('kategoryOn')
    navbar.classList.remove('noneBox')
    closeKategory.classList.remove('closeKategoryOn')
    profilShow = false
    profil.classList.remove('profilOn')
}

// massage bar functoion
setTimeout(() => {
    massageBar.classList.add('massageBarNone')
}, 3000)

// count function
plus.onclick = () => {
    countNumber.textContent + 1
}

console.log(typeof(+countNumber.textContent + 1));

kategoryLinksLeftRight.classList.add('none')


kategoryLinksLeftTitle.onclick = () => {
    
}