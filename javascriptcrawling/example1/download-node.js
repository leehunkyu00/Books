// let url = "http://jpub.tistory.com";     // status code : 301
// let url = "http://nogari.kr";               // status code : 200
let url = "http://devkyu.tistory.com/873";
let savePath = "test.html";

let http = require('http');
let fs = require('fs');

let outfile = fs.createWriteStream(savePath);

http.get(url, function(res) {
    console.log("statusCode : ", res.statusCode);
    res.pipe(outfile);
    res.on('data', function(chuck) {
        console.log("Body :", chuck);
    })
    res.on('end', function() {
        outfile.close();
        console.log("ok")

    });
})

