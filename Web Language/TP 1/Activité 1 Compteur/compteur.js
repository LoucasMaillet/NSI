const  btn_clic = document.getElementById("clic"),
       btn_reset = document.getElementById("raz"),
       val_compteur = document.getElementById("compteurClics");

var n = 0;

function click(ev) {
    val_compteur.textContent = ev.target.id === "clic" ? n+=1 : n=0;
}

btn_clic.onclick = click;
btn_reset.onclick = click;