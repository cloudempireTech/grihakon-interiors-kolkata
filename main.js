// Grihakon Interior Designer - Main Interactive Script
document.addEventListener('DOMContentLoaded', () => {
  // 1. Dynamic Typewriter Animation
  const typewriterEl = document.querySelector('.typewriter-text');
  if (typewriterEl) {
    const words = [
      'Bespoke Home Transformations',
      'Turnkey Interior Architecture',
      'Ergonomic Modular Kitchens',
      'Luxury Master Living Lounges',
      'Heritage Renovation & Remodeling'
    ];
    let wordIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let typingSpeed = 90;

    function type() {
      const currentWord = words[wordIdx];
      if (isDeleting) {
        typewriterEl.textContent = currentWord.substring(0, charIdx - 1);
        charIdx--;
        typingSpeed = 45;
      } else {
        typewriterEl.textContent = currentWord.substring(0, charIdx + 1);
        charIdx++;
        typingSpeed = 90;
      }

      if (!isDeleting && charIdx === currentWord.length) {
        isDeleting = true;
        typingSpeed = 2000; // Pause at end of word
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        wordIdx = (wordIdx + 1) % words.length;
        typingSpeed = 400; // Pause before new word
      }

      setTimeout(type, typingSpeed);
    }
    type();
  }

  // 2. Telemetry Animated Counters
  const telemetryVals = document.querySelectorAll('.telemetry-val');
  if (telemetryVals.length > 0) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-target') || el.textContent.replace(/\D/g, ''), 10);
          const suffix = el.getAttribute('data-suffix') || '';
          if (!isNaN(target)) {
            let start = 0;
            const duration = 1800;
            const step = Math.max(1, Math.floor(target / (duration / 25)));
            const timer = setInterval(() => {
              start += step;
              if (start >= target) {
                el.textContent = target + suffix;
                clearInterval(timer);
              } else {
                el.textContent = start + suffix;
              }
            }, 25);
          }
          obs.unobserve(el);
        }
      });
    }, { threshold: 0.3 });

    telemetryVals.forEach(val => observer.observe(val));
  }

  // 3. Interactive Scope & 3D Intake Estimator Widget
  const homeTypeSel = document.getElementById('estHomeType');
  const scopeSel = document.getElementById('estScope');
  const specSel = document.getElementById('estSpec');
  const estTitle = document.getElementById('estTitle');
  const estTimeline = document.getElementById('estTimeline');
  const estWaBtn = document.getElementById('estWaBtn');

  function updateEstimator() {
    if (!homeTypeSel || !scopeSel || !specSel) return;
    const home = homeTypeSel.value;
    const scope = scopeSel.value;
    const spec = specSel.value;

    let titleText = `${home} — ${scope}`;
    let timelineText = 'Estimated Handover: 45 Days | Plywood: IS:710 Marine Grade BWP';

    if (scope === 'Full Turnkey Interior') {
      if (home === '2BHK Apartment') timelineText = 'Estimated Handover: 40–45 Days | 3D VR Renders + Hafele Modular Kitchen + Living Lounges';
      else if (home === '3BHK Apartment') timelineText = 'Estimated Handover: 45–55 Days | 3D VR Walkthrough + Acrylic Kitchen + Dual Master Suites';
      else if (home === 'Duplex / Bungalow') timelineText = 'Estimated Handover: 60–75 Days | Architectural Spatial Restructure + Custom Lounges';
      else timelineText = 'Estimated Handover: 35–45 Days | Acoustic Ceiling + Glass Partitions + Ergonomic Workstations';
    } else if (scope === 'Modular Kitchen & Dining') {
      timelineText = 'Estimated Handover: 25–30 Days | Blum Soft-Close Tandem Boxes + Quartz Countertops';
    } else if (scope === 'Renovation & Structural Restructure') {
      timelineText = 'Estimated Handover: 35–45 Days | Civil Waterproofing + Italian Tile Laying + Concealed Plumbing';
    }

    if (spec === 'Ultra-Luxury Italian & Veneer') {
      timelineText += ' | Natural Teak Veneer & Lacquered Glass Accents';
    } else if (spec === 'Elite Marine Plywood IS:710') {
      timelineText += ' | 100% Calibrated Marine Plywood & Matte Laminate';
    }

    if (estTitle) estTitle.textContent = titleText;
    if (estTimeline) estTimeline.textContent = timelineText;

    if (estWaBtn) {
      const msg = encodeURIComponent(
        `Hello Grihakon Interior Team! I would like to schedule a 3D architectural consultation for my property:\n\n• Home Type: ${home}\n• Scope: ${scope}\n• Finish Specification: ${spec}\n• Location: Bonhooghly / Baranagar / Kolkata\n\nPlease share your portfolio and available consultation slots!`
      );
      estWaBtn.href = `https://wa.me/919163424988?text=${msg}`;
    }
  }

  if (homeTypeSel && scopeSel && specSel) {
    homeTypeSel.addEventListener('change', updateEstimator);
    scopeSel.addEventListener('change', updateEstimator);
    specSel.addEventListener('change', updateEstimator);
    updateEstimator();
  }

  // 4. Portfolio Filter Rail
  const filterBtns = document.querySelectorAll('.filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');
  if (filterBtns.length > 0 && galleryItems.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.getAttribute('data-filter');

        galleryItems.forEach(item => {
          if (filter === 'all' || item.getAttribute('data-category') === filter) {
            item.style.display = 'block';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // 5. Mobile Navigation Drawer Toggle
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');
  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      drawer.classList.toggle('open');
    });

    document.addEventListener('click', (e) => {
      if (drawer.classList.contains('open') && !drawer.contains(e.target) && !toggleBtn.contains(e.target)) {
        drawer.classList.remove('open');
      }
    });
  }

  // 6. Contact Form WhatsApp Submission Bridge
  const contactForm = document.getElementById('consultationForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('formName')?.value || 'Prospective Homeowner';
      const phone = document.getElementById('formPhone')?.value || '';
      const locality = document.getElementById('formLocality')?.value || 'Kolkata';
      const property = document.getElementById('formProperty')?.value || 'Apartment';
      const notes = document.getElementById('formNotes')?.value || 'Consultation request';

      const waText = encodeURIComponent(
        `New Consultation Request - Grihakon Interiors:\n\n• Name: ${name}\n• Contact: ${phone}\n• Locality: ${locality}\n• Property Scope: ${property}\n• Requirements: ${notes}`
      );
      window.open(`https://wa.me/919163424988?text=${waText}`, '_blank');
    });
  }
});
