#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let i = list.lenght - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return (rev);
};
