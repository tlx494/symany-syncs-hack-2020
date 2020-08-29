const regex = '<a href="(.*?)".*?aria-label="([^"]*?)".*?target=".*?".*?data-lynx-uri=".*?">';

let page_loaded = false;

let posts = {};

window.onload = function () {
    page_loaded = true;
    console.log('Starting Symany...');
}

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
                postWindow.classList.add('dodgy');
            }

            console.log('Updated posts:')
            console.log(posts);
        }
    }
}

window.setInterval(function () {
    searchForArticles();
}, 1000);
