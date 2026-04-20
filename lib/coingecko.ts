import { unstable_cache } from "next/cache";
import { formatCompactCurrency, formatCurrency, formatPercent } from "@/lib/format";
import type {
  AiAnalysis,
  CoinMarket,
  CoinPoint,
  DashboardData,
  DirectionAnalysis,
  MarketIndex
} from "@/lib/types";

const API_BASE = "https://api.coingecko.com/api/v3";
const LIVE_REFRESH_SECONDS = 15;
const fallbackGeneratedAt = "2026-03-19T00:00:00.000Z";

function clamp(value: number, min = 0, max = 100) {
  return Math.max(min, Math.min(max, Math.round(value)));
}

function average(values: number[]) {
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

function getHeaders(): Record<string, string> {
  const apiKey = process.env.COINGECKO_API_KEY;
  const headers: Record<string, string> = {
    accept: "application/json"
  };

  if (apiKey) {
    headers["x-cg-demo-api-key"] = apiKey;
  }

  return headers;
}

async function fetchJson<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: getHeaders(),
    next: { revalidate: LIVE_REFRESH_SECONDS }
  });

  if (!response.ok) {
    throw new Error(`CoinGecko request failed: ${response.status}`);
  }

  return response.json() as Promise<T>;
}

function deriveMarketMood(change: number) {
  if (change > 2) return "趋势偏强";
  if (change > 0) return "温和回暖";
  if (change > -2) return "谨慎中性";
  return "风险偏好下降";
}

function toTrendPoints(prices: number[][], volumes: number[][]): CoinPoint[] {
  return prices.map((entry, index) => ({
    time: new Date(entry[0]).toISOString(),
    price: entry[1],
    volume: volumes[index]?.[1] ?? 0
  }));
}

function buildIndices(featuredCoins: CoinMarket[], summary: DashboardData["marketSummary"]): MarketIndex[] {
  const avgChange = average(featuredCoins.map((coin) => coin.price_change_percentage_24h));
  const breadthScore = clamp(
    (featuredCoins.filter((coin) => coin.price_change_percentage_24h > 0).length / featuredCoins.length) * 100
  );
  const trendStrengthScore = clamp(50 + avgChange * 7);
  const liquidityRatio = (summary.totalVolumeUsd / summary.totalMarketCapUsd) * 100;
  const liquidityScore = clamp(liquidityRatio * 9);
  const dominanceBalanceScore = clamp(100 - Math.abs(summary.btcDominance - 52) * 5);
  const volatilityAverage = average(
    featuredCoins.map((coin) => ((coin.high_24h - coin.low_24h) / coin.current_price) * 100)
  );
  const volatilityRiskScore = clamp(volatilityAverage * 10);
  const defiScore = clamp(summary.defiToEthRatio * 5);
  const eth = featuredCoins.find((coin) => coin.symbol.toLowerCase() === "eth");
  const btc = featuredCoins.find((coin) => coin.symbol.toLowerCase() === "btc");
  const rotationScore = clamp(
    45 +
      ((eth?.price_change_percentage_24h ?? 0) - (btc?.price_change_percentage_24h ?? 0)) * 5 +
      breadthScore * 0.2
  );

  return [
    {
      key: "trend-strength",
      name: "趋势强度指数",
      score: trendStrengthScore,
      valueLabel: `${trendStrengthScore}/100`,
      trend: trendStrengthScore >= 60 ? "up" : trendStrengthScore <= 40 ? "down" : "neutral",
      summary: "综合主流币涨跌幅得到的市场强弱评分。"
    },
    {
      key: "breadth",
      name: "市场广度指数",
      score: breadthScore,
      valueLabel: `${breadthScore}/100`,
      trend: breadthScore >= 60 ? "up" : breadthScore <= 40 ? "down" : "neutral",
      summary: "上涨主流币家数越多，说明行情扩散越健康。"
    },
    {
      key: "liquidity",
      name: "流动性脉冲指数",
      score: liquidityScore,
      valueLabel: `${liquidityRatio.toFixed(2)}%`,
      trend: liquidityScore >= 60 ? "up" : liquidityScore <= 40 ? "down" : "neutral",
      summary: "用成交额相对总市值的比例衡量市场活跃度。"
    },
    {
      key: "dominance",
      name: "主流集中度指数",
      score: dominanceBalanceScore,
      valueLabel: `${summary.btcDominance.toFixed(1)}%`,
      trend: summary.btcDominance >= 52 ? "up" : "neutral",
      summary: "围绕 BTC Dominance 判断资金是否过度集中。"
    },
    {
      key: "defi",
      name: "DeFi 活跃指数",
      score: defiScore,
      valueLabel: `${summary.defiToEthRatio.toFixed(2)}`,
      trend: defiScore >= 55 ? "up" : defiScore <= 35 ? "down" : "neutral",
      summary: "观察链上金融活跃度相对以太坊生态的表现。"
    },
    {
      key: "volatility",
      name: "波动风险指数",
      score: volatilityRiskScore,
      valueLabel: `${volatilityAverage.toFixed(2)}%`,
      trend: volatilityRiskScore >= 60 ? "down" : "neutral",
      summary: "波动越大，越需要把风控放在首位。"
    },
    {
      key: "rotation",
      name: "轮动强弱指数",
      score: rotationScore,
      valueLabel: `${rotationScore}/100`,
      trend: rotationScore >= 60 ? "up" : rotationScore <= 40 ? "down" : "neutral",
      summary: "对 BTC 与 ETH 的相对强弱和广度做出的轮动评分。"
    }
  ];
}

function buildDirection(indices: MarketIndex[]): DirectionAnalysis {
  const weightMap: Record<string, number> = {
    趋势强度指数: 0.24,
    市场广度指数: 0.18,
    流动性脉冲指数: 0.14,
    主流集中度指数: 0.1,
    "DeFi 活跃指数": 0.1,
    波动风险指数: -0.14,
    轮动强弱指数: 0.18
  };

  const rawScore = indices.reduce((sum, index) => sum + index.score * (weightMap[index.name] ?? 0), 0);
  const confidence = clamp(rawScore + 15);

  if (confidence >= 62) {
    return {
      bias: "看多",
      confidence,
      summary: "主流币结构、广度和流动性更支持偏多观察，但仍要防止高波动回撤。"
    };
  }

  if (confidence <= 42) {
    return {
      bias: "看空",
      confidence,
      summary: "当前指数组合偏弱，短线更适合先防守，再等待结构修复。"
    };
  }

  return {
    bias: "中性",
    confidence,
    summary: "当前指数组合更接近震荡观察，方向暂未形成一致性。"
  };
}

function buildAiAnalysis(
  featuredCoins: CoinMarket[],
  summary: DashboardData["marketSummary"],
  direction: DirectionAnalysis,
  indices: MarketIndex[]
): AiAnalysis {
  const btc = featuredCoins.find((coin) => coin.symbol.toLowerCase() === "btc") ?? featuredCoins[0];
  const eth = featuredCoins.find((coin) => coin.symbol.toLowerCase() === "eth") ?? featuredCoins[1];
  const topTrend = indices.find((index) => index.key === "trend-strength");
  const topBreadth = indices.find((index) => index.key === "breadth");
  const riskIndex = indices.find((index) => index.key === "volatility");

  return {
    headline: `实时方向结论：${direction.bias}`,
    summary: `AI 综合 ${topTrend?.name}、${topBreadth?.name}、BTC Dominance 与成交额判断，当前更适合采取“${direction.bias}”视角。${direction.summary}`,
    shortTerm: `短线更应该盯住 BTC 在 ${formatCurrency(btc.low_24h, 0)} - ${formatCurrency(
      btc.high_24h,
      0
    )} 区间内的选择方向，以及 ETH 是否同步跟随。`,
    midTerm: "中期继续观察主流币是否维持扩散。如果 ETH 明显弱于 BTC，通常说明风险偏好还没真正回到进攻状态。",
    risk: `当前波动风险指数为 ${riskIndex?.score ?? 0}/100，全市场 24H 市值变化为 ${formatPercent(
      summary.marketCapChange24h
    )}。高波动时不宜只看 AI 偏向，还要同步约束仓位与止损。`,
    actions: [
      "行情数据每 15 秒刷新一次，优先观察价格与方向结论是否共振。",
      `重点追踪 BTC 当前价格 ${formatCurrency(btc.current_price, 0)} 与 ETH 当前价格 ${formatCurrency(
        eth.current_price,
        0
      )} 的联动关系。`,
      "若趋势强度和广度同时回升，再考虑提高进攻性；若波动风险抬升，则优先收缩风险敞口。"
    ]
  };
}

type GlobalResponse = {
  data: {
    active_cryptocurrencies: number;
    markets: number;
    total_market_cap: {
      usd: number;
    };
    total_volume: {
      usd: number;
    };
    market_cap_percentage: {
      btc: number;
    };
    market_cap_change_percentage_24h_usd: number;
  };
};

type DefiResponse = {
  data: {
    defi_market_cap: string;
    defi_to_eth_ratio: string;
  };
};

type MarketChartResponse = {
  prices: number[][];
  total_volumes: number[][];
};

function createDashboardData(
  generatedAt: string,
  featuredCoins: CoinMarket[],
  marketSummary: DashboardData["marketSummary"],
  trend: CoinPoint[]
): DashboardData {
  const indices = buildIndices(featuredCoins, marketSummary);
  const direction = buildDirection(indices);
  const aiAnalysis = buildAiAnalysis(featuredCoins, marketSummary, direction, indices);

  return {
    generatedAt,
    liveRefreshSeconds: LIVE_REFRESH_SECONDS,
    marketMood: deriveMarketMood(marketSummary.marketCapChange24h),
    marketSummary,
    featuredCoins,
    trend,
    heatmap: featuredCoins.map((coin) => ({
      label: coin.symbol.toUpperCase(),
      change: coin.price_change_percentage_24h,
      volume: coin.total_volume
    })),
    indices,
    direction,
    aiAnalysis
  };
}

const fallbackFeaturedCoins: CoinMarket[] = [
  {
    id: "bitcoin",
    symbol: "btc",
    name: "Bitcoin",
    image: "https://assets.coingecko.com/coins/images/1/large/bitcoin.png",
    current_price: 71314,
    market_cap: 1425683163740,
    total_volume: 43920584675,
    price_change_percentage_24h: -3.88,
    circulating_supply: 19840000,
    market_cap_rank: 1,
    high_24h: 74280,
    low_24h: 70620,
    ath_change_percentage: -3.1,
    sparkline_in_7d: { price: [] }
  },
  {
    id: "ethereum",
    symbol: "eth",
    name: "Ethereum",
    image: "https://assets.coingecko.com/coins/images/279/large/ethereum.png",
    current_price: 2183.01,
    market_cap: 263257295978,
    total_volume: 21198291363,
    price_change_percentage_24h: -6.16,
    circulating_supply: 120700000,
    market_cap_rank: 2,
    high_24h: 2348,
    low_24h: 2162,
    ath_change_percentage: -55.4,
    sparkline_in_7d: { price: [] }
  },
  {
    id: "solana",
    symbol: "sol",
    name: "Solana",
    image: "https://assets.coingecko.com/coins/images/4128/large/solana.png",
    current_price: 89,
    market_cap: 50834454599,
    total_volume: 3834113849,
    price_change_percentage_24h: -5.9,
    circulating_supply: 571200000,
    market_cap_rank: 6,
    high_24h: 95,
    low_24h: 88,
    ath_change_percentage: -65.8,
    sparkline_in_7d: { price: [] }
  },
  {
    id: "binancecoin",
    symbol: "bnb",
    name: "BNB",
    image: "https://assets.coingecko.com/coins/images/825/large/bnb-icon2_2x.png",
    current_price: 647.59,
    market_cap: 88326612938,
    total_volume: 1123863495,
    price_change_percentage_24h: -3.49,
    circulating_supply: 136400000,
    market_cap_rank: 5,
    high_24h: 671,
    low_24h: 643,
    ath_change_percentage: -20.6,
    sparkline_in_7d: { price: [] }
  }
];

const fallbackMarketSummary: DashboardData["marketSummary"] = {
  activeCryptocurrencies: 17483,
  markets: 1189,
  totalMarketCapUsd: 2730000000000,
  marketCapChange24h: -1.42,
  totalVolumeUsd: 122000000000,
  btcDominance: 52.4,
  defiMarketCapUsd: 94500000000,
  defiToEthRatio: 11.5
};

const fallbackTrend: CoinPoint[] = [
  { time: "2026-03-13T00:00:00.000Z", price: 81120, volume: 38600000000 },
  { time: "2026-03-14T00:00:00.000Z", price: 79880, volume: 35200000000 },
  { time: "2026-03-15T00:00:00.000Z", price: 78610, volume: 36400000000 },
  { time: "2026-03-16T00:00:00.000Z", price: 76950, volume: 40100000000 },
  { time: "2026-03-17T00:00:00.000Z", price: 75280, volume: 41800000000 },
  { time: "2026-03-18T00:00:00.000Z", price: 73320, volume: 44600000000 },
  { time: "2026-03-19T00:00:00.000Z", price: 71314, volume: 43920584675 }
];

const fallbackData = createDashboardData(
  fallbackGeneratedAt,
  fallbackFeaturedCoins,
  fallbackMarketSummary,
  fallbackTrend
);

const loadDashboardData = unstable_cache(
  async (): Promise<DashboardData> => {
    try {
      const [featuredCoins, global, defi, chart] = await Promise.all([
        fetchJson<CoinMarket[]>(
          "/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,solana,binancecoin&order=market_cap_desc&sparkline=true&price_change_percentage=24h"
        ),
        fetchJson<GlobalResponse>("/global"),
        fetchJson<DefiResponse>("/global/decentralized_finance_defi"),
        fetchJson<MarketChartResponse>("/coins/bitcoin/market_chart?vs_currency=usd&days=7&interval=daily")
      ]);

      const marketSummary = {
        activeCryptocurrencies: global.data.active_cryptocurrencies,
        markets: global.data.markets,
        totalMarketCapUsd: global.data.total_market_cap.usd,
        marketCapChange24h: global.data.market_cap_change_percentage_24h_usd,
        totalVolumeUsd: global.data.total_volume.usd,
        btcDominance: global.data.market_cap_percentage.btc,
        defiMarketCapUsd: Number(defi.data.defi_market_cap),
        defiToEthRatio: Number(defi.data.defi_to_eth_ratio)
      };

      return createDashboardData(
        new Date().toISOString(),
        featuredCoins,
        marketSummary,
        toTrendPoints(chart.prices, chart.total_volumes)
      );
    } catch {
      return fallbackData;
    }
  },
  ["dashboard-data-live"],
  { revalidate: LIVE_REFRESH_SECONDS }
);

export async function getDashboardData() {
  return loadDashboardData();
}
