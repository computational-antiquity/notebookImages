// Define extra buttons for evaluting the Notebook and toggleing code visability.

function setDefault() {
	$('.input').slideToggle();
};
setDefault();

var startbutton = document.createElement("Button");
startbutton.innerHTML = "Start Notebook"
startbutton.style = "font-size:15px;top:0;right:0;margin-top:4px;margin-right:243px;position:absolute;z-index: 9999;"

startbutton.onclick = function() {
	Jupyter.notebook.execute_all_cells();
}.bind(startbutton);
document.body.appendChild(startbutton);

var codebutton = document.createElement("Button");
codebutton.innerHTML = " Toggle code  "
codebutton.style = "font-size:15px;top:0;right:0;margin-top:4px;margin-right:110px;position:absolute;z-index: 9999;"

codebutton.onclick = function() {
	$('.input').slideToggle();
}.bind(codebutton);
document.body.appendChild(codebutton);
