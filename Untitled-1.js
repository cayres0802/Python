// Get the current year for the copyright notice
const currentYear = new Date().getFullYear();

// Set the copyright notice in the footer
document.querySelector('footer p').innerHTML = `Copyright © ${currentYear} Fisioella. Todos os direitos reservados.`;

// Add a scroll to top button
const scrollToTopButton = document.createElement('button');
scrollToTopButton.textContent = 'Voltar ao topo';
scrollToTopButton.style.position = 'fixed';
scrollToTopButton.style.bottom = '2rem';
scrollToTopButton.style.right = '2rem';
scrollToTopButton.style.backgroundColor = '#0066cc';
scrollToTopButton.style.color = '#fff';
scrollToTopButton.style.padding = '0.5rem 1rem';
scrollToTopButton.style.border = 'none';
scrollToTopButton.style.borderRadius = '0.5rem';
scrollToTopButton.style.cursor = 'pointer';
scrollToTopButton.style.display = 'none';
document.body.appendChild(scrollToTopButton);

window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
        scrollToTopButton.style.display = 'block';
    } else {
        scrollToTopButton.style.display = 'none';
    }
});

scrollToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});