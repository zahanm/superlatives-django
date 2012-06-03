
var fs, path;

fs = require('fs');
path = require('path');

function dumpqs (qsfile) {
  fs.readFile(qsfile, function(err, contents) {
    if (err) { console.error(err); return; }
    questions = JSON.parse(String(contents));
    questions.forEach(function(q) {
      console.log(q.fields.qtext, ' <=> ', q.fields.istwoans ? 'twoans': 'oneans');
    });
  });
}

if (require.main === module) {
  if (process.argv.length === 3) {
    dumpqs(process.argv[2]);
  } else {
    console.log('usage:', path.basename(__filename), '<questions file>');
  }
}
