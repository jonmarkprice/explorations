const express = require('express');
const app = express();
app.use('/static', express.static('public'));
console.log('Listening on port 8080');
app.listen(8080);
