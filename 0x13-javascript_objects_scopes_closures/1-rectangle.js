#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
console.log(Rectangle.name);
module.exports = Rectangle;
