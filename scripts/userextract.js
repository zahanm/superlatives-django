
var fs, path, residents;

fs = require('fs');
path = require('path');
residents = {};

function extraction (dorm) {

  console.log('Extracting residents for', dorm);

  var connection, fields;

  connection = require('mysql').createConnection( require('./dbauth') );
  connection.connect();
  fields = ['sunetid', 'first_name', 'last_name', 'gender'];

  connection.query(
  'SELECT '+ fields.join(', ') + ' FROM roster WHERE dorm = ?',
  [ dorm ],
  function(err, rows, fields) {
    if (err) { console.error(err); return; }
    console.log('Result 1:', rows.length);
    rows.forEach(function(row) {
      residents[ row.sunetid ] = {
        gender: row.gender.match(/female/) ? 'f': 'm',
        sunetid: row.sunetid,
        staff: false,
        name: row.first_name + ' ' + row.last_name,
        year: 'f'
      };
    });
  });

  connection.query('SELECT sunetid FROM staff', function(err, rows, fields) {
    if (err) { console.error(err); return; }
    console.log('Result 2:', rows.length);
    rows.forEach(function(row) {
      if (row.sunetid in residents) {
        residents[ row.sunetid ].staff = true;
      }
    });
    // write out to file
    console.log('Residents:', Object.keys(residents).length);
    dumptojson();
  });

  connection.end();

}

function dumptojson () {
  var dump, modeldata;
  dump = fs.createWriteStream('people.json');
  modeldata = Object.keys(residents).map(function(sunetid, i) {
    return {
      pk: i+1,
      model: 'survey.resident',
      fields: residents[sunetid]
    };
  });
  dump.write(JSON.stringify(modeldata));
  dump.end();
}

if (require.main === module) {
  if (process.argv.length === 3) {
    extraction( process.argv[2] );
  } else {
    console.log('usage: node', path.basename(__filename), '<dorm name>');
  }
}
