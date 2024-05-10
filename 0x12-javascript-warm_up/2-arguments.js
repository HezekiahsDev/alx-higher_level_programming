#!/usr/bin/node

const arg_len = process.argv.length;
console.log(arg_len === 2 ? 'No argument' : arg_len === 3 ? 'Argument found');
