var webpack = require('webpack'); // require webpack

module.exports = {
  entry: './script.js',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules: [{ // used to be loaders object key
      test: /\.js?/,
      loader: 'babel-loader',
      exclude: /node_modules/,
			query: { // new key to handle presets
				presets: ['env']
			}
    }]
  }
};
