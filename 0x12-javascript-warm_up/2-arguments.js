#!/usr/bin/node
const NumArguments = process.argv;
if (NumArguments.length < 3) {
  console.log('No argument');
} else if (NumArguments.length < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
