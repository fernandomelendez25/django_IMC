// Inputs
const calcForm = document.getElementById("calc_form");
const pesoInput = document.getElementById("id_peso");
const estaturaInput = document.getElementById("id_estatura");

// Outputs
const estaturaOutput = document.getElementById("result-estatura");
const pesoOutput = document.getElementById("result-peso");
const imcOutput = document.getElementById("result-imc");
const imcClassOutput = document.getElementById("result-imc-class");

// Variables para el calculo del IMC
const imc = 32.5;

// Llena los campos del area de resultados
// data es el resultado de la peticion POST que devuelve el valor imc y imc_class
const fillResults = (data) => {
    estaturaOutput.textContent = data.estatura + " metros";
    pesoOutput.textContent = data.peso + " kg";
    imcOutput.textContent = data.imc;
    imcClassOutput.textContent = data.imc_class;
}

// Maneja el evento submit del formulario
// Envia los datos del formulario al servidor y llena los campos del area de resultados
calcForm.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log("Vista de calculadora principal");
    const pesoVal = pesoInput.value;
    const estaturaVal = estaturaInput.value;
    const peso = parseFloat(pesoVal);
    const estatura = parseFloat(estaturaVal);

    if (isNaN(peso) || isNaN(estatura)) {
        alert("Peso o estatura no son numeros");
        return;
    }

    const imc = (peso / (estatura * estatura)).toFixed(2);
    const imcClass = getIMCClass(imc);

    fillResults({
        imc: imc,
        imc_class: imcClass,
        peso: peso,
        estatura: estatura
    })


})

// Obtiene la clase del IMC
// imc es el valor del imc
const getIMCClass = (imc) => {
    if (imc < 18.5) {
        return "Bajo peso";
    } else if (imc < 25) {
        return "Peso normal";
    } else if (imc < 30) {
        return "Sobrepeso";
    } else {
        return "Obesidad";
    }
}