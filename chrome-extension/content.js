const regex = '<a href="(.*?)".*?aria-label="([^"]*?)".*?target=".*?".*?data-lynx-uri=".*?">';

const verifyPost = async (title, link) => {

    let url = 'http://35.244.79.248/check-post'
    let options = {
        method: 'POST',
        mode: 'no-cors',
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


// verifyPost('This is a title', 'https://dodgywebsite.com');


const searchForArticles = async () => {
    // let posts = document.querySelectorAll('userContentWrapper')
    document.querySelectorAll('div.userContentWrapper > div > div > div.data-testid="post_message" div > > div > span > div > div > a')
    document.querySelectorAll('a[href][aria-label][target]');
}