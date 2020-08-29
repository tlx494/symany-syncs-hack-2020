// window.addEventListener("DOMContentLoaded", function () {
//   var form = document.getElementById("news");

//   document.getElementById("your-id").addEventListener("click", function () {
//     form.submit();
// }

const verifyPost = async (title, link) => {

  let url = 'http://35.244.79.248/check-post'
  let options = {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json;charset=UTF-8'
    },
    body: JSON.stringify({
      title: title,
      link: link
    })
  };

  let response = await fetch(url, options);
  let responseOK = response && response.ok;
  if (responseOK) {
    let data = await response.json();

    console.log(data);
    // do something with data
  }
}

verifyPost('This is a title', 'https://dodgywebsite.com');
