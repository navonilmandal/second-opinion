// Content Script - Extractor
function extractPageText() {
    let text = document.body.innerText;
    // Compress multiple spaces/tabs into a single space
    text = text.replace(/[ \t]+/g, ' ');
    // Compress multiple newlines (3 or more) into double newlines to maintain paragraphs
    text = text.replace(/\n{3,}/g, '\n\n');
    return text.trim();
}

// Add floating button to trigger analysis
const btn = document.createElement('button');
btn.innerText = "Analyze Policy";
btn.style.position = 'fixed';
btn.style.bottom = '20px';
btn.style.right = '20px';
btn.style.zIndex = '999999';
btn.style.padding = '10px 20px';
btn.style.background = '#8b5cf6';
btn.style.color = 'white';
btn.style.border = 'none';
btn.style.borderRadius = '8px';
btn.style.cursor = 'pointer';
btn.style.boxShadow = '0 4px 12px rgba(0,0,0,0.3)';

btn.onclick = () => {
    // Check if chrome.runtime is available (it is undefined on local file:// URLs without permission or in PDF viewer)
    if (!chrome || !chrome.runtime || !chrome.runtime.sendMessage) {
        alert("Error: Extension cannot communicate with the background on this page. If this is a local file, please go to chrome://extensions, click 'Details' on this extension, and enable 'Allow access to file URLs'. Note: Direct PDF text extraction is not supported by the browser.");
        return;
    }

    const hostname = window.location.hostname;
    const isPDF = document.contentType === 'application/pdf' || window.location.href.toLowerCase().endsWith('.pdf');
    
    if (isPDF) {
        if (window.location.protocol === 'file:') {
            // Local PDFs cannot be fetched by content scripts.
            // Tell the sidebar to show an upload button.
            chrome.runtime.sendMessage({ type: 'LOCAL_PDF_DETECTED' });
        } else {
            // Online PDFs can be sent to the background to be fetched.
            chrome.runtime.sendMessage({ type: 'ANALYSIS_STARTED' });
            chrome.runtime.sendMessage({ 
                type: 'ANALYZE_PDF', 
                url: window.location.href, 
                hostname: hostname 
            }, (response) => {
                if (response && response.status === "success") {
                    alert(`Analysis Complete!\nRisk Level: ${response.risk_level}\nPolicy Score: ${response.score}`);
                } else {
                    alert("Analysis failed.");
                }
            });
        }
        return;
    }

    const text = extractPageText();
    if (!text || text.trim().length === 0) {
        alert("Error: No readable text found on this page.");
        return;
    }
    
    // Broadcast started event to the background/sidebar
    chrome.runtime.sendMessage({ type: 'ANALYSIS_STARTED' });
    
    // Send full page text for analysis
    chrome.runtime.sendMessage({ type: 'ANALYZE_PAGE', payload: text, hostname: hostname }, (response) => {
        if (response && response.status === "success") {
            alert(`Analysis Complete!\nRisk Level: ${response.risk_level}\nPolicy Score: ${response.score}`);
        } else {
            alert("Analysis failed.");
        }
    });
};

document.body.appendChild(btn);
