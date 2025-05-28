// Faça o usuário informar um número e imprima a tabuada desse número.
 
const readlineSync = require(`readline-sync`)

let numero = parseInt(readlineSync.question("Digite um número: "))

console.log(`Tabela do número ${numero}`)

for (let i = 1; i <= 10; i++){
    let resultado = numero * i;
    console.log(`${numero} x ${i} = ${resultado}`)
}