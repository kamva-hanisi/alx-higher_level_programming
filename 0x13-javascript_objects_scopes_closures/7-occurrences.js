#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let NumOccurrences = 0;
  for (const number of list) {
    if (number === searchElement) {
      NumOccurrences += 1;
    }
  }
  return NumOccurrences;
};
