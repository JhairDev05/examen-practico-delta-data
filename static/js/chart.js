document.addEventListener("DOMContentLoaded", function () {
    const ctxTotal = document.getElementById("totalCreditosChart").getContext("2d");
    const ctxClientes = document.getElementById("creditosPorClienteChart").getContext("2d");
    const ctxRangos = document.getElementById("creditosPorRangoChart").getContext("2d");

    new Chart(ctxTotal, {
        type: "bar",
        data: {
            labels: ["Total Créditos"],
            datasets: [{
                label: "Monto Total de Créditos",
                data: [totalCreditos],
                backgroundColor: "#36A2EB",
                borderColor: "#fff",
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: "bottom"
                }
            }
        }
    });

    new Chart(ctxClientes, {
        type: "bar",
        data: {
            labels: labelsClientes,
            datasets: [{
                label: "Monto por Cliente",
                data: dataClientes,
                backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });

    new Chart(ctxRangos, {
        type: "bar",
        data: {
            labels: labelsRangos,
            datasets: [{
                label: "Monto por Rango",
                data: dataRangos,
                backgroundColor: ["#FF5733", "#33FF57", "#3357FF", "#F3FF33"]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
});

