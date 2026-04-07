fetch("data/alerts.json")
.then(response => response.json())
.then(alerts => {

    const container = document.getElementById("alerts");

    alerts.forEach(alert => {

        const div = document.createElement("div");
        div.className = "alert";

        div.innerHTML =
            `<strong>${alert.severity}</strong>: ${alert.title}`;

        container.appendChild(div);

    });

});