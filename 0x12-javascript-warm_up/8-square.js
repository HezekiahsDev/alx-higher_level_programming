#!/usr/bin/node
//Square display

const { argv } = require('process');
const size = parseInt(argv[2]);

const printSquare = (size) => {
	const x = 'X'.repeat(size);
	for (let 1 = 0; i < size; i++)
		console.log(row);
};
Number.isInteger(size) ? printSquare(size) : console.log('Missing size');
