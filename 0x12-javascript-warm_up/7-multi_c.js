#!/usr/bin/node

// print multiple strings (n = number of occurence)

let i = Number(process.argv[2]);
if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else if (i > 0) {
  for (i = 0; i > 0; --i) {
    console.log('C is fun');
  }
}
