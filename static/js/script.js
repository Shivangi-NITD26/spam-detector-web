function toggleTheme() {
    const body = document.body;
    const btn = document.getElementById('themeBtn');

    if (body.getAttribute('data-theme') === 'dark') {
        body.removeAttribute('data-theme');
        btn.innerHTML = '🌙'; // Switch to moon icon
        localStorage.setItem('theme', 'light'); // Save preference
    } else {
        body.setAttribute('data-theme', 'dark');
        btn.innerHTML = '☀️'; // Switch to sun icon
        localStorage.setItem('theme', 'dark'); // Save preference
    }
}

// Check local storage on page load so the theme stays the same after hitting "Analyze Text"
window.onload = function() {
    const savedTheme = localStorage.getItem('theme');
    const btn = document.getElementById('themeBtn');

    if (savedTheme === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
        btn.innerHTML = '☀️';
    }
};