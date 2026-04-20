import Image from "next/image";
import { formatCompactCurrency, formatCurrency, formatPercent, formatTime } from "@/lib/format";
import type { DashboardData, MarketIndex } from "@/lib/types";

type Props = {
  data: DashboardData;
};

function getTrendClass(trend: MarketIndex["trend"]) {
  if (trend === "up") return "change-up";
  if (trend === "down") return "change-down";
  return "muted";
}

export function MarketDashboard({ data }: Props) {
  const topIndices = data.indices.slice(0, 4);

  return (
    <main className="shell shell-compact">
      <section className="compact-hero panel">
        <div>
          <p className="eyebrow">Live Crypto View</p>
          <h1>主流币指数与实时方向</h1>
          <p className="hero-copy compact-copy">
            行情、指数和 AI 方向都会跟随最新数据实时刷新。当前页面每 {data.liveRefreshSeconds} 秒自动更新一次。
          </p>
        </div>

        <div className="hero-side">
          <div className="direction-pill">
            <span className="mini-label">方向结论</span>
            <strong
              className={
                data.direction.bias === "看多"
                  ? "change-up"
                  : data.direction.bias === "看空"
                    ? "change-down"
                    : ""
              }
            >
              {data.direction.bias}
            </strong>
          </div>
          <div className="direction-pill">
            <span className="mini-label">最近刷新</span>
            <strong>{formatTime(data.generatedAt)}</strong>
          </div>
        </div>
      </section>

      <section className="compact-grid">
        <article className="panel compact-card">
          <div className="section-head">
            <div>
              <p className="eyebrow">Overview</p>
              <h2>核心状态</h2>
            </div>
          </div>
          <div className="mini-stats">
            <div>
              <span className="mini-label">市场情绪</span>
              <strong>{data.marketMood}</strong>
            </div>
            <div>
              <span className="mini-label">方向置信度</span>
              <strong>{data.direction.confidence}/100</strong>
            </div>
            <div>
              <span className="mini-label">总市值</span>
              <strong>{formatCompactCurrency(data.marketSummary.totalMarketCapUsd)}</strong>
            </div>
            <div>
              <span className="mini-label">BTC Dominance</span>
              <strong>{formatPercent(data.marketSummary.btcDominance)}</strong>
            </div>
          </div>
        </article>

        <article className="panel compact-card">
          <div className="section-head">
            <div>
              <p className="eyebrow">AI Summary</p>
              <h2>{data.aiAnalysis.headline}</h2>
            </div>
          </div>
          <p className="compact-text">{data.aiAnalysis.summary}</p>
          <p className="compact-text">{data.aiAnalysis.shortTerm}</p>
        </article>
      </section>

      <section className="compact-section panel">
        <div className="section-head">
          <div>
            <p className="eyebrow">Indices</p>
            <h2>核心指数</h2>
          </div>
          <span className="muted">实时计算</span>
        </div>
        <div className="index-grid compact-index-grid">
          {topIndices.map((index) => (
            <article className="index-card" key={index.key}>
              <span className="mini-label">{index.name}</span>
              <strong className="index-score">{index.score}/100</strong>
              <span className={getTrendClass(index.trend)}>
                {index.trend === "up" ? "偏强" : index.trend === "down" ? "偏弱" : "中性"}
              </span>
              <p className="muted">{index.summary}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="compact-section panel">
        <div className="section-head">
          <div>
            <p className="eyebrow">Mainstream Coins</p>
            <h2>主流币概览</h2>
          </div>
          <span className="muted">每 {data.liveRefreshSeconds} 秒刷新</span>
        </div>
        <div className="ticker-grid compact-ticker-grid">
          {data.featuredCoins.map((coin) => (
            <article className="ticker-card" key={coin.id}>
              <div className="ticker-top">
                <div className="coin-row">
                  <Image alt={coin.name} className="coin-logo" height={34} src={coin.image} width={34} />
                  <div>
                    <strong>{coin.symbol.toUpperCase()}</strong>
                    <span className="mini-label">{coin.name}</span>
                  </div>
                </div>
                <span
                  className={
                    coin.price_change_percentage_24h >= 0 ? "change-up" : "change-down"
                  }
                >
                  {formatPercent(coin.price_change_percentage_24h)}
                </span>
              </div>
              <strong className="ticker-price">
                {formatCurrency(coin.current_price, coin.current_price < 10 ? 2 : 0)}
              </strong>
              <span className="metric-sub">成交量 {formatCompactCurrency(coin.total_volume)}</span>
            </article>
          ))}
        </div>
      </section>

      <section className="compact-grid">
        <article className="panel compact-card">
          <div className="section-head">
            <div>
              <p className="eyebrow">Direction</p>
              <h2>操作方向</h2>
            </div>
          </div>
          <ul className="signal-list">
            {data.aiAnalysis.actions.slice(0, 3).map((action) => (
              <li key={action}>{action}</li>
            ))}
          </ul>
        </article>

        <article className="panel compact-card">
          <div className="section-head">
            <div>
              <p className="eyebrow">Risk</p>
              <h2>风险提醒</h2>
            </div>
          </div>
          <p className="compact-text">{data.aiAnalysis.risk}</p>
          <p className="footer-note">本轮数据时间：{formatTime(data.generatedAt)}</p>
        </article>
      </section>
    </main>
  );
}
