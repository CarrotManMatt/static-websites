function increase(amount) {
    let counter = Number(document.getElementById("counter").innerHTML);
    if (counter + amount > 0) {
        for (let button of document.getElementsByClassName("decrease")) {
            button.disabled = false;
        }
    }
    document.getElementById("counter").innerHTML = (counter + amount).toString();
}

function decrease(amount) {
    let counter = Number(document.getElementById("counter").innerHTML);
    if (counter - amount <= 0) {
        document.getElementById("counter").innerHTML = "0";
        for (let button of document.getElementsByClassName("decrease")) {
            button.disabled = true;
        }
    } else {
        document.getElementById("counter").innerHTML = (counter - amount).toString();
    }
}

function names() {
    document.getElementById("button-1").innerHTML = "Motorbike";
    document.getElementById("button-2").innerHTML = "Sports-car/Smartcar";
    document.getElementById("button-3").innerHTML = "Medium Car";
    document.getElementById("button-4").innerHTML = "Family Car/SUV";
    document.getElementById("button-5").innerHTML = "Van/Single Decker Bus";
    document.getElementById("button-6").innerHTML = "Small Lorry/Double Decker Bus/Special Van";
    document.getElementById("button-7").innerHTML = "Lorry/Special Small Lorry/Coach";
    document.getElementById("button-8").innerHTML = "Special Lorry";
    document.getElementById("button-9").innerHTML = "Working Vehicle";
}

function points() {
    document.getElementById("button-1").innerHTML = "1 Point";
    document.getElementById("button-2").innerHTML = "2 Points";
    document.getElementById("button-3").innerHTML = "3 Points";
    document.getElementById("button-4").innerHTML = "4 Points";
    document.getElementById("button-5").innerHTML = "5 Points";
    document.getElementById("button-6").innerHTML = "6 Points";
    document.getElementById("button-7").innerHTML = "7 Points";
    document.getElementById("button-8").innerHTML = "8 Points";
    document.getElementById("button-9").innerHTML = "9 Points";
}
