#!/usr/bin/node

/*
Write a class Rectangle that defines a rectangle:
Instance attributes: width, height;
Constructor arguments/parameter: w, h;
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
