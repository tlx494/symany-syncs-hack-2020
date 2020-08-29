
window.onload = function () {
  var checkbox = document.querySelector("input[name=active-toggle]");

  let extensionOn = false;
  getStatus();


  if (extensionOn == null) {
    extensionOn = true;
    setStatus(true);
  } else {
    if (checkbox.checked && !extensionOn) {
      checkbox.click();
    } else if (!checkbox.checked && extensionOn) {
      checkbox.click();
    }
  }

  checkbox.addEventListener('change', function () {
    if (this.checked) {
      extensionOn = true;
      setStatus(true);
      console.log("on");
    } else {
      extensionOn = false;
      setStatus(false);
      console.log("off");
    }
  });

  const setStatus = (isOn) => {
    return chrome.storage.sync.set({ 'extensionOn': isOn });
  }

  const getStatus = () => {
    chrome.storage.sync.get('extensionOn', function (res) {
      extensionOn = res;
    });
  }

};

