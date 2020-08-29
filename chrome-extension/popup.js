isExtensionOn = true;
console.log(isExtensionOn);

window.onload = function () {
  var checkbox = document.querySelector("input[name=active-toggle]");

  checkbox.addEventListener( 'change', function() {
      if(this.checked) {
        isExtensionOn = true;
        console.log("on");
      } else {
        isExtensionOn = false;
        console.log("off");
      }
  });
};