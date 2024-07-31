#!/usr/bin/node
// Script to fetch and print the names of characters in a Star Wars film from the Star Wars API

const request = require('request');

// Get the film ID from the command line arguments
const id = process.argv[2];

// Construct the URL to fetch the film data
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Make a GET request to the URL to get the film data
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error); // Log any errors
  } else {
    const content = JSON.parse(body); // Parse the response body as JSON
    const characters = content.characters; // Get the list of character URLs from the film data

    // Iterate over each character URL
    for (const character of characters) {
      // Make a GET request to the character URL to get character data
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error); // Log any errors for individual character requests
        } else {
          const names = JSON.parse(body); // Parse the response body as JSON
          console.log(names.name); // Print the name of the character
        }
      });
    }
  }
});
