//Peça para o usuario informar um número, se o numero for maior que 10, repita a pergunta até que ele informe um número menor ou igual a 10.
const readline = require('readline-sync');
let numero = readline.questionInt("Digite um número: ");

while (numero > 10) {
    numero = readline.questionInt("Digite um número: ");
}
console.log(`Você digitou o número: ${numero}`);