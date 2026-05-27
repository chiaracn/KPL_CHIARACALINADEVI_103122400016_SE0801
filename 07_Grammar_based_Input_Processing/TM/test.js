const fs = require('fs');
const path = require('path');
const parseRobots = require('./index');

// ambil salah satu file
const filePath = path.join(__dirname, 'daftar', 'openai.txt');

// baca isi file
const content = fs.readFileSync(filePath, 'utf-8');

// parse
const result = parseRobots(content);

// tampilkan hasil
console.log(JSON.stringify(result, null, 2));