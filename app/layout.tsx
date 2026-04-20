import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "CryptoLens | 虚拟货币分析平台",
  description: "基于 Next.js 的虚拟货币分析网站，集成实时行情、指数分析和 AI 方向判断。"
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
