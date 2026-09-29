const complaintForm = document.getElementById("complaintForm");
const complaintsList = document.getElementById("complaintsList");
const message = document.getElementById("message");
const refreshButton = document.getElementById("refreshButton");

async function loadComplaints() {
    try {
        const response = await fetch("/api/complaints");
        const complaints = await response.json();

        if (complaints.length === 0) {
            complaintsList.innerHTML = "<p>No complaints submitted yet.</p>";
            return;
        }

        complaintsList.innerHTML = complaints.map(complaint => `
            <div class="complaint">
                <h3>Complaint #${complaint.id}</h3>
                <p><strong>Name:</strong> ${complaint.name}</p>
                <p><strong>Category:</strong> ${complaint.category}</p>
                <p><strong>Details:</strong> ${complaint.details}</p>
                <p class="status">
                    <strong>Status:</strong> ${complaint.status}
                </p>
            </div>
        `).join("");

    } catch (error) {
        complaintsList.innerHTML =
            "<p>Unable to load complaints.</p>";
    }
}

complaintForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const complaint = {
        name: document.getElementById("name").value,
        category: document.getElementById("category").value,
        details: document.getElementById("details").value
    };

    try {
        const response = await fetch("/api/complaints", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(complaint)
        });

        const result = await response.json();

        if (!response.ok) {
            message.textContent = result.error;
            return;
        }

        message.textContent = result.message;
        message.style.color = "green";

        complaintForm.reset();

        loadComplaints();

    } catch (error) {
        message.textContent = "Unable to submit complaint.";
        message.style.color = "red";
    }
});

refreshButton.addEventListener("click", loadComplaints);

loadComplaints();

