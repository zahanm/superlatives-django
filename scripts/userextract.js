
var fs, connection, residents, fields, dorm, dump;

fs = require('fs');

connection = require('mysql').createConnection( require('./dbauth') );

residents = {};
fields = ['sunetid', 'first_name', 'last_name', 'gender'];
dorm = 'Cardenal';
dump = fs.createWriteStream('people.json');

connection.connect();

connection.query(
'SELECT '+ fields.join(', ') + ' FROM roster WHERE dorm = ? LIMIT 2',
[ dorm ],
function(err, rows, fields) {
  if (err) { console.error(err); return; }
  console.log('Result:', rows);
  dump.end();
});

connection.end();
