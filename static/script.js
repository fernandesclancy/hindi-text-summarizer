document.getElementById('summarizeForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const text = document.getElementById('text').value.trim();
    const outputDiv = document.getElementById('summaryOutput');
    const loader = document.getElementById('loader');
    const summarizeBtn = document.getElementById('summarizeBtn');

    if (!text) {
        alert("Please enter some text");
        return;
    }

    loader.classList.remove('hidden');
    summarizeBtn.disabled = true;
    outputDiv.textContent = "Generating summary...";

    try {
        const response = await fetch('/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text })
        });

        const data = await response.json();

        if (response.ok) {
            outputDiv.textContent = data.summary;
        } else {
            outputDiv.textContent = "Error: " + (data.error || "Something went wrong");
        }
    } catch (error) {
        outputDiv.textContent = "Could not contact server. Please try again.";
    } finally {
        loader.classList.add('hidden');
        summarizeBtn.disabled = false;
    }
});

// 📋 Copy to Clipboard
document.getElementById('copyBtn').addEventListener('click', () => {
    const output = document.getElementById('summaryOutput').textContent;
    navigator.clipboard.writeText(output).then(() => {
        alert("Summary copied to clipboard!");
    }).catch(() => {
        alert("Failed to copy summary.");
    });
});

// ⬇️ Download Summary
document.getElementById('downloadBtn').addEventListener('click', () => {
    const text = document.getElementById('summaryOutput').textContent;
    const blob = new Blob([text], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'summary.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
});
