const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'C:/psw/python/input.txt'; 
let input = fs.readFileSync(filePath).toString().trim().split(' ');

const n = parseInt(input[0]);
const m = parseInt(input[1])

let visited = new Array(n).fill(false);
let ptr = [];

function back() {
    if (ptr.length == m) {
        console.log(ptr.join(" "))
    }
    for (let i = 1; i < n + 1; i++) {
        if (visited[i-1] == false){
            visited[i - 1] = true;
            ptr.push(i);
            back();
            visited[i - 1] = false;
            ptr.pop();
        }
    }
}

back()