const b1 = document.querySelector("button"),
      ul = document.querySelector("ul");

function remove_dessert(li) {
    li.parentElement.removeChild(li);
}

function ajouter_dessert(ev) {
    let li = document.createElement("li");
    li.textContent = prompt("Nouveau dessert:");
    li.onclick = () => remove_dessert(li);
    ul.appendChild(li);
}

b1.onclick = ajouter_dessert;

// Main

ul.childNodes.forEach(li => li.onclick = () => remove_dessert(li));