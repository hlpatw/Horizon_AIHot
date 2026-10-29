---
layout: default
title: AIHOT Radar
---
{% assign zh_posts = site.posts | where: "lang", "zh" %}
{% assign en_posts = site.posts | where: "lang", "en" %}
{% assign latest_zh = zh_posts | first %}
{% assign latest_en = en_posts | first %}


<div id="aihot-home" class="radar-home">
  <header class="radar-nav">
    <a class="radar-brand" href="{{ '/' | relative_url }}" aria-label="AIHOT Radar 首页">
      <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M4 21a12 12 0 0 1 24 0"/><path d="M8 21a8 8 0 0 1 16 0"/><path d="M12 21a4 4 0 0 1 8 0"/><circle cx="16" cy="21" r="2"/></svg>
      <span>AIHOT <b>DAILY</b></span>
    </a>
    <nav class="radar-actions" aria-label="快捷操作">
      <a href="{{ '/feed-zh.xml' | relative_url }}">订阅 RSS</a>
      <a href="https://github.com/hlpatw/Horizon_AIHot">管理站点</a>
    </nav>
  </header>


  <section class="radar-intro">
    <div>
      <p class="radar-status"><span></span> 今日份已为你整理好</p>
      <h1><span id="time-greeting">你好</span>，今天的 AI 新鲜事<br>都在这里。</h1>
      <p class="radar-lead">从 Hacker News、Reddit、RSS 与 GitHub 中挑出真正值得看的变化。中文速读、英文原文，想浅看或深读都可以。</p>
    </div>
    {% if latest_zh %}
    <div class="radar-signal" aria-label="最新一期信息">
      <span>本期日期</span>
      <strong>{{ latest_zh.date | date: "%m.%d" }}</strong>
      <small>{{ latest_zh.content | strip_html | size }} 字符情报</small>
    </div>
    {% endif %}
  </section>


  <div id="lang-zh" class="lang-section">
    {% if latest_zh %}
    <section class="digest-toolbar" aria-label="今日速递工具栏">
      <div>
        <span class="section-kicker">今日精选</span>
        <h2>{{ latest_zh.date | date: "%Y 年 %m 月 %d 日" }}</h2>
      </div>
      <label class="digest-search">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6"/><path d="m16 16 4 4"/></svg>
        <input id="digest-search" type="search" placeholder="搜索今日资讯、标签或来源" autocomplete="off">
      </label>
    </section>


    <div class="topic-filters" data-for="latest-digest" aria-label="资讯分类筛选">
      <button type="button" class="active" data-filter="all">全部</button>
      <button type="button" data-filter="product">模型与产品</button>
      <button type="button" data-filter="dev">开发工具</button>
      <button type="button" data-filter="research">研究</button>
      <button type="button" data-filter="industry">行业</button>
    </div>

    <div class="digest-layout">
      <article id="latest-digest" class="embedded-digest" data-edition="{{ latest_zh.date | date: '%Y-%m-%d' }}">
        {{ latest_zh.content }}
      </article>
      <aside class="digest-aside" aria-label="资讯详情">
        <div id="detail-panel" class="detail-panel" aria-live="polite">
          <div class="detail-empty">
            <span class="detail-kicker">今日重点</span>
            <h3>选择一条资讯，留在首页继续阅读</h3>
            <p>点击左侧标题或卡片，这里会展示完整背景、影响、社区讨论和参考链接。</p>
            <div id="detail-highlights" class="detail-highlights"></div>
          </div>
        </div>
        <a class="full-report-link" href="{{ latest_zh.url | relative_url }}">打开独立阅读模式</a>
      </aside>
    </div>
    <div id="detail-backdrop" class="detail-backdrop" hidden></div>
    {% else %}
    <div class="empty-radar">日报生成后会直接出现在这里。</div>
    {% endif %}


    <section class="archive-strip">
      <div><span class="section-kicker">往期归档</span><h2>继续回看</h2></div>
      <div class="archive-list">
        {% for post in zh_posts limit:8 %}
          <a href="{{ post.url | relative_url }}"><time>{{ post.date | date: "%m.%d" }}</time><span>{{ post.title | replace: 'Horizon Summary: ', '' | replace: ' (ZH)', '' }}</span></a>
        {% endfor %}
      </div>
    </section>
  </div>


  <div id="lang-en" class="lang-section hidden">
    {% if latest_en %}
      <section class="digest-toolbar">
        <div><span class="section-kicker">Latest briefing</span><h2>{{ latest_en.date | date: "%B %d, %Y" }}</h2></div>
        <label class="digest-search">
          <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6"/><path d="m16 16 4 4"/></svg>
          <input id="digest-search-en" type="search" placeholder="Search stories, tags, or sources" autocomplete="off">
        </label>
      </section>
      <div class="topic-filters" data-for="latest-digest-en" aria-label="Story filters">
        <button type="button" class="active" data-filter="all">All</button>
        <button type="button" data-filter="product">Models & products</button>
        <button type="button" data-filter="dev">Developer tools</button>
        <button type="button" data-filter="research">Research</button>
        <button type="button" data-filter="industry">Industry</button>
      </div>
      <div class="digest-layout">
        <article id="latest-digest-en" class="embedded-digest" data-edition="{{ latest_en.date | date: '%Y-%m-%d' }}">{{ latest_en.content }}</article>
        <aside class="digest-aside" aria-label="Story details">
          <div id="detail-panel-en" class="detail-panel" aria-live="polite">
            <div class="detail-empty">
              <span class="detail-kicker">Top stories</span>
              <h3>Select a story and keep reading here</h3>
              <p>Choose a card to see the full context, impact, discussion, and references.</p>
              <div id="detail-highlights-en" class="detail-highlights"></div>
            </div>
          </div>
          <a class="full-report-link" href="{{ latest_en.url | relative_url }}">Open reading mode</a>
        </aside>
      </div>
      <div id="detail-backdrop-en" class="detail-backdrop" hidden></div>
    {% endif %}
  </div>
</div>
