#!/usr/bin/node

/*
Write a class Rectangle that defines a rectangle:
Instance attributes: width, height;
Constructor arguments/parameter: w, h;
*/

module.exports = class Rectangle {
  width;
  height;
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
