import { NextResponse } from "next/server";
import { getDashboardData } from "@/lib/coingecko";

export const revalidate = 15;

export async function GET() {
  try {
    const data = await getDashboardData();
    return NextResponse.json(data);
  } catch (error) {
    return NextResponse.json(
      {
        message: "Failed to fetch market data.",
        detail: error instanceof Error ? error.message : "Unknown error"
      },
      { status: 500 }
    );
  }
}
