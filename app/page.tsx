import { LiveMarketDashboard } from "@/components/dashboard/live-market-dashboard";
import { getDashboardData } from "@/lib/coingecko";

export const revalidate = 15;

export default async function HomePage() {
  const data = await getDashboardData();

  return <LiveMarketDashboard initialData={data} />;
}
