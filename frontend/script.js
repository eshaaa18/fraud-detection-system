let token = "";
async function login() {
  const res = await fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      email: document.getElementById("email").value,
      password: document.getElementById("password").value
    })
  });

  const data = await res.json();

  if (!data.access_token) {
    alert("Login failed ");
    return;
  }

  token = data.access_token;
  localStorage.setItem("token", token);

  alert("Login successful ");
}

async function sendTransaction() {
  token = localStorage.getItem("token");

  if (!token) {
    alert("Please login first!");
    return;
  }

  const res = await fetch("http://127.0.0.1:8000/transaction", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + token
    },
    body: JSON.stringify({
      user_id: parseInt(document.getElementById("user_id").value),
      amount: parseFloat(document.getElementById("amount").value),
      location: document.getElementById("location").value,
      device: document.getElementById("device").value
    })
  });

  const data = await res.json();

  document.getElementById("result").innerText =
    JSON.stringify(data, null, 2);
}

async function loadTransactions() {
  token = localStorage.getItem("token");

  const res = await fetch("http://127.0.0.1:8000/transactions", {
    headers: {"Authorization": "Bearer " + token}
  });

  const data = await res.json();
  renderTable("transactionsTable", data);
}

async function loadAlerts() {
  token = localStorage.getItem("token");

  const res = await fetch("http://127.0.0.1:8000/alerts", {
    headers: {"Authorization": "Bearer " + token}
  });

  const data = await res.json();
  renderTable("alertsTable", data);
}

async function loadStats() {
  token = localStorage.getItem("token");

  const res = await fetch("http://127.0.0.1:8000/stats", {
    headers: {"Authorization": "Bearer " + token}
  });

  const data = await res.json();

  // CLEAN UI STATS
  document.getElementById("stats").innerHTML = `
    <p><b>Total Transactions:</b> ${data.total_transactions}</p>
    <p><b>Fraud Count:</b> ${data.fraud_count}</p>
    <p><b>Fraud Rate:</b> ${data.fraud_rate.toFixed(2)}%</p>
  `;

  // CHART
  const ctx = document.getElementById("fraudChart").getContext("2d");

  new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["Fraud", "Safe"],
      datasets: [{
        data: [
          data.fraud_count,
          data.total_transactions - data.fraud_count
        ],
        backgroundColor: ["#ff4d94", "#66ff99"]
      }]
    }
  });
}

async function loadPerformance() {
  token = localStorage.getItem("token");

  const res = await fetch("http://127.0.0.1:8000/advanced-metrics", {
    headers: {"Authorization": "Bearer " + token}
  });

  const data = await res.json();

  document.getElementById("performance").innerHTML = `
    <p><b>Accuracy:</b> ${data.accuracy}</p>
    <p><b>Precision:</b> ${data.precision}</p>
    <p><b>Recall:</b> ${data.recall}</p>
    <p><b>TP:</b> ${data.tp} | <b>FP:</b> ${data.fp}</p>
    <p><b>TN:</b> ${data.tn} | <b>FN:</b> ${data.fn}</p>
  `;
}


function renderTable(tableId, data) {
  let table = document.getElementById(tableId);
  table.innerHTML = "";

  if (!data || data.length === 0) return;

  let headers = Object.keys(data[0]);

  // HEADER
  let headerRow = "<tr>";
  headers.forEach(h => headerRow += `<th>${h}</th>`);
  headerRow += "</tr>";
  table.innerHTML += headerRow;

  // ROWS
  data.forEach(row => {
    let rowHtml = "<tr>";

    headers.forEach(h => {
      let value = row[h];

      // FRAUD FLAG
      if (h === "fraud_flag") {
        value = value
          ? `<span class="fraud">🚨 HIGH RISK</span>`
          : `<span class="safe">✅ SAFE</span>`;
      }

      // RISK LEVEL
      if (h === "risk_level") {
        if (value === "HIGH") value = `<span class="fraud">HIGH</span>`;
        else if (value === "MEDIUM") value = `<span style="color:orange">MEDIUM</span>`;
        else value = `<span class="safe">LOW</span>`;
      }

      rowHtml += `<td>${value}</td>`;
    });

    rowHtml += "</tr>";
    table.innerHTML += rowHtml;
  });
}

setInterval(() => {
  if (window.location.href.includes("admin")) {
    loadTransactions();
    loadAlerts();
    loadStats();
    loadPerformance();
  }
}, 5000);