/**
 * Mock Interview Platform - Main JavaScript
 * Handles global utilities, animations, and shared logic
 */

const API_BASE_URL = ''; // Relative path for deployment

// ==================== AUTH INTERCEPTOR ====================
const originalFetch = window.fetch;
window.fetch = async function (url, options = {}) {
    // Add Authorization header if token exists
    const token = localStorage.getItem('auth_token');
    if (token) {
        options.headers = {
            ...options.headers,
            'Authorization': `Bearer ${token}`
        };
    }

    // Handle JSON content type default
    if (options.body && typeof options.body === 'string' && !options.headers['Content-Type']) {
        // Keep existing if any, but default usually handled by caller.
        // Let's not force it unless needed.
    }

    const response = await originalFetch(url, options);

    // Handle 401 Unauthorized or 403 Forbidden (Global logout)
    if ((response.status === 401 || response.status === 403) && !url.includes('/auth/login')) {
        console.warn('Unauthorized: Redirecting to login');
        logout();
    }

    return response;
};

// ==================== GLOBAL UTILITIES ====================

/**
 * Show a feedback message to the user
 * @param {string} text - The message text
 * @param {string} type - 'success', 'error', or 'info'
 */
function showMessage(text, type = 'info') {
    const messageDiv = document.getElementById('message');
    if (messageDiv) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
        messageDiv.style.display = 'block';

        // Add animation
        messageDiv.classList.remove('animate-slide-down');
        void messageDiv.offsetWidth; // Trigger reflow
        messageDiv.classList.add('animate-slide-down');

        // Auto-hide after 5 seconds
        if (window.messageTimeout) clearTimeout(window.messageTimeout);
        window.messageTimeout = setTimeout(() => {
            messageDiv.style.opacity = '0';
            setTimeout(() => {
                messageDiv.style.display = 'none';
                messageDiv.style.opacity = '1';
            }, 300);
        }, 5000);
    }
}

/**
 * Shake an element to indicate error
 * @param {string} elementId 
 */
function shakeElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.classList.remove('animate-shake');
        void element.offsetWidth; // Trigger reflow
        element.classList.add('animate-shake');
    }
}

// ==================== AUTHENTICATION ====================

function checkAuth() {
    const userId = localStorage.getItem('user_id');
    if (!userId && !window.location.pathname.endsWith('index.html')) {
        window.location.href = 'index.html';
    }
    return userId;
}

function logout() {
    if (confirm('Are you sure you want to logout?')) {
        localStorage.clear(); // Clears everything including auth_token
        window.location.href = 'index.html';
    }
}

// ==================== ANIMATIONS & INTERACTIONS ====================

// Initialize Intersection Observer for scroll animations
document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once visible
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all elements with .animate-on-scroll class
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });

    // Initialize Ripple Effect globally
    initRippleEffect();
});

/**
 * Initialize Ripple Effect for all buttons with .ripple-container class
 */
function initRippleEffect() {
    document.addEventListener('click', (e) => {
        const target = e.target.closest('.ripple-container');
        if (target) {
            createRipple(e, target);
        }
    });
}

function createRipple(event, button) {
    const ripple = document.createElement('span');
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;

    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.classList.add('ripple');

    // Remove existing ripples to prevent buildup
    const existing = button.getElementsByClassName('ripple');
    if (existing.length > 0) {
        existing[0].remove();
    }

    button.appendChild(ripple);

    setTimeout(() => {
        ripple.remove();
    }, 600);
}

// ==================== FORMATTING ====================

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// ==================== EXPORTS ====================
// Make functions available globally
window.showMessage = showMessage;
window.shakeElement = shakeElement;
window.checkAuth = checkAuth;
window.logout = logout;
window.formatDate = formatDate;
