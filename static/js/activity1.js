// const context = document.getElementById("data-set").getContext("2d");
const context2 = document.getElementById("data-set2").getContext("2d");

// let line = new Chart(context, {});
let line2 = new Chart(context2, {});

//Values from the form
const intialAmount = document.getElementById("initialamount");
const years = document.getElementById("years");
// const rates = document.getElementById("rates");
const rates2 = document.getElementById("rates2");

const compound = document.getElementById("compound");

//Messge
// const message = document.getElementById("message");
const message2 = document.getElementById("message2");

//The calculate button
const button = document.querySelector(".input-group button");

//Attach an event listener
// button.addEventListener("click", calculateGrowth);
button.addEventListener("click", calculateGrowth2);


// const data = [];
// const labels = [];

// function calculateGrowth(e) {
//     e.preventDefault();
//     data.length = 0;
//     labels.length = 0;
//     let growth = 0;
//     try {
//         const initial = parseInt(intialAmount.value);
//         const period = parseInt(years.value);
//         const interest = parseInt(rates.value);
//         const comp = parseInt(compound.value);

//         for(let i = 1; i <= period; i++) {
//             const final = initial * Math.pow(1 + ((interest / 100) / comp), comp * i);
//             data.push(toDecimal(final, 2));
//             labels.push("Year " + i);
//             growth = toDecimal(final, 2);
//         }
//         //
//         message.innerText = `You will have this amount ${growth} after ${period} years`;
//         drawGraph();
//     } catch (error) {
//         console.error(error);
//     }
// }

// function drawGraph() {
//     line.destroy();
//     line = new Chart(context, {
//         type: 'line',
//         data: {
//             labels,
//             datasets: [{
//                 label: "compound",
//                 data,
//                 fill: true,
//                 backgroundColor: "rgba(12, 141, 0, 0.7)",
//                 borderWidth: 3
//             }]
//         }
//     });
// }

const data2 = [];
const labels2 = [];

function calculateGrowth2(e) {
    e.preventDefault();
    data2.length = 0;
    labels2.length = 0;
    let growth2 = 0;
    try {
        const initial = parseInt(intialAmount.value);
        const period = parseInt(years.value);
        const interest2 = parseInt(rates2.value);
        // const comp = parseInt(compound.value);

        for(let i = 1; i <= period; i++) {
            const final2 = interest2 * i;
            // const final2 = ( initial * interest2 * i ) / 100;
            data2.push(toDecimal(final2, 2));
            labels2.push("Year " + i);
            growth2 = toDecimal(final2, 2);
        }
        //
        message2.innerText = `You will have $${growth2} after ${period} years with Simple Interest ${data2}`;
        drawGraph2();
    } catch (error) {
        console.error(error);
    }
}

function drawGraph2() {
    line2.destroy();
    line2 = new Chart(context2, {
        type: 'line',
        data: {
            labels2,
            datasets: [{
                label: "Simple Interest",
                data2,
                fill: true,
                backgroundColor: "rgba(12, 141, 0, 0.7)",
                borderWidth: 3
            }]
        }
    });
}

function toDecimal(value, decimals) {
    return +value.toFixed(decimals);
}