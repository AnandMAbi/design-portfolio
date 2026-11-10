/* Anand M A — portfolio interactions */
(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;

  /* header state + scroll progress */
  const head = document.querySelector('.site-head');
  const bar = document.querySelector('.progress');
  const onScroll = () => {
    const y = window.scrollY;
    if (head) head.classList.toggle('is-scrolled', y > 8);
    if (bar) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = max > 0 ? `${Math.min(1, y / max) * 100}%` : '0%';
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* reveal on scroll */
  const targets = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && !reduced) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach((t) => io.observe(t));
  } else {
    targets.forEach((t) => t.classList.add('is-in'));
  }

  /* duplicate marquee content so the loop is seamless */
  document.querySelectorAll('.marquee').forEach((m) => {
    m.innerHTML += m.innerHTML;
  });

  /* cursor-following project preview */
  const preview = document.querySelector('.preview');
  if (preview && fine && !reduced) {
    const img = preview.querySelector('img');
    const tag = preview.querySelector('.preview__tag');
    let tx = 0, ty = 0, cx = 0, cy = 0, raf = null;

    const loop = () => {
      cx += (tx - cx) * 0.14;
      cy += (ty - cy) * 0.14;
      preview.style.left = `${cx}px`;
      preview.style.top = `${cy}px`;
      raf = Math.abs(tx - cx) > 0.3 || Math.abs(ty - cy) > 0.3 ? requestAnimationFrame(loop) : null;
    };

    const rows = document.querySelectorAll('[data-preview]');
    rows.forEach((row) => {
      row.addEventListener('pointerenter', (ev) => {
        const src = row.getAttribute('data-preview');
        if (!src) return;
        img.src = src;
        if (tag) tag.textContent = row.getAttribute('data-preview-tag') || '';
        tx = cx = ev.clientX;
        ty = cy = ev.clientY;
        preview.classList.add('is-on');
        preview.style.left = `${cx}px`;
        preview.style.top = `${cy}px`;
      });
      row.addEventListener('pointermove', (ev) => {
        tx = ev.clientX;
        ty = ev.clientY;
        if (!raf) raf = requestAnimationFrame(loop);
      });
      row.addEventListener('pointerleave', () => {
        preview.classList.remove('is-on');
      });
    });
  }

  /* local clock (every instance) */
  const clocks = document.querySelectorAll('[data-clock]');
  if (clocks.length) {
    const tick = () => {
      const now = new Date();
      const t = now.toLocaleTimeString('en-GB', {
        timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit'
      }) + ' IST';
      clocks.forEach((el) => { el.textContent = t; });
    };
    tick();
    setInterval(tick, 20000);
  }

  /* year */
  document.querySelectorAll('[data-year]').forEach((el) => {
    el.textContent = new Date().getFullYear();
  });
})();
