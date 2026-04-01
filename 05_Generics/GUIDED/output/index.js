function fizzBuzz(input) {
  const deretLarik = input.split(" ");
  let hasil = "";

  for (const d of deretLarik) {
    const bil = +d;
    let fz = "";

    if (bil % 3 === 0) {
      fz += "Fizz";
    }
    if (bil % 5 === 0) {
      fz += "Buzz";
    }

    if (fz != "") {
      hasil += fz + " ";
      continue;
    }

    hasil += bil + " ";
  }

  return hasil.trim(); // biar rapi ga ada spasi di akhir
}

console.log(fizzBuzz("123 35 1 24 15 15 66 25 1 2"));