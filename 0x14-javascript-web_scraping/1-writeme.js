#!/usr/bin/node
// write into a file

const filesys = require('fs');

filesys.writeFile(process.argv[2], process.argv[3], 'utf-8',
	function (err) {
		if (err) {
			console.log(err);
		}
	});
