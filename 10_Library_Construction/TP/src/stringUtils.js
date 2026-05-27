export function hitungHuruf(teks) {
  const cocok = teks.match(/[A-Za-z]/g);
  return cocok ? cocok.length : 0;
}

export function hitungKata(teks) {
  const cocok = teks.match(/[A-Za-z]+/g);
  return cocok ? cocok.length : 0;
}