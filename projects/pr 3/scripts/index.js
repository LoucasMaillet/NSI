"use strict"

const MAIN = document.querySelector("main"),
    PREV = document.querySelector("button:first-of-type"),
    NEXT = document.querySelector("button:last-of-type"),
    TIMELINE = {
        bar: document.querySelector("object"),
        div: document.querySelector("footer>div")
    },
    // Everything is based from https://en.wikipedia.org/wiki/History_of_Linux
    SECTIONS = [
        {
            name: "Linus Torwalds",
            year: 1991,
            url: "https://fr.wikipedia.org/wiki/Linus_Torvalds",
            img: "https://pi.tedcdn.com/r/talkstar-photos.s3.amazonaws.com/uploads/f69760c8-2dea-43ce-9594-f02ca4175946/LinusTorvalds_2016-embed.jpg",
            text: "While studying computer science at University of Helsinki, Linus Torvalds began a project that later became the Linux kernel. He wrote the program specifically for the hardware he was using and independent of an operating system because he wanted to use the functions of his new PC with an 80386 processor. Development was done on MINIX using the GNU C Compiler.",
            label: "The kernel"
        },
        {
            name: "HJ Lu",
            year: 1992,
            url: "https://en.wikipedia.org/wiki/HJ_Lu",
            img: "https://www.linux.co.cr/free-unix-os/review/1995/images/76.gif",
            text: "HJ Lu is a computer programmer credited with creating the first Linux distribution in 1992, titled Boot/Root.",
            label: "The first distro"
        },
        {
            name: "Ian Murdock",
            year: 1993,
            url: "https://fr.wikipedia.org/wiki/Ian_Murdock",
            img: "https://www.liberation.fr/resizer/gm9bzzFQWcGtIa87Fa1XedlcAbo=/1440x810/filters:format(jpg):quality(70)/cloudfront-eu-central-1.images.arcpublishing.com/liberation/UQZ26ATNJGJJKDUUFTSZ2VA6YY.jpg",
            text: "While a college student, Murdock founded the Debian project in August 1993, and wrote the Debian Manifesto in January 1994. Murdock conceived Debian as a Linux distribution that embraced open design, contributions, and support from the free software community.",
            label: "The first stable distro"
        },
        {
            name: "Larry Ewing",
            year: 1996,
            url: "https://en.wikipedia.org/wiki/Larry_Ewing",
            img: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Larry_ewing_linuxtag2007_berlin.jpg/220px-Larry_ewing_linuxtag2007_berlin.jpg",
            text: "Larry Ewing provided the original draft of the actual penguin. The name Tux was suggested by James Hughes as derivative of Torvalds' UniX.",
            label: "The mascot, Tux"
        },
        {
            name: "Matthias Ettrich",
            year: 1996,
            url: "https://en.wikipedia.org/wiki/Matthias_Ettrich",
            img: "https://25years.kde.org/assets/img/gallery/2005wikipedia.jpg",
            text: "Among his concerns was that none of the applications looked or behaved alike. In his opinion, desktop applications of the time were too complicated for end users. In order to solve the issue, he proposed the creation of a desktop environment in which users could expect the applications to be consistent and easy to use.",
            label: "The first GUI, KDE"
        },
        {
            name: "Miguel de Icaza",
            year: 1997,
            url: "https://en.wikipedia.org/wiki/Miguel_de_Icaza",
            img: "https://bimmcp.files.wordpress.com/2017/02/miguel-de-icaza.jpg",
            text: "Miguel de Icaza with Federico Mena started developping GNOME as a free desktop environment, to make an alternative to KDE for license purposes. GNOME is now use in big distro such as Ubuntu or Fedora",
            label: "The second GUI, GNOME"
        }
    ];

var current,
    sections = {},
    size = {
        width: window.innerWidth * .5,
        height: window.innerHeight * .5
    },
    cursor = {
        x: 0,
        y: 0
    };

//* Functions

/**
 * Get current cursor or finger position from the center
 * @param {Object} {clientX, clientY} Mouse / finger coordonates 
 */
function getCursor({ clientX, clientY }) {
    cursor.x = clientX - size.width;
    cursor.y = clientY - size.height;
}

/**
 * Navigate to another section
 * @param {HTMLElement} section The new section to go
 */
function setCurrent(section) {
    current.time.className = current.className = '';
    MAIN.scrollTo({ left: (current = section).offsetLeft, behavior: "smooth" });
    current.className = current.time.className = "appear";
    TIMELINE.bar.style.width = current.percent;
    // WARNING : Technicaly this will turn in an endless event loop but idk how navigator fix it.
    if (window.location != current.id) window.location = current.id;
}

/**
 * Generate HTML content from object
 * @param {Object} {name, year, url, img, label, text} Content of section
 */
function genSection({ name, year, url, img, label, text }) {
    let section = document.createElement("section");
    sections[section.id = `#${name.replace(/\s/g, '-')}`] = section;
    section.time = document.createElement('time');
    section.time.style.left = section.percent = `${Math.round(100 / (SECTIONS.length - 1) * MAIN.childElementCount)}%`;
    section.time.textContent = year;
    section.time.onclick = () => setCurrent(section);
    TIMELINE.div.appendChild(section.time);
    section.innerHTML = `
        <a href="${url}" title="Click to see more">
            <img src="${img}">
            <div>
                <h2>${name}</h2>
                <p>${text}</p>
                <label>${label}</label>
            </div>
        </a>`;
    MAIN.appendChild(section);
}

/**
 * Render light & shadow & parallax animation, 
 * partly based on https://codepen.io/rudyt7/pen/ExjVwya
 */
function render() {
    current.firstElementChild.style.transform = `perspective(100em) rotateY(${cursor.x / size.width}rad) rotateX(${-cursor.y / size.height}rad)`;
    let x = cursor.x * -4 / size.width,
        y = cursor.y * -4 / size.height;
    MAIN.style.filter = `drop-shadow(var(--c-s-0) ${x}em ${y}em 4em) drop-shadow(var(--c-l-0) ${-x}em ${-y}em 1.5em)`;
    current.firstElementChild.firstElementChild.style.transform = `translate(${x}em, ${y}em)`;
    window.requestAnimationFrame(render);
}

/**
 * Go to the next or first section
 */
function next() { setCurrent(current.nextElementSibling || MAIN.firstElementChild) }

/**
 * Go to the previous or last section
 */
function previous() { setCurrent(current.previousElementSibling || MAIN.lastElementChild) }

//* Events

// Previous button
PREV.onclick = previous;
PREV.ondblclick = () => setCurrent(MAIN.firstElementChild);
// Next button
NEXT.onclick = next;
NEXT.ondblclick = () => setCurrent(MAIN.lastElementChild);
// Go to the correct section
window.onhashchange = () => setCurrent(sections[window.location.hash] || MAIN.firstElementChild);
// Keyboard navigation
window.onkeydown = ({ key }) => {
    switch (key) {
        case "ArrowLeft": previous(); break;
        case "ArrowRight": next(); break;
    }
};
// Fix issues with scroll position & window size
window.onresize = () => {
    MAIN.scrollLeft = current.offsetLeft;
    size = { width: window.innerWidth * .5, height: window.innerHeight * .5 };
};
// Get cursor position
window.onmousemove = getCursor;
window.ontouchmove = ({ touches }) => getCursor(touches[0]);

//* Setup

document.body.onload = () => {
    // Create each sections
    SECTIONS.forEach(genSection);
    // Get & set current page
    if (!(current = sections[window.location.hash])) {
        MAIN.scrollLeft = (current = MAIN.firstElementChild).offsetLeft
    }
    current.className = current.time.className = "appear";
    TIMELINE.bar.style.width = current.percent;
    // And start rendering content
    render();
}
