const API_BASE = "http://127.0.0.1:8000";

const downloadBtn = document.getElementById("downloadBtn");
const input = document.getElementById("donorName");
const status = document.getElementById("status");

input.focus();

function setStatus(message, type = "") {
    status.textContent = message;
    status.className = type;
}

async function fetchPdf() {

    const donorName = input.value.trim();

    if (!donorName) {
        setStatus("Enter a name first.", "error");
        return null;
    }

    setStatus("Generating...");
    downloadBtn.disabled = true;

    try {

        const res = await fetch(`${API_BASE}/generate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                donor_name: donorName
            }),
        });

        if (!res.ok) {
            throw new Error(`HTTP ${res.status}`);
        }

        const pdfBlob = await res.blob();

        const certificateNumber =
            res.headers.get("X-Certificate-Number") || "certificate";

        return {
            blob: pdfBlob,
            certificateNumber
        };

    } catch (err) {
        console.error(err);

        setStatus(`Failed: ${err.message}`, "error");
        return null;

    } finally {

        downloadBtn.disabled = false;

    }
}

downloadBtn.addEventListener("click", async () => {

    const result = await fetchPdf();

    if (!result) return;

    const url = URL.createObjectURL(result.blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = `${result.certificateNumber}.pdf`;

    document.body.appendChild(a);
    a.click();
    a.remove();

    URL.revokeObjectURL(url);

    setStatus(
        `Downloaded ${result.certificateNumber}.pdf`,
        "success"
    );

});

input.addEventListener("keydown", (e) => {

    if (e.key === "Enter") {
        downloadBtn.click();
    }

});