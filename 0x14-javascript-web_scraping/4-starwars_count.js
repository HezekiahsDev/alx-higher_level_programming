#!/usr/bin/node
// Count movies with given character ID
const request = require('request');
let n = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((mov) => {
      mov.characters.forEach((character) => {
        if (character.includes('18')) { // '18' should be a string to correctly match the character URL
          n += 1;
        }
      });
    });
    console.log(n);
  }
});

