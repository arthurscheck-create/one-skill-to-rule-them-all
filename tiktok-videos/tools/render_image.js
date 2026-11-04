// Rendert eine HTML-Seite als PNG:  node tools/render_image.js <datei.html> <ausgabe.png> [breite] [höhe] [#hash]
const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const [file, out, w = "1080", h = "1080", hash = ""] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  await page.goto("file://" + path.resolve(file) + hash);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  await page.screenshot({ path: out });
  await browser.close();
  console.log("PNG:", out);
})();
