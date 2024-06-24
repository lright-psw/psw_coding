const fs = require('fs');

fs.readFile('/dev/stdin', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    
    let inputLines = data.trim().split('\n');
    let n = parseInt(inputLines[0]);
    
    for (let i = 1; i <= n; i++) {
        let ps = inputLines[i];
        let cnt = 0;
        let isValid = true;
        
        for (let j = 0; j < ps.length; j++) {
            if (ps[j] === '(') {
                cnt++;
            } else if (ps[j] === ')') {
                cnt--;
            }
            
            if (cnt < 0) {
                console.log("NO");
                isValid = false;
                break;
            }
        }
        
        if (isValid) {
            if (cnt === 0) {
                console.log("YES");
            } else {
                console.log("NO");
            }
        }
    }
});