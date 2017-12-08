module.exports = {
  entry: "./client/index.js",
  module: { loaders: [{loader: 'babel-loader', test: /\js$/}]},
  output: {
    path: __dirname + "/dist",
    filename: "bundle.js"
  }
};

