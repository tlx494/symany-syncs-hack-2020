// var ss = document.getElementById("customSwitch1");

// ($ss).click(function() {
//   if(($ss).prop("checked")){
//     chrome.runtime.sendMessage({isOn: "true"}, function(response) {
//       console.log(response.farewell);
//     });
//   }
//   else{
//     chrome.runtime.sendMessage({isOn: "false"}, function(response) {
//       console.log(response.state);
//     });
//   }
// });
console.log("hello");
var checkbox = document.querySelector("input[name=checkbox]");
console.log(checkbox)

checkbox.addEventListener('change', function () {
  if (this.checked) {
    console.log("hello");
  } else {
    console.log("hebyllo");
  }
});

window.onload = function () {
  $("#intro").click(function () {
    alert("clicked"); // Should fire now
  });
};