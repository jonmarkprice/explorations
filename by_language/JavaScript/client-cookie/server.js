const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();

app.use(cookieParser());
app.use((req, res, next) => {
  console.log('Responding to %s', req.path);
  console.log('Cookies: %o', req.cookies);
  next();
});
app.use('/static', express.static('public'));

app.get('/ping', (req, res) => {
  console.log('Cookies');
  console.log(req.cookies);
  res.end(); // should set HTTP 200 OK, otherwise use sendStatus
});

console.log('Listening on port 8080');
app.listen(8080);
