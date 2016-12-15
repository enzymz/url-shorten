funtion copyToClipboard(s) {
    if(window.clipboardData && clipboardData.setData) {
        clipboardData.setData('text', s);
    }
}
