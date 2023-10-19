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
// button.addEventListener("click", calculateGrowth2);

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

        for(let i = 1; i <= period; i++) {
            let final = initial * Math.pow(1 + ((interest / 100) / comp), comp * i);
            data.push(toDecimal(final, 2));
            let final2 = ( initial * interest * i ) / 100;
            data2.push(toDecimal(final2, 2))
            labels.push("Year " + i);
            growth = toDecimal(final, 2);
            growth2 = toDecimal(final2, 2);
        }
        //
        message.innerText = `You will have this amount ${growth} after ${period} years`;
        message2.innerText = `You will have this amount ${growth2} after ${period} years`;
        drawGraph();
        drawGraph2();
    } catch (error) {
        console.error(error);
    }
}

function drawGraph() {
    console.log(data)
    console.log(data2)
    if (click_counter > 0) {
        line.destroy();
    }
    line = new Chart(context, {
        type: 'line',
        data: {
            labels,
            datasets: [
            {
                label: "compound",
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
    console.log(data2);
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

// const data2 = [];
// const labels2 = [];

// function calculateGrowth2(e) {
//     e.preventDefault();
//     data2.length = 0;
//     labels2.length = 0;
//     let growth2 = 0;
//     try {
//         const initial = parseInt(intialAmount.value);
//         const period = parseInt(years.value);
//         const interest2 = parseInt(rates2.value);
//         // const comp = parseInt(compound.value);

//         for(let i = 1; i <= period; i++) {
//             const final2 = interest2 * i;
//             // const final2 = ( initial * interest2 * i ) / 100;
//             data2.push(toDecimal(final2, 2));
//             labels2.push("Year " + i);
//             growth2 = toDecimal(final2, 2);
//         }
//         //
//         message2.innerText = `You will have $${growth2} after ${period} years with Simple Interest ${data2}`;
//         drawGraph2();
//     } catch (error) {
//         console.error(error);
//     }
// }

function toDecimal(value, decimals) {
    return +value.toFixed(decimals);
}