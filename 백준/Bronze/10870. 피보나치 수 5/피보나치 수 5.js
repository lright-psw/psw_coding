const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'C:/psw/python/input.txt'; 
let num = fs.readFileSync(filePath).toString().trim(); 

function fibo(num) {
    if (num == 0) 
        return 0;
    else if (num <= 2) {
        return 1;
    }
    return fibo(num - 1) + fibo(num - 2);
}

console.log(fibo(num))