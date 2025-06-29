document.addEventListener('DOMContentLoaded', function() {
  // Fetch top 10 crypto prices from CoinGecko and render ticker and grid
  fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1')
    .then(res => res.json())
    .then(data => {
      // Ticker
      document.getElementById('ticker').innerHTML = data.map(coin =>
        `<span>
          <img src="${coin.image}" alt="${coin.symbol}" style="width:20px;vertical-align:middle;">
          <b>${coin.name}</b>: $${coin.current_price.toLocaleString()} 
          <span style="color:${coin.price_change_percentage_24h>=0?'#0f0':'#f00'};">
            (${coin.price_change_percentage_24h.toFixed(2)}%)
          </span>
        </span>`
      ).join(' &nbsp; | &nbsp; ');

      // Top 10 grid
      document.getElementById('top10-grid').innerHTML = data.map(coin => `
        <div class="crypto-card">
          <img src="${coin.image}" alt="${coin.symbol}" class="crypto-icon">
          <div class="crypto-name">${coin.name}</div>
          <div class="crypto-price">$${coin.current_price.toLocaleString()}</div>
          <div class="crypto-change" style="color:${coin.price_change_percentage_24h>=0?'#0f0':'#f00'};">
            ${coin.price_change_percentage_24h.toFixed(2)}%
          </div>
        </div>
      `).join('');
    });

  // Fetch news from CoinDesk RSS via rss2json
  async function fetchNews() {
      const url = 'https://api.rss2json.com/v1/api.json?rss_url=https://www.coindesk.com/arc/outboundfeeds/rss/';
      try {
          const res = await fetch(url);
          const data = await res.json();
          if (data.items && data.items.length > 0) {
              document.getElementById('news').innerHTML = data.items.slice(0, 5).map(item =>
                  `<li>
                      <a href="${item.link}" target="_blank">${item.title}</a>
                      <div style="font-size:0.9em;color:#888;">${item.pubDate.split(' ')[0]}</div>
                      <div style="font-size:0.95em;">${item.description.replace(/<[^>]+>/g, '').slice(0, 100)}...</div>
                      ${item.thumbnail ? `<img src="${item.thumbnail}" alt="news image" style="width:100%;max-width:180px;border-radius:8px;margin-top:4px;">` : ''}
                  </li>`
              ).join('');
          } else {
              document.getElementById('news').innerHTML = '<li>No news found.</li>';
          }
      } catch (e) {
          document.getElementById('news').innerHTML = '<li>Could not load news.</li>';
      }
  }
  fetchNews();

  // Fetch articles from Cointelegraph RSS via rss2json
  async function fetchArticles() {
      const url = 'https://api.rss2json.com/v1/api.json?rss_url=https://cointelegraph.com/rss';
      try {
          const res = await fetch(url);
          const data = await res.json();
          if (data.items && data.items.length > 0) {
              document.getElementById('articles').innerHTML = data.items.slice(0, 5).map(item =>
                  `<li>
                      <a href="${item.link}" target="_blank">${item.title}</a>
                      <div style="font-size:0.9em;color:#888;">${item.pubDate.split(' ')[0]}</div>
                      <div style="font-size:0.95em;">${item.description.replace(/<[^>]+>/g, '').slice(0, 100)}...</div>
                      ${item.thumbnail ? `<img src="${item.thumbnail}" alt="article image" style="width:100%;max-width:180px;border-radius:8px;margin-top:4px;">` : ''}
                  </li>`
              ).join('');
          } else {
              document.getElementById('articles').innerHTML = '<li>No articles found.</li>';
          }
      } catch (e) {
          document.getElementById('articles').innerHTML = '<li>Could not load articles.</li>';
      }
  }
  fetchArticles();
});

// Place this inside a <script> tag at the end of your body or after DOMContentLoaded

// Render all cryptos as cards in a grid
fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1')
  .then(res => res.json())
  .then(data => {
    document.getElementById('all-cryptos').innerHTML = data.map(coin => `
      <div class="all-crypto-card">
        <img src="${coin.image}" alt="${coin.symbol}" class="all-crypto-logo">
        <div class="all-crypto-name">${coin.name}</div>
        <div class="all-crypto-symbol">${coin.symbol.toUpperCase()}</div>
        <div class="all-crypto-price">$${coin.current_price.toLocaleString()}</div>
        <div class="all-crypto-change" style="color:${coin.price_change_percentage_24h>=0?'#0f0':'#f00'};">
          ${coin.price_change_percentage_24h>=0?'+':''}${coin.price_change_percentage_24h.toFixed(2)}%
        </div>
      </div>
    `).join('');
  });