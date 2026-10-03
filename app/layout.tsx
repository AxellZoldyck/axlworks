import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "Axlworks — Digital systems & experiments", description: "A creative software lab building digital systems, interfaces, and experiments." };
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}