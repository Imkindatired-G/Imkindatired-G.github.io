// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', () => {
  // Fade-in animation for main content or hero section
  const main = document.querySelector('.content, .hero');
  if (main) {
    main.style.opacity = 0;
    main.style.transition = 'opacity 0.8s';
    setTimeout(() => {
      main.style.opacity = 1;
    }, 100);
  }

  // Smooth scroll for anchor links (if any)
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href').slice(1);
      const target = document.getElementById(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Header hide-on-scroll
  let lastScrollY = window.scrollY;
  const header = document.querySelector('header');
  let ticking = false;

  function handleHeaderScroll() {
    const currentScrollY = window.scrollY;
    if (currentScrollY > lastScrollY && currentScrollY > 50) {
      header.classList.add('header-hidden');
    } else {
      header.classList.remove('header-hidden');
    }
    lastScrollY = currentScrollY;
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(handleHeaderScroll);
      ticking = true;
    }
  });
});