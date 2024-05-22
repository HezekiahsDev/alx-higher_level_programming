#!/usr/bin/node
// count movies with given character ID
const request = require('request');
let n = 0;

req.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((mov) => {
      mov.characters.forEach((character) => {
        if (character.includes(18)) {
          n += 1;
        }
      });
    });
    console.log(n);
  }
});
