module.exports = {
  entry: './script.js',
  output: {filename: 'bundle.js'}, // Can name this whatever you like, but most people call it bundle.js
  module: {
    loaders: [ // array of things you want to load
        {test: /\.js?/, loader: 'babel-loader', exclude: /node_modules/} // test any file ending with .js, specify loader, and exclude node_modules.
    ]
  }
};
