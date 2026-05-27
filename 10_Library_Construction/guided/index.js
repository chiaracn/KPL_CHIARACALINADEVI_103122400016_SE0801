/**
 *  Persamaa Linear Satu Variabel dan dua suku
 * @param {string} x 
 * @param {number} a 
 * @returns 
 */

export function pslv_dua(x, a) {

    const coeff = parseInt(x);
    const hasil = a / coeff;
    return {
        "x": x,
        "dengan": "=",
        hasil
    }
}

/** *  Persamaa Linear Satu Variabel dan tiga suku
 * @param {string} x 
 * @param {number} a 
 * @param {number} b  
 */

export function pslv_tiga(x, a, b) {
    let hasil = 0;

    if (x.length === 1) {
        hasil = b - a;
    } else if (x.length >= 2) {
        const coeff = parseInt(x);
        hasil = (b - a) / coeff;
    }
    return {
        "x": x,
        "dengan": "=",
        hasil
    }
}

/**
 * @param {string} x
 * @param {number} a
 * @param {number} b
 */

export function ptlsv_dua(x,a,op,b){
    let hasil = 0;

    const balikkan_op = {
        ">": "<",
        "<": ">",
        ">=": "<=",
        "<=": ">="
    }

    const coeff = parseInt(x);

    if (x.length === 1) {
        hasil = b - a;
    } else if (x.length >= 2) {
        const coeff = parseInt(x);
        hasil = (b - a) / coeff;
    }

    const op_baru = coeff <= -1 ? balikkan_op : [op] 

    return {
        "x": x,
        "dengan": op_baru || op,
        hasil
    }
}