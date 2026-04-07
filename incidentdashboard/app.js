// Incident Response Dashboard App

let alertsData = [];
let activeCount = 0;
let resolvedCount = 0;

// Load alerts from JSON
fetch("data/alerts.json")
.then(response => response.json())
.then(data => {

    alertsData = data;

    renderAlerts();
    updateCounters();

});


// Render Alerts to Dashboard

function renderAlerts() {

    const container =
        document.getElementById("alerts");

    container.innerHTML = "";

    alertsData.forEach(alert => {

        if (alert.status !== "Resolved") {

            const div =
                document.createElement("div");

            div.className =
                "alert " + alert.severity;

            div.innerHTML = `

                <strong>${alert.severity}</strong>
                - ${alert.title}
                <br>
                Time: ${alert.time}

                <br><br>

                <button onclick="acknowledge(${alert.id})">
                    Acknowledge
                </button>

                <button onclick="investigate(${alert.id})">
                    Investigating
                </button>

                <button onclick="resolveIncident(${alert.id})">
                    Resolve
                </button>

            `;

            // Click alert → load logs
            div.onclick = () => loadLogs(alert.id);

            container.appendChild(div);

        }

    });

}


// Update Active / Resolved Counters

function updateCounters() {

    activeCount =
        alertsData.filter(a =>
            a.status !== "Resolved"
        ).length;

    resolvedCount =
        alertsData.filter(a =>
            a.status === "Resolved"
        ).length;

    document.getElementById("activeCount")
        .innerText = activeCount;

    document.getElementById("resolvedCount")
        .innerText = resolvedCount;

}


// Status Actions

function acknowledge(id) {

    updateStatus(id, "Acknowledged");

}

function investigate(id) {

    updateStatus(id, "Investigating");

}

function resolveIncident(id) {

    updateStatus(id, "Resolved");

    renderAlerts();
    updateCounters();

}


// Update Status Helper

function updateStatus(id, status) {

    alertsData.forEach(alert => {

        if (alert.id === id) {

            alert.status = status;

        }

    });

    updateCounters();

}


// Load Logs

function loadLogs(id) {

    fetch("logs/sample-logs.txt")
    .then(response => response.text())
    .then(data => {

        const logViewer =
            document.getElementById("logs");

        logViewer.textContent =
            "Incident ID: " + id +
            "\n\n" +
            data;

    });

}


// Simulated New Alerts (Optional)

const incidentTypes = [

"API Latency > 500ms",
"TLS Certificate Expiring",
"Disk Usage > 85%",
"Unauthorized Login Attempt",
"High Memory Usage Detected"

];

function generateRandomAlert() {

    const newId =
        alertsData.length + 1;

    const randomTitle =
        incidentTypes[
            Math.floor(
                Math.random() *
                incidentTypes.length
            )
        ];

    const newAlert = {

        id: newId,
        severity: randomSeverity(),
        title: randomTitle,
        time: new Date()
            .toLocaleTimeString(),
        status: "Active"

    };

    alertsData.unshift(newAlert);

    renderAlerts();
    updateCounters();

}


// Random Severity Generator

function randomSeverity() {

    const levels =
        ["CRITICAL", "HIGH", "MEDIUM"];

    return levels[
        Math.floor(
            Math.random() *
            levels.length
        )
    ];

}


// Auto-generate alerts every 30 seconds

setInterval(
    generateRandomAlert,
    30000
);


// Live Clock

setInterval(() => {

    const clock =
        document.getElementById("clock");

    if (clock) {

        clock.innerText =
            new Date()
            .toLocaleTimeString();

    }

}, 1000);


// Add Notes Persistence (local browser)

const notesField =
    document.getElementById("notes");

if (notesField) {

    notesField.value =
        localStorage.getItem("incidentNotes") || "";

    notesField.addEventListener("input", () => {

        localStorage.setItem(
            "incidentNotes",
            notesField.value
        );

    });

}