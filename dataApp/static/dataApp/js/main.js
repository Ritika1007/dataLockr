function toggleEdit() {
    const fileContent = document.getElementById("file-content");
    const editForm = document.getElementById("edit-form");

    if (fileContent.style.display === "none") {
      fileContent.style.display = "block";
      editForm.style.display = "none";
    } else {
      fileContent.style.display = "none";
      editForm.style.display = "block";
    }
  }

// const nav = document.querySelector(".nav"),
// searchIcon = document.querySelector("#searchIcon"),
// navOpenBtn = document.querySelector(".navOpenBtn"),
// navCloseBtn = document.querySelector(".navCloseBtn");

// searchIcon.addEventListener("click", () => {
//   nav.classList.toggle("openSearch");
//   nav.classList.remove("openNav");
//   if (nav.classList.contains("openSearch")) {
//     return searchIcon.classList.replace("uil-search", "uil-times");
//   }
//   searchIcon.classList.replace("uil-times", "uil-search");
// });

// navOpenBtn.addEventListener("click", () => {
//   nav.classList.add("openNav");
//   nav.classList.remove("openSearch");
//   searchIcon.classList.replace("uil-times", "uil-search");
// });

// navCloseBtn.addEventListener("click", () => {
//   nav.classList.remove("openNav");
// });