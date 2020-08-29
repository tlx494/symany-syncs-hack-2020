const regex = '<a href="(.*?)".*?aria-label="([^"]*?)".*?target=".*?".*?data-lynx-uri=".*?">';

let page_loaded = false;

let posts = {};

window.onload = function () {
    page_loaded = true;
    console.log('Starting Symany...');
}


// chrome.contextMenus.create({
//     title: "This is a test",
//     contexts: ["selection"],
//     onclick: searchSimilar()
// })

const verifyPost = async (title, link) => {

    let url = 'https://symanyapi.gq/check-post';
    let options = {
        method: 'POST',
        headers: {
            'Accept': '*/*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title,
            link: link
        })
    };

    let response = await fetch(url, options);

    if (response.ok) {
        let data = await response.json();
        return data;
    } else {
        console.log('Got a bad response from the server:');
        console.log(response);
        return null;
    }

}

const searchForArticles = async () => {
    if (!page_loaded) {
        return;
    }
    let postLink = document.querySelectorAll('div.userContentWrapper > div > div > div > div > div > div > div > div > span > div > a[aria-label]');

    for (let i = 0; i < postLink.length; i++) {
        let postWindow = postLink[i].parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
        let postWindowChild = postLink[i].parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
        let headline = postLink[i].getAttribute('aria-label');
        let link = postLink[i].getAttribute('href');

        if (!(headline in posts)) {
            console.log(`Adding to list of known posts - ${headline}`);
            posts[headline] = {
                'link': link,
                'postWindowRef': postWindow
            }

            // console.log(headline, link);
            let verified = await verifyPost(headline, link);
            if (verified == null) {
                console.log('Could not verify post');
            }

            if (!(verified['domain_is_dodgy'] || verified['title_is_dodgy'])) { // invert this later
                postWindowChild.classList.add('dodgy');
                let alertDiv = document.createElement('div');
                let alertDiv2 = document.createElement('div');

                let button1 = document.createElement('button');
                button1.setAttribute('type', 'button');
                button1.classList.add('btn', 'btn-primary', 'button1');
                button1.innerHTML = 'Search Online';

                button2.setAttribute('type', 'button');
                button2.classList.add('btn', 'btn-primary', 'button2');
                button2.innerHTML = 'See anyway';

                verified['domain_is_dodgy'] = true; // delete this later
                verified['warning_msg'] = 'This source is known for producing fake news' // delete this later

                let alertText = '';
                if (verified['domain_is_dodgy'] && verified['title_is_dodgy']) {
                    alertText = `${verified['warning_msg']} and ${verified['title_warning']}`
                } else if (verified['domain_is_dodgy']) {
                    alertText = verified['warning_msg'];
                } else if (verified['title_is_dodgy']) {
                    alertText = verified['title_warning'];
                }

                let text = document.createTextNode('WARNING');
                let text2 = document.createTextNode(alertText);

                alertDiv.classList.add('alert-popup');
                alertDiv2.classList.add('alert-popup-small');

                alertDiv.appendChild(text);
                alertDiv2.appendChild(text2);
                postWindow.appendChild(alertDiv);
                postWindow.appendChild(alertDiv2);
                postWindow.appendChild(button1);
                postWindow.appendChild(button2);
            }

            console.log('Updated posts:')
            console.log(posts);
        }
    }
}

window.setInterval(function () {
    searchForArticles();
}, 1000);
