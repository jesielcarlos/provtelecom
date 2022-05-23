const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#btn-close");
const themeToggler = document.querySelector(".theme-toggle");
const dark = false;

menuBtn.addEventListener("click", () => {
    sideMenu.style.display = "block";
})
closeBtn.addEventListener("click", () => {
    sideMenu.style.display = "none";
})

themeToggler.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme-variables");

    themeToggler.querySelector("span:nth-child(1)").classList.toggle("active");
    themeToggler.querySelector("span:nth-child(2)").classList.toggle("active");

    dark = true;
})