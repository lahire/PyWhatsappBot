// server.js
// where your node app starts

// init project
var express = require('express');
var app = express();



// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACde60019f8d64eac48ea794f384858795';
const authToken = '190461bdcf6989539c97085afee01524';
const client = require('twilio')(accountSid, authToken);
const MessagingResponse = require('twilio').twiml.MessagingResponse;

app.use(express.static('public'));

client.messages
      .create({
        body: 'Hello there!',
        from: 'whatsapp:+14155238886',
        to: 'whatsapp:+919725633422'
      })
      .then(message => console.log(message.sid))
      .done();


app.post('/incoming', (req, res) => {
  const twiml = new MessagingResponse();

  twiml.message('The Robots are coming! Head for the hills!');

  res.writeHead(200, {'Content-Type': 'text/xml'});
  res.end(twiml.toString());
});


app.get('/', function(request, response) {
  response.sendFile(__dirname + '/views/index.html');
});


var listener = app.listen(process.env.PORT, function() {
  console.log('Your app is listening on port ' + listener.address().port);
});

