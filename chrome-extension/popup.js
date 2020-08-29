var ss = document.getElementById("customSwitch1");

(ss).click(function() {
  if((ss).prop("checked")){
    chrome.runtime.sendMessage({isOn: "true"}, function(response) {
      console.log(response.farewell);
    });
  }
  else{
    chrome.runtime.sendMessage({isOn: "false"}, function(response) {
      console.log(response.state);
    });
  }
});