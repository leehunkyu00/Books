const RSS = `http://web.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109`;

const parseString = require('xml2js').parseString;
const request = require('request');

request(RSS, function (err, response, body) {
    if (!err && response.statusCode == 200) {
        analyzeRSS(body);
    }
});

function analyzeRSS(xml) {
    parseString(xml, function(err, obj) {
        if (err) { console.log(err); return; }

        const datas = obj.rss.channel[0].item[0].description[0].body[0].location[0].data;
        const city = obj.rss.channel[0].item[0].description[0].body[0].location[0].city;
        console.log(obj);

        for (let i in datas) {
            const data = datas[i];
            console.log(city + " " + data.tmEf + " " + data.wf + " " + data.tmn + "~" + data.tmx);
        }
    })
}