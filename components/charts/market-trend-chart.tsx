"use client";

import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from "recharts";
import type { CoinPoint } from "@/lib/types";
import { formatCurrency, formatTime } from "@/lib/format";

type Props = {
  data: CoinPoint[];
};

export function MarketTrendChart({ data }: Props) {
  return (
    <ResponsiveContainer width="100%" height={320}>
      <AreaChart data={data}>
        <defs>
          <linearGradient id="trendFill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#4df0b0" stopOpacity={0.5} />
            <stop offset="95%" stopColor="#4df0b0" stopOpacity={0.02} />
          </linearGradient>
        </defs>
        <CartesianGrid stroke="rgba(164,189,224,0.12)" vertical={false} />
        <XAxis
          dataKey="time"
          tickFormatter={formatTime}
          tick={{ fill: "#9baecc", fontSize: 12 }}
          tickLine={false}
          axisLine={false}
        />
        <YAxis
          tickFormatter={(value) => formatCurrency(value, 0)}
          tick={{ fill: "#9baecc", fontSize: 12 }}
          tickLine={false}
          axisLine={false}
          width={92}
        />
        <Tooltip
          contentStyle={{
            background: "#0d1f36",
            border: "1px solid rgba(164,189,224,0.15)",
            borderRadius: 16
          }}
          formatter={(value) => [formatCurrency(Number(value ?? 0), 2), "BTC 价格"]}
          labelFormatter={(label) => formatTime(String(label))}
        />
        <Area
          type="monotone"
          dataKey="price"
          stroke="#76baff"
          strokeWidth={3}
          fill="url(#trendFill)"
        />
      </AreaChart>
    </ResponsiveContainer>
  );
}
