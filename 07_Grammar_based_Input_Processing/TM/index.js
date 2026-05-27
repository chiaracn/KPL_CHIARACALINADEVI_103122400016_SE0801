function parseRobots(content) {
  const lines = content.split('\n');

  const result = [];
  let current = null;

  for (let line of lines) {
    line = line.trim();

    // skip baris kosong & komentar
    if (!line || line.startsWith('#')) continue;

   const [key, ...rest] = line.split(':');
const value = rest.join(':').trim();
    if (!key || !value) continue;

    switch (key.toLowerCase()) {
      case 'user-agent':
        // buat object baru
        current = {
          'User-agent': value,
          'Allow': [],
          'Disallow': [],
          'Sitemap': []
        };
        result.push(current);
        break;

      case 'allow':
        current?.Allow.push(value);
        break;

      case 'disallow':
        current?.Disallow.push(value);
        break;

      case 'sitemap':
        current?.Sitemap.push(value);
        break;
    }
  }

  return result;
}

module.exports = parseRobots;