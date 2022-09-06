#!/usr/bin/node

const Square = require('./5-square');

module.exports = class Square extends Square {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
};
