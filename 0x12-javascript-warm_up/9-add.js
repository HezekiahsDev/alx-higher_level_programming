#!/usr/bin/node
//add two ints from args

function add (a, b) {
	return (a + b);
}
const { argv } = require('process');
const i = parseInt(argv[2]);
const j = parseInt(argv[3]);

console.log(add(i, j));
