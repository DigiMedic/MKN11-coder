"use client"

import {
  Footer,
  FooterColumn,
  FooterBottom,
  FooterContent,
} from "@/components/ui/footer";
import SovadinaLogo from "@/components/logos/sovadina-logo";
import Link from "next/link";
import Image from "next/image"
import { Github, Linkedin } from "lucide-react"
import Balancer from "react-wrap-balancer"
import { Button } from "./ui/button"
import { PulsatingOutlineShadowButton } from "./ui/pulsating-button"

export default function FooterSection() {
  return (
    <footer className="bg-background py-8 sm:py-12 border-t border-border/5">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="flex flex-col gap-4 sm:gap-6">
            <Link href="/" className="inline-block">
              <SovadinaLogo className="h-8 w-auto transition-all hover:opacity-75" />
            </Link>
            <p className="max-w-xl text-muted-foreground">
              <Balancer>
                Asistované kódování diagnóz pomocí umělé inteligence
              </Balancer>
            </p>
            <div className="flex gap-2">
              <Button
                variant="outline"
                size="icon"
                className="border border-muted-foreground text-muted-foreground hover:border-primary hover:text-primary"
                asChild
              >
                <a
                  href="https://github.com/DigiMedic"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <Github className="h-5 w-5" />
                </a>
              </Button>
              <Button
                variant="outline"
                size="icon"
                className="border border-muted-foreground text-muted-foreground hover:border-primary hover:text-primary"
                asChild
              >
                <a
                  href="https://www.linkedin.com/in/petrsovadina"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <Linkedin className="h-5 w-5" />
                </a>
              </Button>
            </div>
          </div>

          <div className="flex flex-col justify-between items-end">
            <div className="flex flex-col items-end gap-2">
              <p className="text-muted-foreground text-sm text-right max-w-xs">
                Přečtěte si články na mém blogu a podívejte se na další projekty ze zdravotnictví
              </p>
              <PulsatingOutlineShadowButton asChild>
                <a
                  href="https://portfolio-sovadina.vercel.app/blog"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Přejít na blog
                </a>
              </PulsatingOutlineShadowButton>
            </div>
          </div>
        </div>
        <div className="border-border/30 mt-8 flex flex-col justify-between gap-6 border-t pt-6 md:flex-row md:items-center md:gap-2">
          <p className="mx-auto text-center text-muted-foreground">
            {new Date().getFullYear()} Petr Sovadina. Všechna práva vyhrazena
          </p>
        </div>
      </div>
    </footer>
  )
}
