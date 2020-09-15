#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
