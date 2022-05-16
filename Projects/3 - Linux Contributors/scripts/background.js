const PI2 = Math.PI * 2;

async function getImg(src) {    
    return new Promise((res) => {
        let img = document.createElement("img");
        img.onload = () => res(img);
        img.crossOrigin = "anonymous";
        img.src = src;
    })
}

class P2D {
    constructor(x, y, w, color) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.color = color;
    }
    
    applyForce ({x, y, radius, value}) {
        const dx = this.x - x,
              dy = this.y - y,
              dh = Math.hypot(dx, dy);
        if (dh <= radius) {
            console.log(p)
            const factor = (radius - dh) / radius * value;
            this.x *= factor;
            this.y *= factor;
        }
    }
}


class Scene {
    constructor(cvs) {
        if(!(this.ctx = cvs.getContext("2d"))) throw new Error("Browser doesn't support 2d canvas API");
        let {width, height} = cvs.getBoundingClientRect();
        cvs.width = width;
        cvs.height = height;
        this.cvs = cvs;
        this.mw = width *.5;
        this.mh = height *.5;
        this.particules = [];
    }
    render(fn) {
        const loop = () => {
            this.ctx.clearRect(0, 0, this.cvs.width, this.cvs.height);
            fn();
            window.requestAnimationFrame(loop);
        };
        loop();
    }
    draw({x, y, w, color}){
        this.ctx.beginPath();
        this.ctx.fillStyle = color;
        this.ctx.arc(this.mw + x, this.mh + y, w, 0, PI2);
        this.ctx.fill();
        this.ctx.closePath();
    }
    drawImg(img, scale=.7) {
        img.width *= scale;
        img.height *= scale;
        img.left = this.mw - img.width*.5;
        img.top = this.mh - img.height*.5;
        this.ctx.drawImage(img, img.left, img.top, img.width, img.height);
    }
    async getPixelFromUrl(src, res) {
        const img = await getImg(src)
        scene.drawImg(img);
        const {data} = this.ctx.getImageData(img.left, img.top, img.width, img.height),
            pixelArray = [];
        res = img.width / res;
        for (let x = 0; x < img.width; x += res) {
            for (let y = 0; y < img.height; y += res) {
                const i =(y * 4 * img.height) + x * 4;
                if (data[i+3] === 0) continue;
                pixelArray.push(
                    new P2D(
                        x - img.width * .5, 
                        y - img.height * .5,
                        (data[i] + data[i+1] + data[i+2]) / 3 * (data[i+3] / 256) / 256 * res *.5,
                        `rgb(${data[i]},${data[i + 1]},${data[i+2]},${data[i+3]})`
                    )
                )
            }
        }
        return pixelArray;
    }
}

const scene = new Scene(document.querySelector("canvas"));
//scene.draw(new P2D(0, 0, 5, "red"));

/*(async () => {
    particules = await scene.getPixelFromUrl("https://images.unsplash.com/photo-1579353977828-2a4eab540b9a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c2FtcGxlfGVufDB8fDB8fA%3D%3D&w=1000&q=80", 100)
    scene.render(() => {
        particules.forEach(p => {
            p.applyForce({x:500, y:100, radius:100, value:10});
            scene.draw(p);
        });
    })
})()*/