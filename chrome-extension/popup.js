window.onload = function () {
  var checkbox = document.querySelector("input[name=active-toggle]");

  checkbox.addEventListener( 'change', function() {
      if(this.checked) {
        isExtensionOn = false;
        console.log("off");
      } else {
        isExtensionOn = true;
        console.log("on");
      }
  });
};