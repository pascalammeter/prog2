document.querySelector('#berechnen').addEventListener('click', berechne_BMI);

function berechne_BMI () {
    var groesse = parseInt(document.getElementById("groesse").value);
    var gewicht = parseInt(document.getElementById("gewicht").value);
    var bmi = Math.round(100000 * gewicht / (groesse * groesse)) / 10;
    document.querySelector("output").textContent = bmi;
}

/*
   	document.getElementById("bmi")
		.value = bmi;
}
window.onload = function () {
	document.getElementById("berechnen")
		.onclick = berechne_BMI;