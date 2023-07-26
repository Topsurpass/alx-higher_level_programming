#!/usr/bin/node

// script that computes the number of tasks completed by user id.

const url = process.argv[2];
const req = require('request');

req(url, (err, res) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(res.body);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (dic[tasks[i].userId] === undefined) {
          dic[tasks[i].userId] = 1;
        } else {
          dic[tasks[i].userId]++;
        }
      }
    }
    console.log(dic);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
