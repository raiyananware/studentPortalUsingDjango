document.addEventListener("DOMContentLoaded", () => {
  console.log("ID received: " + id);
});

var scrollableContent = document.getElementsByClassName("FixedSizeDiv");

  scrollableContent.addEventListener("wheel", function(event) {
    scrollableContent.scrollTop += event.deltaY;
    event.preventDefault();
  });