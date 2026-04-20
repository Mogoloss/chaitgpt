"use client";

import { useEffect, useState } from "react";
import { MarketDashboard } from "@/components/dashboard/market-dashboard";
import type { DashboardData } from "@/lib/types";

type Props = {
  initialData: DashboardData;
};

export function LiveMarketDashboard({ initialData }: Props) {
  const [data, setData] = useState(initialData);

  useEffect(() => {
    let cancelled = false;

    const load = async () => {
      try {
        const response = await fetch("/api/market", { cache: "no-store" });
        if (!response.ok) return;
        const next = (await response.json()) as DashboardData;
        if (!cancelled) {
          setData(next);
        }
      } catch {
        // Keep the last successful snapshot if polling fails.
      }
    };

    const interval = window.setInterval(load, initialData.liveRefreshSeconds * 1000);
    return () => {
      cancelled = true;
      window.clearInterval(interval);
    };
  }, [initialData.liveRefreshSeconds]);

  return <MarketDashboard data={data} />;
}
