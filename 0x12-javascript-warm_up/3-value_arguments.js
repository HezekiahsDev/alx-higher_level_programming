#!/usr/bin/node
const { argv } = require('process');
let args_len = 0;

argv.forEach(() => args_len++);

console.log(args_len === 2 ? 'No argument' : argv[2]);
