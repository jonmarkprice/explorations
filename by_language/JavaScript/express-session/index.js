// Following: https://glebbahmutov.com/blog/express-sessions/

const express = require('express')
//const parseurl = require('parseurl')
const session = require('express-session') // parses, validates session-cookie
const FileStore = require('session-file-store')(session) // stores in sessions/ folder

const app = express()
app.use(require('morgan')('dev'))
app.use(session({
  name: 'session-tutorial',
  secret: 'keyboard cat',
  saveUninitialized: true,
  resave: true,                           // was false
  store: new FileStore(),
}))
app.get('/', function initViewCount(req, res, next) {
  if (typeof req.session.views === 'undefined') {
    req.session.views = 0
    return res.end('Welcome to session demo, refresh page.')
  }
  return next()
})
app.get('/', function incrViewCount(req, res, next) {
  console.assert(typeof req.session.views === 'number', '!')
  req.session.views += 1
  return next() // he always returns next
})
app.use(function printSession(req, res, next) {
  console.log('req.session', req.session)
  return next()
})
app.get('/', function sendCounterPg(req, res) {
  // pretty sure this does all the same things as: setHeader, write, end
  res.send(`<p>views ${req.session.views}</p>\n`)
})

/*
app.use(function (req, res, next) {
  if (!req.session.views) {
    console.log("Resetting session")
    req.session.views = {}
  }

  // get the url pathname
  var pathname = parseurl(req).pathname

  // count the views
  console.log("Views %o", req.session.views)
  req.session.views[pathname] = (req.session.views[pathname] || 0) + 1

  next()
})

app.get('/foo', function (req, res, next) {
  res.send('you viewed this page ' + req.session.views['/foo'] + ' times')
})

app.get('/bar', function (req, res, next) {
  res.send('you viewed this page ' + req.session.views['/bar'] + ' times')
})
*/

console.log("Listening ...");
app.listen(8080);
