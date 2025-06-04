// Criando um vetor 
const frutas = ['Maça', 'Banana', 'Laranja', 'Uva', 'Pera']

console.log(frutas)
// Exibindo o primeiro elemento do vetor
console.log(frutas[0])
// Exibindo o segundo elemento do vetor
console.log(frutas[2])
// Exibindo o terceiro elemento do vetor        

frutas.push('Abacaxi') // Adicionando um elemento ao final do vetor
console.log(frutas[2])

frutas.pop() // Removendo o último elemento do vetor
console.log(frutas)

frutas.shift() // Removendo o primeiro elemento do vetor
console.log(frutas)

frutas.forEach((fruta, index) => {
    console.log(`${++index}: ${fruta}`) // Exibindo o índice e o valor de cada elemento do vetor
})

