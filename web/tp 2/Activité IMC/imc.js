"use strict"

const BU_CALC = document.querySelector("button"),
      P_IMC = document.getElementById("imc"),
      P_MEAN = document.getElementById("interpretation");

var data = {}, 
    imc = {
	details: {
	    "Anorexie ou dénutrition": 16,
	    "Maigreur": 16.5,
	    "Maigreur": 18.5,
	    "Corpulence normale": 25,
	    "Surpoids": 30,
	    "Obésité modérée (Classe 1)": 35,
	    "Obésité élevée (Classe 2)": 40
	},
	hover: "Obésité morbide ou massive"	
    };

// Functions

function getInput(input){
    data[input.name] = parseFloat(input.value);
}

function meanIMC(imc_V){
    for(let i in imc.details) {
	if (imc_V < imc.details[i]) return i;
    }
    return imc.hover;
}

function calcIMC(){
    P_MEAN.textContent = meanIMC((P_IMC.textContent = data.poids/data.taille**2)) ;
}

// Setup

document.querySelectorAll("input").forEach(input => {
    input.oninput = () => getInput(input);
    getInput(input);
});
calcIMC();
BU_CALC.onclick = calcIMC;
