// Faça um algortimo que leia dois valores inmteiro A e B;
// se os valores forem iguais, deverá se somar os dois;
// caso contrario multiplique
// Ao final de qualquer um dos calculos, deve-seatribuir o resultado a 
// uma variavel c e mostrar seu conteudo no temrinal;

const readline = require('readline-sync')

let a = readline.questionInt('Digite o valor de A: ')
let b = readline.questionInt('Digite o valor de B: ')
let c = 0

if (a == b) {
    c = a + b
} else {
    c = a * b
}

console.log(`Resultado: ${c}`)

