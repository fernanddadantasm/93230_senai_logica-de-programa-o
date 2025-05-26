// Criando uma função
function somar (a, b) {
    return a + b;
}

function subtrair (a, b) {
    return a - b;
}
function multiplicar (a, b) {
    return a * b;
}
function dividir (a, b) {
    return a / b;
}

// Chamando a função
// Adicionar o resultado da função na constante 

const soma = somar(10, 20);
const subtracao = subtrair(20,10);
const multiplicacao = multiplicar(20,10);
const divisao = dividir(20, 10);
console.log(`Soma: ${soma}`);
console.log(`Subtração: ${subtracao}`);
console.log(`Multiplicação: ${multiplicacao}`);
console.log(`Divisão: ${divisao}`);