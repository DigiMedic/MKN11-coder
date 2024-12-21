import Image from "next/image";
import { cn } from "@/lib/utils";

interface SovadinaLogoProps {
  className?: string;
}

export default function SovadinaLogo({ className }: SovadinaLogoProps) {
  return (
    <>
      <Image
        src="/sovadina.dev - white -long2-logo.png"
        alt="Sovadina Logo"
        width={240}
        height={80}
        className={cn("object-contain hidden dark:block", className)}
        priority
      />
      <Image
        src="/sovadina.dev.png"
        alt="Sovadina Logo"
        width={240}
        height={80}
        className={cn("object-contain dark:hidden", className)}
        priority
      />
    </>
  );
}
