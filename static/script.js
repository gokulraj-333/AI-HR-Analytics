let chart = null;
let historyList = [];

// Load KPI Cards
async function loadKPIs() {

    const res = await fetch("/kpis");
    const data = await res.json();

    document.getElementById("total").innerText = data.total;
    document.getElementById("active").innerText = data.active;
    document.getElementById("left").innerText = data.left;
    document.getElementById("attrition").innerText = data.attrition + "%";
    document.getElementById("salary").innerText = "₹" + Number(data.salary).toLocaleString();
    document.getElementById("performance").innerText = data.performance;
    document.getElementById("satisfaction").innerText = data.satisfaction;
    document.getElementById("years").innerText = data.years;

}

loadKPIs();


// Ask AI
async function askAI() {

    const question = document.getElementById("question").value.trim();

    if (question === "") {
        alert("Please enter a question.");
        return;
    }

    const res = await fetch("/ask", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question: question
        })

    });

    const data = await res.json();

    if (!data.success) {
        alert(data.error);
        return;
    }

    document.getElementById("sql").textContent = data.sql;

    createTable(data.columns, data.rows);

    drawChart(data.columns, data.rows);

    document.getElementById("answer").innerHTML =
        formatInsight(data.insight);

    addHistory(question);

}


// Create Result Table
function createTable(columns, rows) {

    let html = "<tr>";

    columns.forEach(col => {

        html += `<th>${col}</th>`;

    });

    html += "</tr>";

    rows.forEach(row => {

        html += "<tr>";

        row.forEach(value => {

            html += `<td>${value}</td>`;

        });

        html += "</tr>";

    });

    document.getElementById("resultTable").innerHTML = html;

}


// Draw Chart
function drawChart(columns, rows) {

    if (chart) {

        chart.destroy();

    }

    if (columns.length < 2) return;

    const labels = [];
    const values = [];

    rows.forEach(r => {

        labels.push(r[0]);
        values.push(Number(r[1]));

    });

    chart = new Chart(

        document.getElementById("resultChart"),

        {

            type: "bar",

            data: {

                labels: labels,

                datasets: [

                    {

                        label: columns[1],

                        data: values

                    }

                ]

            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        display: false

                    }

                }

            }

        }

    );

}


// Format AI Insight
function formatInsight(text) {

    return text
        .replace(/\n/g, "<br>")
        .replace(/📊/g, "<b>📊</b>")
        .replace(/🔍/g, "<b>🔍</b>")
        .replace(/💡/g, "<b>💡</b>");

}


// Recent Questions
function addHistory(question) {

    historyList.unshift(question);

    if (historyList.length > 10) {

        historyList.pop();

    }

    const ul = document.getElementById("history");

    ul.innerHTML = "";

    historyList.forEach(q => {

        const li = document.createElement("li");

        li.innerText = q;

        li.onclick = function () {

            document.getElementById("question").value = q;

        };

        ul.appendChild(li);

    });

}


// Export CSV
function exportCSV() {

    const table = document.getElementById("resultTable");

    let csv = [];

    for (let row of table.rows) {

        let cols = [];

        for (let cell of row.cells) {

            cols.push(cell.innerText);

        }

        csv.push(cols.join(","));

    }

    const blob = new Blob(

        [csv.join("\n")],

        {

            type: "text/csv"

        }

    );

    const a = document.createElement("a");

    a.href = URL.createObjectURL(blob);

    a.download = "query_result.csv";

    a.click();

}


// Press Enter to Ask
document
    .getElementById("question")
    .addEventListener("keypress", function (e) {

        if (e.key === "Enter") {

            askAI();

        }

    });