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

  /* --- Anno corrente nel footer --- */
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

});
