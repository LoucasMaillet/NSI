"use strict"

const PARA = document.querySelectorAll("p"),
      COLORS = {
        red: document.querySelector("input[name='red']"),
        green: document.querySelector("input[name='green']"),
        blue: document.querySelector("input[name='blue']"),
      };

// First version, the basic one:

//function set_color_(color){
//    PARA.forEach(p => p.style.backgroundColor = color);
//}

//function changer_couleur(ev){
//    switch (ev.key) { // ev.keyCode is depreciated
//        case 'r': set_color_("red"); break;
//        case 'v': set_color_("green"); break;
//        case 'b': set_color_("blue"); break;
//        case 'j': set_color_("yellow");
//    }
//}

//document.addEventListener("keypress",changer_couleur);

// And the second one:

function set_color() {
    PARA.forEach(p => p.style.backgroundColor = `rgb(${COLORS.red.value}%,${COLORS.green.value}%,${COLORS.blue.value}%)`);
}

// Setup

document.body.onload = () => {
    document.onkeypress = (ev) => {
    	switch (ev.key) {
        	case 'r': {
            	COLORS.red.value=(parseInt(COLORS.red.value)+1)%100; 
            	break;
        	}
        	case 'g': {
            	COLORS.green.value=(parseInt(COLORS.green.value)+1)%100; break;
        	}
        	case 'b': COLORS.blue.value=(parseInt(COLORS.blue.value)+1)%100;
    	}
    	set_color();
    };
    for (let color in COLORS) {
        COLORS[color].oninput = set_color;
    }
    set_color();
}