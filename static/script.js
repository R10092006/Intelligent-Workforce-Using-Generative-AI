function analyzeTask() {
    let task = document.getElementById("task").value;

    if (task === "") {
        alert("Please enter a task");
        return;
    }

    fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task: task })
    })
    .then(res => res.json())
    .then(data => {
        let result = data.result;

        let output = document.getElementById("output");
        output.innerText = result;

        // Color logic
        output.className = "";
        if (result.includes("High")) output.classList.add("high");
        else if (result.includes("Schedule")) output.classList.add("meeting");
        else if (result.includes("Risk")) output.classList.add("risk");
        else output.classList.add("normal");

        // Add to history table
        let row = `<tr><td>${task}</td><td>${result}</td></tr>`;
        document.getElementById("history").innerHTML += row;
    });
}