function change_value(val, diff) {
    let param = document.getElementById(val);
    let paramCurr = param.getAttribute("aria-valuenow");

    paramCurr = String(Number(paramCurr) + diff);
    param.setAttribute("aria-valuenow", paramCurr);

    param.style.width = paramCurr + '%';
    param.innerText = val + '(' + paramCurr + '/100)';
}

function eat() {
    change_value('HP', 4);
}

function study() {
    change_value('IQ', 6);
}

function sleep() {
    change_value('FUN', 3);
}

function allAtOnce() {
    change_value('HP', 4);
    change_value('IQ', 4);
    change_value('FUN', 4);
}

function addValuesToForm() {
    document.getElementById("id_HP").setAttribute("value", document.getElementById("HP").getAttribute("aria-valuenow"));
    document.getElementById("id_IQ").setAttribute("value", document.getElementById("IQ").getAttribute("aria-valuenow"));
    document.getElementById("id_FUN").setAttribute("value", document.getElementById("FUN").getAttribute("aria-valuenow"));
}