"""Offline browser checks: pip install playwright; python tests/test_story_languages_browser.py.

Uses installed Chrome by default; set HORIZON_BROWSER_CHANNEL to another channel.
No AI keys, network requests, or live-site writes are required.
"""
import os
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://hlpatw.github.io/Horizon_AIHot/"
ARTICLE = BASE + "2026/10/29/summary-zh.html"
TITLES = {
    "zh": {1: "中文标题一", 2: "本条资讯的中文解读暂未生成", 3: "中文标题三"},
    "en": {1: "English story one", 2: "English story two", 3: "English story three"},
}


def stories(lang, order=(1, 2, 3)):
    return "".join(
        f'<p><a id="item-tech-news-{i}"></a></p>'
        f'<h3 id="heading-{lang}-{i}">{TITLES[lang][i]} ⭐️ 7.0/10</h3>'
        f'<p>{"中文解读生成失败" if lang == "zh" and i == 2 else lang + " summary " + str(i)}</p>'
        f'<p>hackernews · author{i} · 10月28日 17:01</p>'
        f'<div class="story-actions"><a href="https://example.com/{i}">Source</a>'
        f'<button class="copy-story-link" data-copy-url="https://example.com/{i}">'
        f'{"Copy link" if lang == "en" else "复制链接"}</button></div>'
        f'<p><strong>{"标签" if lang == "zh" else "Tags"}</strong>: <code>#AI</code></p><hr>'
        for i in order
    )


def document(body):
    return ('<!doctype html><html><head><meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<link rel="stylesheet" href="/Horizon_AIHot/assets/css/horizon.css">'
            '<script src="/Horizon_AIHot/assets/js/horizon.js" defer></script>'
            '<script src="/Horizon_AIHot/assets/js/story-languages.js" defer></script>'
            '</head><body><main class="main-content">' + body
            + '<footer class="site-footer">Original footer</footer></main></body></html>')


def home(en_order=(3, 2, 1), en_date="2026-10-29"):
    body = '<div id="aihot-home">'
    for lang, suffix, order in (("zh", "", (1, 2, 3)), ("en", "-en", en_order)):
        body += (
            f'<div id="lang-{lang}" class="lang-section {"hidden" if lang == "en" else ""}">'
            f'<input id="digest-search{suffix}" placeholder="Search">'
            f'<div class="topic-filters" data-for="latest-digest{suffix}">'
            '<button data-filter="all" class="active">All</button></div><div class="digest-layout">'
            f'<article id="latest-digest{suffix}" class="embedded-digest" '
            f'data-edition="{en_date if lang == "en" else "2026-10-29"}">'
            + stories(lang, order) + '</article><aside class="digest-aside">'
            f'<div id="detail-panel{suffix}" class="detail-panel">'
            f'<div id="detail-highlights{suffix}"></div></div></aside></div>'
            f'<div id="detail-backdrop{suffix}" class="detail-backdrop" hidden></div></div>'
        )
    return document(body + '</div>')


@unittest.skipUnless(sync_playwright, "Install playwright to run browser checks")
class StoryLanguagesBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(
            channel=os.environ.get("HORIZON_BROWSER_CHANNEL", "chrome"), headless=True
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.context = self.browser.new_context(viewport={"width": 1440, "height": 1000})
        self.page = self.context.new_page()
        self.errors = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))
        self.page.add_init_script("""window.copied = [];
          Object.defineProperty(navigator, 'clipboard', {value: {
            writeText: async function(text) { window.copied.push(text); }
          }});""")
        self.home_html = home()
        self.counterpart_status = 200
        self.page.route("**/*", self.route)

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors, [])

    def route(self, route):
        path = urlsplit(route.request.url).path
        asset = re.search(r"/assets/(js|css)/([^/]+)$", path)
        if asset:
            file = ROOT / "docs" / "assets" / asset[1] / asset[2]
            route.fulfill(path=str(file), content_type="text/javascript" if asset[1] == "js" else "text/css")
        elif path.endswith("summary-en.html"):
            route.fulfill(status=self.counterpart_status, body=document(stories("en", (3, 2, 1))))
        elif path.endswith("summary-zh.html"):
            route.fulfill(body=document(stories("zh")))
        elif path.rstrip("/") == "/Horizon_AIHot":
            route.fulfill(body=self.home_html)
        else:
            route.abort()

    def card(self, i=2, lang="zh"):
        return self.page.locator(f'#lang-{lang} .news-card[data-story-key="item-tech-news-{i}"]')

    def switch(self, card, lang):
        card.locator(f'.story-lang-toggle [data-story-language="{lang}"]').click()

    def test_missing_chinese_switches_only_that_story_and_restores(self):
        self.page.goto(BASE)
        card = self.card()
        self.assertIn("暂未生成", card.locator("h3").inner_text())
        self.switch(card, "en")
        self.assertEqual(card.locator("h3").inner_text().strip(), TITLES["en"][2])
        self.assertEqual(self.card(1).locator("h3").inner_text().strip(), TITLES["zh"][1])
        self.assertEqual(self.page.url, BASE)
        self.assertFalse(self.page.locator("#detail-panel").evaluate("e=>e.classList.contains('has-detail')"))
        self.assertEqual(self.page.evaluate("localStorage.getItem('horizon-lang')"), "zh")
        self.assertEqual(card.locator(".score-badge").count(), 1)
        self.switch(card, "zh")
        self.assertIn("暂未生成", card.locator("h3").inner_text())

    def test_matches_stable_key_when_other_language_order_differs(self):
        self.page.goto(BASE)
        self.switch(self.card(1), "en")
        self.assertEqual(self.card(1).locator("h3").inner_text().strip(), TITLES["en"][1])
        self.assertEqual(self.card(1).locator(".copy-story-link").get_attribute("data-copy-url"), "https://example.com/1")

    def test_detail_switch_syncs_card_copy_and_navigation(self):
        self.page.goto(BASE)
        card = self.card()
        card.locator(".card-read-more").click()
        before = self.page.url
        detail = self.page.locator("#detail-panel .detail-story")
        self.switch(detail, "en")
        self.assertEqual(detail.locator("h3").inner_text().strip(), TITLES["en"][2])
        self.assertEqual(card.get_attribute("lang"), "en")
        self.assertEqual(self.page.url, before)
        detail.locator(".copy-story-link").click()
        self.assertEqual(self.page.evaluate("window.copied"), ["https://example.com/2"])
        self.page.locator('#detail-panel [data-direction="next"]').click()
        self.assertEqual(detail.locator("h3").inner_text().strip(), TITLES["zh"][3])

    def test_keyboard_does_not_open_details(self):
        self.page.goto(BASE)
        button = self.card().locator('[data-story-language="en"]')
        button.focus()
        button.press("Enter")
        self.assertEqual(self.card().get_attribute("lang"), "en")
        self.assertEqual(self.page.locator(":focus").get_attribute("data-story-language"), "en")
        self.assertNotIn("#", self.page.url)

    def test_global_toggle_and_search_keep_working(self):
        self.page.goto(BASE)
        self.page.locator("#digest-search").fill("summary 1")
        self.switch(self.card(1), "en")
        self.assertEqual(self.page.locator("#digest-search").input_value(), "summary 1")
        self.page.locator('.lang-toggle button', has_text="EN").click()
        self.assertTrue(self.page.locator("#lang-en").is_visible())
        self.switch(self.card(2, "en"), "zh")
        self.assertEqual(self.card(2, "en").get_attribute("lang"), "zh-CN")
        self.assertEqual(self.card(1, "en").get_attribute("lang"), "en")

    def test_different_editions_do_not_pair(self):
        self.home_html = home(en_date="2026-10-28")
        self.page.goto(BASE)
        self.assertTrue(self.card().locator('[data-story-language="en"]').is_disabled())

    def test_missing_counterpart_does_not_use_a_neighbor(self):
        self.home_html = home(en_order=(3, 1))
        self.page.goto(BASE)
        self.assertTrue(self.card().locator('[data-story-language="en"]').is_disabled())
        self.assertTrue(self.card(1).locator('[data-story-language="en"]').is_enabled())

    def test_reading_page_switches_in_place_and_preserves_anchors_and_footer(self):
        self.page.goto(ARTICLE)
        card = self.page.locator('.article-news-card[data-story-key="item-tech-news-2"]')
        self.page.wait_for_function("!document.querySelector('[data-story-language=en]').disabled")
        self.switch(card, "en")
        self.assertEqual(card.locator("h3").inner_text().strip(), TITLES["en"][2])
        self.assertEqual(self.page.url, ARTICLE)
        self.assertEqual(self.page.locator("#item-tech-news-2").count(), 1)
        self.assertEqual(self.page.locator(".article-news-card footer").count(), 0)
        self.assertEqual(card.locator(".score-badge").count(), 1)
        self.switch(card, "zh")
        self.assertIn("暂未生成", card.locator("h3").inner_text())

    def test_reading_page_handles_unavailable_translation(self):
        self.counterpart_status = 404
        self.page.goto(ARTICLE)
        self.page.wait_for_function("document.querySelector('[data-story-language=en]').title.includes('unavailable')")
        card = self.page.locator('.article-news-card[data-story-key="item-tech-news-2"]')
        self.assertTrue(card.locator('[data-story-language="en"]').is_disabled())
        self.assertIn("暂未生成", card.locator("h3").inner_text())
        self.assertEqual(card.locator(".score-badge").count(), 1)

    def test_mobile_layout_and_detail_toggle(self):
        self.page.set_viewport_size({"width": 375, "height": 812})
        self.page.goto(BASE)
        card = self.card()
        self.switch(card, "en")
        toolbar = card.locator(".story-toolbar").bounding_box()
        heading = card.locator("h3").bounding_box()
        self.assertLessEqual(toolbar["y"] + toolbar["height"], heading["y"] + 1)
        self.assertLessEqual(self.page.evaluate("document.documentElement.scrollWidth"), 375)
        card.locator(".card-read-more").click()
        detail = self.page.locator("#detail-panel .detail-story")
        self.switch(detail, "zh")
        self.assertIn("暂未生成", detail.locator("h3").inner_text())
        self.assertTrue(self.page.locator("#detail-panel").is_visible())


if __name__ == "__main__":
    unittest.main(verbosity=2)
