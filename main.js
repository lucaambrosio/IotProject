/*const { spawn } = require('child_process');
const util = require('util');
const py = spawn('python', ['code.py']);
*/

var x = document.getElementsByClassName("button");
for (var i = 0; i < x.length; i++) {
    x[i].addEventListener("click", myFunction);
}
var y = document.getElementsByClassName("button1");
for (var j = 0; j < y.length; j++) {
    y[j].addEventListener("click", myFunction1);
}


function myFunction(event) {
    var clickedElement = event.target;
    var id=clickedElement.id;
    let xhr = new XMLHttpRequest;
    xhr.open('GET', 'http://localhost:3000/devices/cbyId/5/run?cell=' + id); // vai in restmanager a implementarla
    // dovrà contenere una chiamata allo script python
    // script.run() invocherà this.driver.run()
    // il driver sarà composto dal contenuto di start.js e invocherà il python
    xhr.send(null);
    document.getElementById("area").value = "Position " + clickedElement.name + "\n";
    document.getElementById("immagine").src = "C:\\Users\\User\\Documents\\Supsi2019\\SummerSchool\\ProgettoIoT\\project-5\\immaginesalvata";

}
function myFunction1(event) {
    var clickedElement = event.target;
    document.getElementById("area").value = "Position " + clickedElement.name + " is not selectable \n";
    document.getElementById("immagine").src = "C:\\Users\\User\\Documents\\Supsi2019\\SummerSchool\\ProgettoIoT\\project-5\\bianca.jpg"

}

