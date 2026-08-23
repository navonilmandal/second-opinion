import * as pdfjsLib from 'pdfjs-dist';
// Set the workerSrc to the local bundled worker to comply with MV3 CSP
pdfjsLib.GlobalWorkerOptions.workerSrc = chrome.runtime.getURL('pdf.worker.min.mjs');

chrome.runtime.onMessage.addListener((message) => {
    const scoreContainer = document.getElementById("score-container");
    const loadingContainer = document.getElementById("loading-container");

    const analysisPlaceholder = document.getElementById("analysis-placeholder");
    const analysisContent = document.getElementById("analysis-content");

    if (message.type === "ANALYSIS_STARTED") {
        if (scoreContainer) scoreContainer.classList.add("hidden");
        if (loadingContainer) loadingContainer.classList.remove("hidden");
        if (analysisPlaceholder) {
            analysisPlaceholder.classList.remove("hidden");
            const p = analysisPlaceholder.querySelector('p');
            if (p) p.innerText = "Extracting text and uploading to AI backend...";
        }
        if (analysisContent) analysisContent.classList.add("hidden");
    }
    else if (message.type === "LOCAL_PDF_DETECTED") {
        if (scoreContainer) scoreContainer.classList.add("hidden");
        if (loadingContainer) loadingContainer.classList.add("hidden");
        if (analysisContent) analysisContent.classList.add("hidden");
        if (analysisPlaceholder) analysisPlaceholder.classList.add("hidden");
        
        const localUpload = document.getElementById("local-pdf-upload");
        if (localUpload) localUpload.classList.remove("hidden");
    }
    else if (message.type === "EXTRACT_PDF_TEXT") {
        if (analysisPlaceholder) {
            analysisPlaceholder.classList.remove("hidden");
            const p = analysisPlaceholder.querySelector('p');
            if (p) p.innerText = "Extracting text from PDF (Local Browser)...";
        }
        
        // Run PDF extraction locally
        (async () => {
            try {
                // Decode Base64 string back into raw bytes (Uint8Array)
                const binaryString = window.atob(message.payload);
                const bytes = new Uint8Array(binaryString.length);
                for (let i = 0; i < binaryString.length; i++) {
                    bytes[i] = binaryString.charCodeAt(i);
                }

                const pdf = await pdfjsLib.getDocument({ data: bytes }).promise;
                let fullText = "";
                for (let i = 1; i <= pdf.numPages; i++) {
                    chrome.runtime.sendMessage({ type: "ANALYSIS_STATUS", message: `Extracting PDF Page ${i} of ${pdf.numPages}...` });
                    const page = await pdf.getPage(i);
                    const textContent = await page.getTextContent();
                    const pageText = textContent.items.map((item: any) => item.str).join(" ");
                    fullText += pageText + "\n\n";
                }
                
                // Compress whitespace
                fullText = fullText.replace(/[ \t]+/g, ' ');
                fullText = fullText.replace(/\n{3,}/g, '\n\n');
                fullText = fullText.trim();
                
                // Send back to service worker to continue standard pipeline
                chrome.runtime.sendMessage({ type: "PDF_EXTRACTED", payload: fullText, hostname: message.hostname, originalSenderId: message.originalSenderId });
                
            } catch (err: any) {
                console.error("PDF Extraction Error:", err);
                chrome.runtime.sendMessage({ type: "ANALYSIS_STATUS", message: "Failed to read PDF: " + err.message });
                // Tell service worker it failed
                chrome.runtime.sendMessage({ type: "PDF_EXTRACTED_FAILED", originalSenderId: message.originalSenderId });
            }
        })();
    }
    else if (message.type === "ANALYSIS_STATUS") {
        if (analysisPlaceholder) {
            const p = analysisPlaceholder.querySelector('p');
            if (p) p.innerText = message.message;
        }
    }
    else if (message.type === "ANALYSIS_COMPLETE" && message.data) {
        if (scoreContainer) scoreContainer.classList.remove("hidden");
        if (loadingContainer) loadingContainer.classList.add("hidden");

        const data = message.data;
        const score = data.policy_score?.overall_score || 0;
        const verdict = data.policy_score?.verdict || "UNKNOWN";
        const trustScore = data.policy_score?.trust_score || 0;
        const transparencyScore = data.policy_score?.transparency_score || 0;
        const trapCount = data.policy_score?.trap_count || 0;
        const claimSettlement = data.policy_score?.claim_settlement_pct || 0;

        const summary = data.analysis?.summary || "No summary provided.";
        const whyFlagged = data.analysis?.why_flagged || "No risks flagged.";
        const recommendation = data.analysis?.recommendation || "No recommendation provided.";

        const scoreCircle = document.getElementById("score-circle");
        const scoreEl = document.getElementById("score-text");
        const verdictEl = document.getElementById("verdict-text");

        let color = "#ef4444"; // Red
        if (score >= 65) color = "#10b981"; // Green
        else if (score >= 50) color = "#f59e0b"; // Yellow

        if (scoreCircle) {
            scoreCircle.setAttribute("stroke-dasharray", `${score}, 100`);
            scoreCircle.setAttribute("stroke", color);
        }

        if (scoreEl) {
            scoreEl.textContent = score.toString();
        }

        if (verdictEl) {
            verdictEl.innerText = verdict;
            verdictEl.style.color = color;
            verdictEl.style.background = color + "20"; // 20% opacity background
        }

        if (analysisPlaceholder) analysisPlaceholder.classList.add("hidden");
        if (analysisContent) analysisContent.classList.remove("hidden");

        const sumEl = document.getElementById("summary-text");
        const goodEl = document.getElementById("good-text");
        const badEl = document.getElementById("bad-text");
        const factorEl = document.getElementById("factors-text");
        const recEl = document.getElementById("recommendation-text");

        const formatText = (text: string) => text.split('\n').filter(p => p.trim()).map(p => `<p>${p}</p>`).join('');

        if (sumEl) sumEl.innerHTML = formatText(summary);
        // API doesn't explicitly return 'what's good' separately right now, so we use summary if good or a generic line.
        if (goodEl) goodEl.innerHTML = formatText(score >= 60 ? "The core policy covers standard requirements well based on the analysis." : "Few explicitly positive features highlighted over the risks.");
        if (badEl) badEl.innerHTML = formatText(whyFlagged);

        if (factorEl) {
            factorEl.innerHTML = `<p><strong>Trust Score:</strong> ${trustScore}/100</p><p><strong>Transparency Score:</strong> ${transparencyScore}/100</p><p><strong>Hidden Traps Found:</strong> ${trapCount}</p><p><strong>Claim Settlement (IRDAI):</strong> ${claimSettlement}%</p>`;
        }

        if (recEl) recEl.innerHTML = formatText(recommendation);
    }
});

// Setup file upload listener for local PDFs
const fileInput = document.getElementById("pdf-upload-input") as HTMLInputElement;
if (fileInput) {
    fileInput.addEventListener('change', (e: Event) => {
        const target = e.target as HTMLInputElement;
        if (!target.files || target.files.length === 0) return;
        
        const file = target.files[0];
        const reader = new FileReader();
        
        const localUpload = document.getElementById("local-pdf-upload");
        if (localUpload) localUpload.classList.add("hidden");
        
        const analysisPlaceholder = document.getElementById("analysis-placeholder");
        if (analysisPlaceholder) {
            analysisPlaceholder.classList.remove("hidden");
            const p = analysisPlaceholder.querySelector('p');
            if (p) p.innerText = "Extracting text from uploaded PDF...";
        }

        reader.onload = async (event) => {
            const arrayBuffer = event.target?.result as ArrayBuffer;
            if (!arrayBuffer) return;
            
            try {
                const pdf = await pdfjsLib.getDocument({ data: new Uint8Array(arrayBuffer) }).promise;
                let fullText = "";
                for (let i = 1; i <= pdf.numPages; i++) {
                    chrome.runtime.sendMessage({ type: "ANALYSIS_STATUS", message: `Extracting PDF Page ${i} of ${pdf.numPages}...` });
                    const page = await pdf.getPage(i);
                    const textContent = await page.getTextContent();
                    const pageText = textContent.items.map((item: any) => item.str).join(" ");
                    fullText += pageText + "\n\n";
                }
                
                // Compress whitespace
                fullText = fullText.replace(/[ \t]+/g, ' ');
                fullText = fullText.replace(/\n{3,}/g, '\n\n');
                fullText = fullText.trim();
                
                // Send back to service worker to continue standard pipeline
                // Since this was initiated locally, we don't have a pending sendResponse, 
                // so we just start the pipeline in the background directly.
                chrome.runtime.sendMessage({ type: "ANALYZE_PAGE", payload: fullText, hostname: "local_pdf" });
                
            } catch (err: any) {
                console.error("PDF Extraction Error:", err);
                chrome.runtime.sendMessage({ type: "ANALYSIS_STATUS", message: "Failed to read PDF: " + err.message });
            }
        };
        
        reader.readAsArrayBuffer(file);
    });
}

// UI Toggles for Providers View
const btnShowProviders = document.getElementById('btn-show-providers');
const btnBackProviders = document.getElementById('btn-back-providers');
const btnHome = document.getElementById('btn-home');
const mainView = document.getElementById('main-view');
const providersView = document.getElementById('providers-view');
const providersList = document.getElementById('providers-list');

const companies = [
    "Tata AIG General Insurance",
    "HDFC Ergo General Insurance",
    "ICICI Lombard General Insurance",
    "New India Assurance",
    "United India Insurance",
    "National Insurance",
    "Star Health and Allied Insurance",
    "Bajaj Allianz General Insurance",
    "SBI General Insurance",
    "Care Health Insurance"
];

if (providersList) {
    companies.forEach(company => {
        const div = document.createElement('div');
        div.className = 'provider-item';
        div.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px; color: var(--risk-low);"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> ${company}`;
        providersList.appendChild(div);
    });
}

const showProviders = () => {
    if (mainView) mainView.classList.add('hidden');
    if (providersView) providersView.classList.remove('hidden');
};

const hideProviders = () => {
    if (mainView) mainView.classList.remove('hidden');
    if (providersView) providersView.classList.add('hidden');
};

if (btnShowProviders) btnShowProviders.addEventListener('click', showProviders);
if (btnBackProviders) btnBackProviders.addEventListener('click', hideProviders);
if (btnHome) btnHome.addEventListener('click', hideProviders);
