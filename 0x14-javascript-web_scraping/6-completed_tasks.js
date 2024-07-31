#!/usr/bin/node
// Web scraper logic

const request = require('request');

// Make a GET request to the URL provided as the first command line argument
request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error); // Log any errors
    return;
  }

  const tasksCompleted = {}; // Object to store the count of completed tasks by user ID

  // Iterate through each to-do item in the response body
  body.forEach((todo) => {
    if (todo.completed) { // Check if the task is completed
      if (!tasksCompleted[todo.userId]) { // If user ID not in tasksCompleted, initialize it
        tasksCompleted[todo.userId] = 1;
      } else { // If user ID is already in tasksCompleted, increment the count
        tasksCompleted[todo.userId] += 1;
      }
    }
  });

  console.log(tasksCompleted); // Log the result
});
