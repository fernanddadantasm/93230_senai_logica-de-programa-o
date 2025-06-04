// Crie um vetor que contenha 6 números, informe quantos são pares e quantos são ímpares 

console.clear(); // LIMPA A TELA DO TERMINAL
const readline = require('readline-sync');

const numerosPares = [];
const numerosImpares = [];
const numeros = [];
for (let i = 0; i < 6; i++) {
    const numero = readline.questionInt(`Informe o ${i+1}º número: `);
    numeros.push(numero);
    if (numero % 2 === 0) {
        numerosPares.push(numero);
    } else {
        numerosImpares.push(numero);
    }
}
console.log(`Números informados: ${numeros}`);
console.log(`Quantidade de números pares: ${numerosPares.length}`);
console.log(`Quantidade de números ímpares: ${numerosImpares.length}`);
console.log(`Números pares: ${numerosPares}`);
console.log(`Números ímpares: ${numerosImpares}`);


