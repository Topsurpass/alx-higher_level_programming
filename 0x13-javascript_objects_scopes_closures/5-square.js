#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  size;
  constructor (size) {
    super(size, size);
  }
};
