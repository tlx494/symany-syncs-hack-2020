const regex = '<a href="(.*?)".*?aria-label="([^"]*?)".*?target=".*?".*?data-lynx-uri=".*?">';

const verifyPost = async (title, link) => {

    let url = 'http://35.244.79.248/check-post'
    let options = {
        method: 'POST',
<<<<<<< HEAD
        mode: 'cors',
=======
        mode: 'no-cors',
>>>>>>> e0e7177ea14529e19701c06cdb87004db74fedbb
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


<<<<<<< HEAD
verifyPost('This is a title', 'https://dodgywebsite.com');
=======
// verifyPost('This is a title', 'https://dodgywebsite.com');
>>>>>>> e0e7177ea14529e19701c06cdb87004db74fedbb


const searchForArticles = async () => {
    // let posts = document.querySelectorAll('userContentWrapper')
<<<<<<< HEAD
    document.querySelectorAll('div.userContentWrapper div div div.data-testid="post_message" dev')
=======
    document.querySelectorAll('div.userContentWrapper > div > div > div.data-testid="post_message" div > > div > span > div > div > a')
>>>>>>> e0e7177ea14529e19701c06cdb87004db74fedbb
    document.querySelectorAll('a[href][aria-label][target]');
}