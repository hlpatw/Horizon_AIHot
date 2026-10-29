(function () {
  'use strict';

  // Pair by the renderer's item anchor, never by a translated title or list position.
  function key(card) { return card.dataset.storyKey; }

  function toolbar(card, state) {
    var previous = card.querySelector('.story-toolbar');
    var bar = document.createElement('div');
    bar.className = 'story-toolbar';
    var score = card.querySelector('h3 .score-badge') || (previous && previous.querySelector('.score-badge'));
    if (score) bar.appendChild(score);
    if (previous) previous.remove();
    var group = document.createElement('div');
    group.className = 'story-lang-toggle';
    group.setAttribute('role', 'group');
    group.setAttribute('aria-label', '本条资讯语言 / Story language');
    ['zh', 'en'].forEach(function (lang) {
      var button = document.createElement('button');
      button.type = 'button';
      button.dataset.storyLanguage = lang;
      button.textContent = lang === 'zh' ? '中文' : 'EN';
      button.setAttribute('aria-pressed', String(state.language === lang));
      button.disabled = !state.variants[lang];
      button.title = button.disabled
        ? (state.loading ? '正在加载另一语言版本 / Loading translation'
          : '本条暂无此语言版本 / Translation unavailable')
        : (lang === 'zh' ? '仅查看本条中文内容' : 'Read this story in English');
      group.appendChild(button);
    });
    bar.appendChild(group);
    card.prepend(bar);
    card.lang = state.language === 'zh' ? 'zh-CN' : 'en';
  }

  function bind(target, original) {
    target.addEventListener('click', function (event) {
      var button = event.target.closest('button[data-story-language]');
      if (!button || !target.contains(button)) return;
      event.stopPropagation();
      if (button.disabled) return;
      change(original, button.dataset.storyLanguage, target);
    });
    // Feed cards also support Enter/Space; let a nested button handle its own keys.
    target.addEventListener('keydown', function (event) {
      if (event.target.closest('.story-lang-toggle')) event.stopPropagation();
    });
  }

  function change(card, language, source) {
    var state = card._storyLanguages;
    if (!state || !state.variants[language] || state.language === language) return;
    var focusCard = source === card && card.contains(document.activeElement);
    state.language = language;
    card.innerHTML = state.variants[language];
    toolbar(card, state);
    window.HorizonFeed.bindCopies(card);
    if (card.hasAttribute('aria-label')) {
      card.setAttribute('aria-label', (language === 'en' ? 'Read details: ' : '阅读详情：')
        + card.querySelector('h3').textContent.trim());
    }
    card.dispatchEvent(new CustomEvent('storylanguagechange', {
      detail: { language: language, focusDetail: source !== card }
    }));
    if (focusCard) card.querySelector('[data-story-language="' + language + '"]').focus({ preventScroll: true });
  }

  function install(card, variants, language, loading) {
    // Templates are captured before controls are added. Keep each card's choice local.
    var state = { variants: variants, language: language, loading: !!loading };
    card._storyLanguages = state;
    toolbar(card, state);
    bind(card, card);
    card.dispatchEvent(new CustomEvent('storylanguagechange'));
  }

  function snapshots(cards) {
    var result = new Map();
    cards.forEach(function (card) {
      if (!key(card)) return;
      var body = card.cloneNode(true);
      // A translated heading may already exist in the other feed. Item anchors
      // stay outside cards, so removing heading IDs keeps swaps free of duplicate IDs.
      body.querySelectorAll('[id]').forEach(function (node) { node.removeAttribute('id'); });
      result.set(key(card), body.innerHTML);
    });
    return result;
  }

  function home() {
    var zh = document.getElementById('latest-digest');
    var en = document.getElementById('latest-digest-en');
    var zhCards = zh ? Array.from(zh.querySelectorAll('.news-card')) : [];
    var enCards = en ? Array.from(en.querySelectorAll('.news-card')) : [];
    var zhBodies = snapshots(zhCards), enBodies = snapshots(enCards);
    var sameEdition = zh && en && zh.dataset.edition && zh.dataset.edition === en.dataset.edition;
    [[zhCards, 'zh', zhBodies], [enCards, 'en', enBodies]].forEach(function (entry) {
      entry[0].forEach(function (card) {
        var variants = {};
        variants[entry[1]] = entry[2].get(key(card)) || card.innerHTML;
        var other = entry[1] === 'zh' ? 'en' : 'zh';
        if (sameEdition) variants[other] = (other === 'en' ? enBodies : zhBodies).get(key(card));
        install(card, variants, entry[1], false);
      });
    });
  }

  function reading() {
    var path = location.pathname;
    if (!/-(?:zh|en)(?:\.html)?$/.test(path)) return;
    var language = /-en(?:\.html)?$/.test(path) ? 'en' : 'zh';
    var other = language === 'zh' ? 'en' : 'zh';
    var cards = Array.from(document.querySelectorAll('.article-news-card'));
    if (!cards.length) return;
    var current = snapshots(cards);
    cards.forEach(function (card) {
      var variants = {};
      variants[language] = current.get(key(card)) || card.innerHTML;
      install(card, variants, language, true);
    });
    var otherPath = path.replace(/-(?:zh|en)(\.html)?$/, '-' + other + '$1');
    var controller = new AbortController();
    var timeout = setTimeout(function () { controller.abort(); }, 15000);
    fetch(otherPath, { credentials: 'same-origin', signal: controller.signal }).then(function (response) {
      if (!response.ok) throw new Error('Translation unavailable');
      return response.text();
    }).then(function (html) {
      var doc = new DOMParser().parseFromString(html, 'text/html');
      var root = doc.querySelector('.main-content');
      if (!root) throw new Error('Translation unavailable');
      window.HorizonFeed.prepare(doc);
      root.dataset.storyLang = other;
      var otherBodies = snapshots(window.HorizonFeed.cardify(root));
      cards.forEach(function (card) {
        card._storyLanguages.variants[other] = otherBodies.get(key(card));
      });
    }).catch(function () {
      // Leave the current article readable; unavailable controls explain why.
    }).finally(function () {
      clearTimeout(timeout);
      cards.forEach(function (card) {
        card._storyLanguages.loading = false;
        toolbar(card, card._storyLanguages);
      });
    });
  }

  window.HorizonStoryLanguages = {
    // Details are clones; bind their controls back to the original story state.
    bindDetail: function (detail, card) {
      if (card._storyLanguages) bind(detail, card);
    }
  };
  document.addEventListener('DOMContentLoaded', function () {
    if (!window.HorizonFeed) return;
    if (document.getElementById('aihot-home')) home();
    else reading();
  });
})();
