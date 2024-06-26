document.getElementById('themeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    this.textContent = document.body.classList.contains('dark-mode') ? '🌙' : '☀️';
});

function onSelectionHandler(selectionEvent){
    const value  =  selectionEvent.value;
    window.location.href = value;
}