function toggleTheme() {
    const body = document.body;
    const btn = document.getElementById('themeBtn');

    if (body.getAttribute('data-theme') === 'dark') {
        body.removeAttribute('data-theme');
        btn.innerHTML = '🌙';
        localStorage.setItem('theme', 'light');
    } else {
        body.setAttribute('data-theme', 'dark');
        btn.innerHTML = '☀️';
        localStorage.setItem('theme', 'dark');
    }
}
window.onload = function() {
    const savedTheme = localStorage.getItem('theme');
    const btn = document.getElementById('themeBtn');

    if (savedTheme === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
        btn.innerHTML = '☀️';
    }
};
