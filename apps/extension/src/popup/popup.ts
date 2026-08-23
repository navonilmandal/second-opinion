document.getElementById('open-sidebar')?.addEventListener('click', () => {
    chrome.windows.getCurrent({populate: true}, (window) => {
        if(window.id !== undefined) {
            chrome.sidePanel.open({windowId: window.id});
        }
    });
});
