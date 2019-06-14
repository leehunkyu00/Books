const client = require('cheerio-httpcli');
const request = require('request');
const fs = require('fs');
const urlType = require('url');

const savedir = __dirname + "/img";
if (!fs.existsSync(savedir)) {
    fs.mkdirSync(savedir);
}

const url = "https://ko.wikipedia.org/wiki/" + encodeURIComponent("강아지");
const param = {};

client.fetch(url, param, function(err, $, res) {
    if (err) { console.log(err); return;}

    $("img").each(function(idx) {
        let src = $(this).attr('src');
        src = urlType.resolve(url, src);

        let fname = urlType.parse(src).pathname;
        fname = savedir + "/" + fname.replace(/[^a-zA-Z0-9.]+/g, '_');

        request(src).pipe(fs.createWriteStream(fname));
    }) 
});