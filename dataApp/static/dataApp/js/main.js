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