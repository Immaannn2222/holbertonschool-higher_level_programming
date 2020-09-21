#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let j = 0;
  for (const i of list) {
    if (i === searchElement) {
      j += 1;
    }
  }
  return (j);
};
