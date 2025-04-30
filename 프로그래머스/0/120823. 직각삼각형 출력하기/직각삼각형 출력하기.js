const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input;

rl.on('line', function (line) {
    input = parseInt(line); // 숫자로 변환
    rl.close(); // 입력 종료
}).on('close', function () {
    for (let i = 1; i <= input; i++) {
        console.log('*'.repeat(i));
    }
});