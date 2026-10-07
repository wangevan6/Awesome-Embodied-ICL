// Regenerate the README screenshots in assets/readme/ from a locally served website.
// The banners there come from the brand kit and are not generated.
// Requires Playwright (npm install playwright). Usage:
//   python3 scripts/build_site.py
//   python3 -m http.server 8765 --bind 127.0.0.1 --directory _site &
//   node scripts/capture_readme_images.js http://127.0.0.1:8765/
const path = require('path');
const { chromium } = require('playwright');

const OUT = path.join(__dirname, '..', 'assets', 'readme');

(async () => {
  const site = process.argv[2] || 'http://127.0.0.1:8765/';
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});

  const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  await page.goto(new URL('index.html', site).href, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.addStyleTag({ content: '.agent-track{animation:none!important}' });  // Hold the ticker still.
  await page.screenshot({ path: path.join(OUT, 'website.png') });

  // The README supplies its own heading, so capture only the legend and the tree.
  await page.addStyleTag({ content: '.site-header,.agent-float,.skip-link,.survey-map-head > div{display:none!important}.survey-map-head{justify-content:flex-end!important}.survey-map{border-top:0!important}' });
  const map = await page.$('#survey-map');
  await map.scrollIntoViewIfNeeded();
  await map.screenshot({ path: path.join(OUT, 'survey-map.png') });

  await browser.close();
})();
