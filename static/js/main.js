const menu= document.querySelector("#menu")
const sidebar=document.querySelector(".sidebar")

menu.addEventListener("click",function(){
    sidebar.classList.toggle("show-sidebar")
})


const dropdown=document.querySelector("#drop-down")
const drop=document.querySelector(".dropdown-content-background")


dropdown.addEventListener("click",function(){
    drop.classList.toggle("show-dropdown")
})
