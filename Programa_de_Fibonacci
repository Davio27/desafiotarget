const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function isFibonacci(n) {
    let a = 0, b = 1;
    while (b < n) {
        let temp = a + b;
        a = b;
        b = temp;
    }
    return b === n || a === n;
}

rl.question("Digite um número: ", (input) => {
    const num = parseInt(input);
    if (isFibonacci(num)) {
        console.log(`O número ${num} pertence à sequência de Fibonacci.`);
    } else {
        console.log(`O número ${num} não pertence à sequência de Fibonacci.`);
    }
    rl.close();
});
