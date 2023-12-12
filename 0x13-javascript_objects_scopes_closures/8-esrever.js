#!/usr/bin/node

exports.esrever = function (list) {
  const Array = [];
  for (let i = list.length - 1; i >= 0; i--) {
    Array.push(list[i]);
  }
  return Array;
};
