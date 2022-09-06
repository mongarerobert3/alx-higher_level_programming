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
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // double method
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
