"use client";

import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from "recharts";
import { formatCompactCurrency, formatPercent } from "@/lib/format";

type HeatmapDatum = {
  label: string;
  change: number;
  volume: number;
};

type Props = {
  data: HeatmapDatum[];
};

export function VolumeBarChart({ data }: Props) {
  return (
    <ResponsiveContainer width="100%" height={320}>
      <BarChart data={data}>
        <CartesianGrid stroke="rgba(164,189,224,0.12)" vertical={false} />
        <XAxis
          dataKey="label"
          tick={{ fill: "#9baecc", fontSize: 12 }}
          tickLine={false}
          axisLine={false}
        />
        <YAxis
          tickFormatter={formatCompactCurrency}
          tick={{ fill: "#9baecc", fontSize: 12 }}
          tickLine={false}
          axisLine={false}
          width={88}
        />
        <Tooltip
          contentStyle={{
            background: "#0d1f36",
            border: "1px solid rgba(164,189,224,0.15)",
            borderRadius: 16
          }}
          formatter={(value, name) => {
            const numericValue = Number(value ?? 0);

            if (name === "volume") {
              return [formatCompactCurrency(numericValue), "24H 成交额"];
            }

            return [formatPercent(numericValue), "24H 涨跌幅"];
          }}
        />
        <Bar dataKey="volume" radius={[12, 12, 4, 4]}>
          {data.map((entry) => (
            <Cell
              key={entry.label}
              fill={entry.change >= 0 ? "rgba(77,240,176,0.85)" : "rgba(255,125,125,0.85)"}
            />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}
