// color-modes.js
(() => {
  'use strict';

  const storedTheme = localStorage.getItem('theme');

  const getPreferredTheme = () => {
    if (storedTheme) {
      return storedTheme;
    }

    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const setTheme = (theme) => {
    if (theme === 'auto') {
      document.documentElement.removeAttribute('data-bs-theme');
    } else {
      document.documentElement.setAttribute('data-bs-theme', theme);
    }
  };

  setTheme(getPreferredTheme());

  window.addEventListener('DOMContentLoaded', () => {
    const themeButtons = document.querySelectorAll('[data-bs-theme-value]');

    themeButtons.forEach(button => {
      button.addEventListener('click', () => {
        const theme = button.getAttribute('data-bs-theme-value');
        localStorage.setItem('theme', theme);
        setTheme(theme);
      });
    });
  });
})();
