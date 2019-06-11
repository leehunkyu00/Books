const client = require('cheerio-httpcli');
const urlType = require('url');

const url = "http://jpub.tistory.com"
const param = {};

client.fetch(url, param, function(err, $, res) {
    if (err) { console.log("error: ", err); return; }

    const body = $.html();
    console.log(body);

    // get link
    $("a").each(function(idx) {
        let text = $(this).text();
        let href = $(this).attr('href');        // relative address
        if (!href) return;
        let href2 = urlType.resolve(url, href); // absolute address

        // console.log(text, ":", href);
        console.log(text, ":", href2);
    });
});