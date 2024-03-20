const imageInput = document.getElementById("image");
const saveButton = document.getElementById("submit-button");
const outputImage = document.getElementById("output-image");

saveButton.addEventListener("pointerdown", () => {
  outputImage.classList.remove("invisible");
  outputImage.classList.add("visible");
});

function handleFormSubmit(event) {
    event.preventDefault();
    // Your logic to handle form submission data
}

