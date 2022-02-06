"use strict"

const FORM = document.querySelector("form"),
      [I_WEIGHT, I_HEIGHT] = document.querySelectorAll("input"),
      [S_IMC, S_MEAN] = document.querySelectorAll("span");

var imc = {
        details: {
            16: ["Anorexie ou dénutrition", "blue"],
            16.5: [ "Maigreur", "blue"],
            18.5: ["Maigreur", "blue"],
            25: ["Corpulence normale", "green"],
            30: ["Surpoids", "yellow"],
            35: ["Obésité moderée (Classe 1)", "red"],
            40: ["Obésité élevée (Classe 2)", "red"]
        },
	   hover: ["Obésité morbide ou massive", "red"]
    };

function getIMC() {
    return I_WEIGHT.value/I_HEIGHT.value**2;
}

function meanIMC(value){
    for(let i in imc.details) {
	   if (value < i) return imc.details[i];
    }
    return imc.hover;
}

function chgIMC(){
    [S_MEAN.textContent, FORM.className] = meanIMC((S_IMC.textContent = getIMC()));
}

// Setup

FORM.onsubmit = () => {chgIMC(); return false};
S_IMC.textContent = "None";
S_MEAN.textContent = "Please enter value.";