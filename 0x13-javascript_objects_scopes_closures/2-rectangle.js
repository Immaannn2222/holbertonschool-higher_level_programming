#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      new Object();
    }
  }
};
console.log(Rectangle.name);
module.exports = Rectangle;
