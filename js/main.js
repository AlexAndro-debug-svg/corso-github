/* =====================================================
   alessandrosimone.it — Interazioni del sito
   ===================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* --- Menu mobile (hamburger) --- */
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.querySelector('.nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
    // chiudi il menu quando si clicca un link
    menu.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => menu.classList.remove('open'))
    );
  }

  /* --- Evidenzia la voce di menu della pagina corrente --- */
  const here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-menu a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === here || (here === '' && href === 'index.html')) {
      if (!a.classList.contains('btn')) a.classList.add('active');
    }
  });

  /* --- Filtri esercizi (pagina esercizi.html) --- */
  const chips = document.querySelectorAll('.filters .chip');
  const items = document.querySelectorAll('.ex-list .ex-item');
  if (chips.length && items.length) {
    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const filter = chip.dataset.filter;
        items.forEach(item => {
          const match = filter === 'tutti' || item.dataset.cat === filter;
          item.classList.toggle('hidden', !match);
        });
      });
    });
  }

  /* --- Menu a tendina "Corsi" --- */
  const corsi = document.querySelector('.nav-corsi');
  const corsiToggle = document.querySelector('.nav-corsi-toggle');
  if (corsi && corsiToggle) {
    corsiToggle.addEventListener('click', (e) => {
      e.preventDefault();
      corsi.classList.toggle('open');
    });
    document.addEventListener('click', (e) => {
      if (!corsi.contains(e.target)) corsi.classList.remove('open');
    });
  }

  /* --- Barra corsi: evidenzia e porta in vista il corso attivo --- */
  const courseNav = document.querySelector('.course-nav-inner');
  if (courseNav) {
    const page = location.pathname.split('/').pop() || 'index.html';
    let active = courseNav.querySelector('a.active');
    // Se nessun link è già marcato active, ricavalo dalla pagina corrente
    if (!active) {
      courseNav.querySelectorAll('a').forEach(a => {
        if (a.getAttribute('href') === page) { a.classList.add('active'); active = a; }
      });
    }
    // Porta il corso attivo al centro della barra scorrevole orizzontale.
    // Uso i rect (non offsetLeft) per essere indipendente dall'offsetParent
    // e non provocare scroll verticale della pagina.
    if (active) {
      const centra = () => {
        const navRect = courseNav.getBoundingClientRect();
        const aRect = active.getBoundingClientRect();
        const posInNav = (aRect.left - navRect.left) + courseNav.scrollLeft;
        const target = posInNav - (courseNav.clientWidth / 2) + (aRect.width / 2);
        courseNav.scrollLeft = Math.max(0, target);
      };
      centra();
      // i font web possono cambiare le larghezze dopo il load: ricentra
      window.addEventListener('load', centra);
    }
  }

  /* --- Anno corrente nel footer --- */
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

});
