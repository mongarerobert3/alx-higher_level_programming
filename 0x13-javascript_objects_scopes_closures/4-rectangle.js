#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Dynamic method
  print () {
    for (let y = 0; y < this.height; y++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Rotate method
  rotate () {
    let temp;

    this.width = temp;
    this.height = this.width;
    this.temp = this.height;
  }

  // double method
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
