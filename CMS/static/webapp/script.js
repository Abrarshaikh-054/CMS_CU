// Sabour College Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Sticky Navbar Functionality
    const navbar = document.getElementById('mainNavbar');
    const body = document.body;
    const collegeHeader = document.querySelector('.college-header');
    let headerBottom = 0;

    function updateHeaderBottom() {
        if (collegeHeader) {
            const rect = collegeHeader.getBoundingClientRect();
            headerBottom = rect.bottom + window.scrollY;
        } else {
            headerBottom = 0;
        }
    }

    // Update headerBottom on load and resize
    updateHeaderBottom();
    window.addEventListener('resize', updateHeaderBottom);

    function handleScroll() {
        if (window.scrollY >= headerBottom) {
            navbar.classList.add('sticky');
            body.classList.add('navbar-sticky');
        } else {
            navbar.classList.remove('sticky');
            body.classList.remove('navbar-sticky');
        }
    }
    
    // Throttle scroll events for better performance
    let ticking = false;
    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(handleScroll);
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', function() {
        requestTick();
        ticking = false;
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
    
    // Auto-close mobile navbar when clicking on links
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse && navbarCollapse.classList.contains('show')) {
                const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                bsCollapse.hide();
            }
        });
    });
    
    // Enhanced dropdown hover effects
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    
    dropdownToggles.forEach(toggle => {
        const dropdown = toggle.parentElement;
        
        dropdown.addEventListener('mouseenter', function() {
            if (window.innerWidth >= 992) {
                const dropdownMenu = this.querySelector('.dropdown-menu');
                if (dropdownMenu) {
                    this.classList.add('show');
                    dropdownMenu.classList.add('show');
                    toggle.setAttribute('aria-expanded', 'true');
                }
            }
        });
        
        dropdown.addEventListener('mouseleave', function() {
            if (window.innerWidth >= 992) {
                const dropdownMenu = this.querySelector('.dropdown-menu');
                if (dropdownMenu) {
                    this.classList.remove('show');
                    dropdownMenu.classList.remove('show');
                    toggle.setAttribute('aria-expanded', 'false');
                }
            }
        });
    });
    
    // Carousel auto-play with pause on hover
    const carousel = document.querySelector('#heroCarousel');
    if (carousel) {
        const bsCarousel = new bootstrap.Carousel(carousel, { interval: 5000, wrap: true });
        carousel.addEventListener('mouseenter', () => { bsCarousel.pause(); });
        carousel.addEventListener('mouseleave', () => { bsCarousel.cycle(); });
    }
    
    // Animate elements on scroll
    const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('fade-in'); } });
    }, observerOptions);
    document.querySelectorAll('.quick-link-card').forEach(card => { observer.observe(card); });
    
    // News item click tracking
    document.querySelectorAll('.news-link').forEach(link => {
        link.addEventListener('click', function() { console.log('News item clicked:', this.textContent.trim()); });
    });
    
    // Login dropdown enhancement
    const loginDropdown = document.querySelector('.login-dropdown');
    if (loginDropdown) {
        loginDropdown.addEventListener('click', function() { console.log('Login dropdown clicked'); });
    }
    
    // Keyboard navigation enhancement
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
                const dropdown = menu.parentElement;
                dropdown.classList.remove('show');
                menu.classList.remove('show');
                const toggle = dropdown.querySelector('.dropdown-toggle');
                if (toggle) { toggle.setAttribute('aria-expanded', 'false'); }
            });
        }
    });
    
    // Responsive image loading
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    images.forEach(img => imageObserver.observe(img));
    
    // Performance optimization: Preload critical resources
    const preloadLinks = [
        'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css'
    ];
    preloadLinks.forEach(href => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'style';
        link.href = href;
        document.head.appendChild(link);
    });

    console.log('%c🎓 Welcome to Sabour College Website!', 'color: #dc3545; font-size: 16px; font-weight: bold;');
    console.log('%cBuilt with Bootstrap 5 and modern web technologies', 'color: #002147; font-size: 12px;');
});

// Utility functions
const utils = {
    debounce: function(func, wait, immediate) {
        let timeout;
        return function executedFunction() {
            const context = this;
            const args = arguments;
            const later = function() {
                timeout = null;
                if (!immediate) func.apply(context, args);
            };
            const callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func.apply(context, args);
        };
    },
    scrollTo: function(element, duration = 1000) {
        const targetPosition = element.offsetTop - 80;
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        let startTime = null;
        function animation(currentTime) {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = ease(timeElapsed, startPosition, distance, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(animation);
        }
        function ease(t, b, c, d) {
            t /= d / 2;
            if (t < 1) return c / 2 * t * t + b;
            t--;
            return -c / 2 * (t * (t - 2) - 1) + b;
        }
        requestAnimationFrame(animation);
    }
};

window.SabourCollegeUtils = utils;
