
var fs, connection;

fs = require('fs');

connection = require('mysql').createConnection( require('./dbauth') );

connection.connect();

connection.query('SELECT * FROM roster LIMIT 2', function(err, rows, fields) {
  if (err) { console.error(err); return; }
  console.log('Result:', rows);
});

connection.end();
