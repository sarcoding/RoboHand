function onSelectionHandler(selectionEvent){
    const value  =  selectionEvent.value;
    window.location.href = value;
    // const buttonsContainer = document.getElementById('manualButtons');
    // if (value === 'manual') {
    //     buttonsContainer.classList.remove('hidden');
    //     handImage.src = "static/img/hand.png";
    // } else {
    //     buttonsContainer.classList.add('hidden');
    //     handImage.src = "static/img/ro_without_back.png";
    //     window.location.href = value;
    // }
}
// function toggleColor(button, storageKey) {
//     var currentColor = localStorage.getItem(storageKey);

//     if (currentColor === 'red') {
//         button.style.backgroundColor = 'green';
//         localStorage.setItem(storageKey, 'green');
//     } else {
//         button.style.backgroundColor = 'red';
//         localStorage.setItem(storageKey, 'red');
//     }
// }

// // Restore color from localStorage on page load
// document.addEventListener('DOMContentLoaded', function() {
//     var buttons = document.querySelectorAll('.button');

//     buttons.forEach(function(button) {
//         var storageKey = button.textContent.trim().toLowerCase();
//         var storedColor = localStorage.getItem(storageKey);

//         if (storedColor === 'red') {
//             button.style.backgroundColor = 'red';
//         } else {
//             button.style.backgroundColor = 'green';
//         }
//     });
// });

document.getElementById('themeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    this.textContent = document.body.classList.contains('dark-mode') ? '🌙' : '☀️';
});

// document.querySelectorAll('.finger-button').forEach(button => {
//     button.addEventListener('click', function(event) {
//         event.preventDefault();
//         const value = this.getAttribute('data-value');
//         document.getElementById('button_value').value = value;
//         document.getElementById('manualButtons').submit();
//     });
// });