const context = document.getElementById("data-set").getContext("2d");
const context2 = document.getElementById("data-set2").getContext("2d");

//Values from the form
const intialAmount = document.getElementById("initialamount");
const years = document.getElementById("years");
const rates = document.getElementById("rates");
// const rates2 = document.getElementById("rates2");

const compound = document.getElementById("compound");

//Messge
const message = document.getElementById("message");
const message2 = document.getElementById("message2");

//The calculate button
const button = document.querySelector(".input-group button");

//Attach an event listener
button.addEventListener("click", calculateGrowth);

const data = [];
const data2 = [];
const labels = [];
let click_counter = 0;
let line;
let line2;

function calculateGrowth(e) {
    e.preventDefault();
    data.length = 0;
    labels.length = 0;
    let growth = 0;
    let growth2 = 0;
    try {
        const initial = parseInt(intialAmount.value);
        const period = parseInt(years.value);
        const interest = parseInt(rates.value);
        const comp = parseInt(compound.value);

        for (let i = 1; i <= period; i++) {
            let final = initial * Math.pow(1 + ((interest / 100) / comp), comp * i);
            data.push(toDecimal(final, 2));
            let final2 = (initial * interest * i) / 100;
            data2.push(toDecimal(final2, 2))
            labels.push("Year " + i);
            growth = toDecimal(final, 2);
            growth2 = toDecimal(final2, 2);
        }
        //
        message.innerText = `You will have $${numberWithCommas(toDecimal(growth, 0))} after ${period} years`;
        message2.innerText = `You will have $${numberWithCommas(toDecimal(growth2, 0))} after ${period} years`;
        drawGraph();
        drawGraph2();
    } catch (error) {
        console.error(error);
    }
}

function drawGraph() {
    if (click_counter > 0) {
        line.destroy();
    }
    line = new Chart(context, {
        type: 'line',
        data: {
            labels,
            datasets: [
                {
                    label: "Compound Interest",
                    data: data,
                    fill: true,
                    backgroundColor: "green",
                    borderWidth: 3
                }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    min: 0
                }
            }
        }
    });
}

function drawGraph2() {
    if (click_counter > 0) {
        line2.destroy();
    }
    line2 = new Chart(context2, {
        type: 'line',
        data: {
            labels,
            datasets: [{
                label: "Simple Interest",
                data: data2,
                fill: true,
                backgroundColor: "rgba(12, 141, 0, 0.7)",
                borderWidth: 3
            }],
            scales: {
                y: {
                    min: 0,
                }
            }
        }
    });

    click_counter = click_counter + 1;
}

function toDecimal(value, decimals) {
    return +value.toFixed(decimals);
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}