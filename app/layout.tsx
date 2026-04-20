import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "CryptoLens | 虚拟货币分析平台",
  description: "基于 Next.js 的虚拟货币分析平台，集成实时行情、核心指标与 AI 方向判断。"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
