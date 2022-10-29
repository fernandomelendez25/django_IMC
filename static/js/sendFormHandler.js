// Inputs
const calcForm = document.getElementById("calc_form");
const pesoInput = document.getElementById("id_peso");
const estaturaInput = document.getElementById("id_estatura");

// Outputs
const estaturaOutput = document.getElementById("result-estatura");
const pesoOutput = document.getElementById("result-peso");
const imcOutput = document.getElementById("result-imc");
const imcClassOutput = document.getElementById("result-imc-class");

// Listeners

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const fillResults = (data) => {
    estaturaOutput.textContent = estaturaInput.value;
    pesoOutput.textContent = pesoInput.value;
    imcOutput.textContent = data.imc;
    imcClassOutput.textContent = data.imc_class;
}

calcForm.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log("Listening");
    const peso = pesoInput.value;
    const estatura = estaturaInput.value;
    const data = {
        peso,
        estatura
    }
    console.log(data);
    const csrftoken = getCookie('csrftoken');
    fetch("/", {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data)
    }).then(response => response.json()).then(data => {
        console.log(data);
        fillResults(data);
    }
    )
})


