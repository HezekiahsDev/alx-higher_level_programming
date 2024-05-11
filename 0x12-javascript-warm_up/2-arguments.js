#!/usr/bin/node

// check if argument is available
const argsCount = process.argv.length - 2; // Subtracting 2 to exclude 'node' and the script file path

if (argsCount === 0) {
    console.log("No argument");
} else if (argsCount === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
