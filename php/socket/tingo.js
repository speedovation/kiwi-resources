var Db = require('tingodb')().Db,
    assert = require('assert');

var db = new Db('/home/yash/DB', {});
// Fetch a collection to insert document into
var collection = db.collection("batch_document_insert_collection_safe");
// Insert a single document
collection.insert([{hello:'world_safe1'}
  , {hello:'world_safe2'}], {w:1}, function(err, result) {
  assert.equal(null, err);

  // Fetch the document
  collection.findOne({hello:'world_safe2'}, function(err, item) {
    assert.equal(null, err);
    assert.equal('world_safe2', item.hello);
  })
});



//php php-parse.php -d -p -N -d file.php

var exec = require("child_process").exec,
app;

app =	exec("php /home/yash/Projects/qt/kiwi/Build/debug/resources/php/parser/PHP-Parser/bin/php-parse.php  sample.php", 
			function (error, stdout, stderr) 
				{
					
					console.log('stdout: ' + stdout);
				    console.log('stderr: ' + stderr);
				    if (error !== null) {
				      console.log('exec error: ' + error);
				    }

				    collection.insert([{hello:JSON.parse(stdout)}] );

				});

