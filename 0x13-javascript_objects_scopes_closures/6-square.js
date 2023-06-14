#!/usr/bin/node

const BaseSquareModel = require('./5-square.js');

module.exports = class Square extends BaseSquareModel {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
