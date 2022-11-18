var lado1 = prompt('1º Lado');
var lado2 = prompt('2º Lado');
var lado3 = prompt('3º Lado');

if (lado1 == lado2 && lado2 == lado3 && lado3 == lado1) {
    console.log('Triângulo Equilátero')
}
else if (lado1 != lado2 && lado2 != lado3 && lado3 != lado1) {
    console.log('Triângulo Escaleno');
}
else {
    console.log('Triângulo Isósceles')
}
