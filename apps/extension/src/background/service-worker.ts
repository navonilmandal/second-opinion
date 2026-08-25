// Background Service Worker
chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true }).catch((error) => console.error(error));

// Store pending sendResponse callbacks for async PDF extraction
const pendingResponses: any = {};

// Helper function to run the backend pipeline
function runBackendPipeline(payload: string, hostname: string, sendResponse: any) {
    // 1. Upload the text as a file to get a document_id
    const blob = new Blob([payload], { type: 'text/plain' });
    const formData = new FormData();
    formData.append('file', blob, 'page_extract.txt');

    // Broadcast UI update
    chrome.runtime.sendMessage({ type: "ANALYSIS_STATUS", message: "Uploading text to AI backend..." });

    fetch("https://second-opinion-gy3d.onrender.com/api/v1/documents/upload", {
        method: "POST",
        body: formData
    })
    .then(uploadRes => uploadRes.json())
    .then(uploadData => {
        const documentId = uploadData.document_id;
        
        let providerId = "hdfc_ergo_seed";
        if (hostname.includes("tataaig")) providerId = "tata_aig_seed";
        else if (hostname.includes("icicilombard")) providerId = "icici_lombard_seed";
        else if (hostname.includes("newindia")) providerId = "new_india_assurance_seed";
        else if (hostname.includes("uiic.co.in")) providerId = "united_india_insurance_seed";
        else if (hostname.includes("nationalinsurance")) providerId = "national_insurance_seed";
        else if (hostname.includes("starhealth")) providerId = "star_health_seed";
        else if (hostname.includes("bajajallianz")) providerId = "bajaj_allianz_seed";
        else if (hostname.includes("sbigeneral")) providerId = "sbi_general_seed";
        else if (hostname.includes("careinsurance")) providerId = "care_health_seed";
        
        // Broadcast UI update
        chrome.runtime.sendMessage({ type: "ANALYSIS_STATUS", message: "Generating AI Embeddings & Analyzing Legal Clauses..." });
        
        // 2. Call the analyze endpoint with the document_id
        return fetch("https://second-opinion-gy3d.onrender.com/api/v1/analysis/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                document_id: documentId,
                provider_id: providerId
            })
        });
    })
    .then(analyzeRes => analyzeRes.json())
    .then(data => {
        // Broadcast to sidebar
        chrome.runtime.sendMessage({
            type: "ANALYSIS_COMPLETE",
            data: data
        });

        // Respond to content script (popup)
        if (sendResponse) {
            sendResponse({ 
                status: "success", 
                risk_level: data.analysis?.risk_level || "unknown",
                score: data.policy_score?.overall_score || 0
            });
        }
    })
    .catch(err => {
        console.error("Analysis Error:", err);
        if (sendResponse) {
            sendResponse({ status: "error", risk_level: "unknown", score: 0 });
        }
    });
}

chrome.runtime.onMessage.addListener((request, _sender, sendResponse) => {
    if (request.type === 'ANALYZE_PAGE') {
        runBackendPipeline(request.payload, request.hostname || "", sendResponse);
        return true; // Keep message channel open
    }
    
    if (request.type === 'ANALYZE_PDF') {
        const id = Date.now().toString();
        pendingResponses[id] = sendResponse;
        
        // Tell sidebar to extract the PDF text
        chrome.runtime.sendMessage({
            type: "EXTRACT_PDF_TEXT",
            url: request.url,
            hostname: request.hostname,
            originalSenderId: id
        });
        
        return true; // Keep message channel open
    }
    
    if (request.type === 'PDF_EXTRACTED') {
        const respond = pendingResponses[request.originalSenderId];
        if (respond) delete pendingResponses[request.originalSenderId];
        runBackendPipeline(request.payload, request.hostname || "", respond);
    }
    
    if (request.type === 'PDF_EXTRACTED_FAILED') {
        const respond = pendingResponses[request.originalSenderId];
        if (respond) {
            delete pendingResponses[request.originalSenderId];
            respond({ status: "error", risk_level: "unknown", score: 0 });
        }
    }
});
