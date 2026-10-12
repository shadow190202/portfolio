// ==========================================================================
// Portfolio JavaScript Interactions
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initContactForm();
  initScrollSpy();
  initCardAmbientGlow();
});

/**
 * Mobile Drawer Menu Toggle
 */
function initMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const menuLinks = document.querySelectorAll('.mobile-nav-link');

  if (!menuBtn || !mobileMenu) return;

  menuBtn.addEventListener('click', () => {
    const isExpanded = menuBtn.getAttribute('aria-expanded') === 'true';
    menuBtn.setAttribute('aria-expanded', !isExpanded);
    mobileMenu.classList.toggle('hidden');
  });

  menuLinks.forEach((link) => {
    link.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
      menuBtn.setAttribute('aria-expanded', 'false');
    });
  });
}

/**
 * Contact Form Submission with AJAX & Feedback
 */
function initContactForm() {
  const form = document.getElementById('contact-form');
  const alertContainer = document.getElementById('contact-alert');
  const submitBtn = document.getElementById('contact-submit-btn');

  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const originalBtnText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
      Sending Message...
    `;

    // Clear previous alerts
    if (alertContainer) {
      alertContainer.innerHTML = '';
      alertContainer.classList.add('hidden');
    }

    try {
      const formData = new FormData(form);
      const response = await fetch('/api/contact', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (response.ok && data.success) {
        form.reset();
        showAlert(
          alertContainer,
          'success',
          data.message || 'Thank you! Your message has been sent successfully.'
        );
      } else {
        showAlert(
          alertContainer,
          'error',
          data.error || 'Failed to send message. Please verify your fields and try again.'
        );
      }
    } catch (err) {
      console.error('Contact submit error:', err);
      showAlert(
        alertContainer,
        'error',
        'A network error occurred. Please try again or reach out directly via email.'
      );
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalBtnText;
    }
  });
}

function showAlert(container, type, message) {
  if (!container) return;

  const isSuccess = type === 'success';
  const bgColor = isSuccess ? 'bg-emerald-950/80' : 'bg-red-950/80';
  const borderColor = isSuccess ? 'border-emerald-500/40' : 'border-red-500/40';
  const textColor = isSuccess ? 'text-emerald-300' : 'text-red-300';
  const icon = isSuccess
    ? `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />`
    : `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />`;

  container.className = `p-4 mb-6 rounded-xl border ${bgColor} ${borderColor} ${textColor} text-sm flex items-start gap-3 transition-all duration-300`;
  container.innerHTML = `
    <svg class="w-5 h-5 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      ${icon}
    </svg>
    <div>${message}</div>
  `;
  container.classList.remove('hidden');

  container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * ScrollSpy for Active Navigation Link Highlighting
 */
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.desktop-nav-link');

  if (!sections.length || !navLinks.length) return;

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPosition = window.pageYOffset + 120;

    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach((link) => {
      link.classList.remove('text-cyan-400', 'font-semibold');
      link.classList.add('text-slate-300');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('text-cyan-400', 'font-semibold');
        link.classList.remove('text-slate-300');
      }
    });
  });
}

/**
 * Subtle Ambient Mouse Spotlight on Interactive Panels
 */
function initCardAmbientGlow() {
  const cards = document.querySelectorAll('.card-interactive');

  cards.forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });
}
