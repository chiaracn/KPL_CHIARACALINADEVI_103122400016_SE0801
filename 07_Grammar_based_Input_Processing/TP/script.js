function toNumberArray(number) {
  return number
    .split(",")
    .map(item => item.trim())
    .map(item => Number(item))
    .filter(item => !isNaN(item));
}

// Testing
console.log(toNumberArray("1, 2"));
console.log(toNumberArray("1 , 2"));
console.log(toNumberArray("11,55,33"));
console.log(toNumberArray("0.2, -11, abc23"));