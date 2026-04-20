export type CoinMarket = {
  id: string;
  symbol: string;
  name: string;
  image: string;
  current_price: number;
  market_cap: number;
  total_volume: number;
  price_change_percentage_24h: number;
  circulating_supply: number;
  market_cap_rank: number;
  high_24h: number;
  low_24h: number;
  ath_change_percentage: number;
  sparkline_in_7d?: {
    price: number[];
  };
};

export type CoinPoint = {
  time: string;
  price: number;
  volume?: number;
};

export type MarketIndex = {
  key: string;
  name: string;
  score: number;
  valueLabel: string;
  trend: "up" | "down" | "neutral";
  summary: string;
};

export type DirectionAnalysis = {
  bias: "看多" | "中性" | "看空";
  confidence: number;
  summary: string;
};

export type AiAnalysis = {
  headline: string;
  summary: string;
  shortTerm: string;
  midTerm: string;
  risk: string;
  actions: string[];
};

export type DashboardData = {
  generatedAt: string;
  liveRefreshSeconds: number;
  marketMood: string;
  marketSummary: {
    activeCryptocurrencies: number;
    markets: number;
    totalMarketCapUsd: number;
    marketCapChange24h: number;
    totalVolumeUsd: number;
    btcDominance: number;
    defiMarketCapUsd: number;
    defiToEthRatio: number;
  };
  featuredCoins: CoinMarket[];
  trend: CoinPoint[];
  heatmap: Array<{
    label: string;
    change: number;
    volume: number;
  }>;
  indices: MarketIndex[];
  direction: DirectionAnalysis;
  aiAnalysis: AiAnalysis;
};
