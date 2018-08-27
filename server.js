var express = require('express');
var app = express();
var request = require('request');
const bodyParser = require('body-parser');


const accountSid = 'ACde60019f8d64eac48ea794f384858795';
const authToken = '190461bdcf6989539c97085afee01524';
const client = require('twilio')(accountSid, authToken);
const MessagingResponse = require('twilio').twiml.MessagingResponse;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: false }));



app.post('/incoming', (req, res) => {
  const twiml = new MessagingResponse();
  
  request('https://api.duckduckgo.com/?skip_disambig=1&format=json&pretty=1&q='+req.body.Body, function (error, response, body) {
    console.log('body:', JSON.parse(body)["Abstract"]);
    
//     if(body["Abstract"] == ""){
// 	    body["Abstract"]= request["RelatedTopics"][0]["Text"]
// 	  }
    
    twiml.message("j");
    
  });
  res.writeHead(200, {'Content-Type': 'text/xml'});
  res.end(twiml.toString());
});


app.get('/', function(request, response) {
  response.sendFile(__dirname + '/views/index.html');
});


var listener = app.listen(process.env.PORT, function() {
  console.log('Your app is listening on port ' + listener.address().port);
});

