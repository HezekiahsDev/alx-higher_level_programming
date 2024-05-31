#!/usr/bin/node

const { argv } = require('process');
const n = parseInt(argv[2]);
const cIsFun = (i) => {
	  for (; i > 0; i--) console.log('C is fun');
};

Number.isInteger(n) ? cIsFun(n) : console.log('Missing number of occurrences');
