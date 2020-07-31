
let rslider;
let gslider;
let bslider;

let sizeslider;
let hardnessslider;


function setup() {
	createCanvas(400,400);
	noStroke();
	mouseX = -100;
	mouseY = -100;

	createP('<br><br>red: ');           // dont ask
	rslider = createSlider(0, 255, 0, 1);
	createP('green: ');
	gslider = createSlider(0, 255, 0, 1);
	createP('blue: ');
	bslider = createSlider(0, 255, 0, 1);
	rslider.style('width', '150px');
	gslider.style('width', '150px');
	bslider.style('width', '150px');

	createP('<br>size');
	sizeslider = createSlider(100, 250, 100, 1);
	sizeslider.style('width', '120px');
	createP('hardness');
	hardnessslider = createSlider(3, 30, 10, 1);
	hardnessslider.style('width', '120px');
}

function draw() {
	if (createVector(pmouseX-mouseX, pmouseY-mouseY).mag() > 0) {
		fill(rslider.value(), gslider.value(), bslider.value(), hardnessslider.value());
		ellipse(mouseX, mouseY, sizeslider.value());
	}
}


