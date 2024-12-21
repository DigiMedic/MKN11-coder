# Build stage
FROM node:20-alpine

WORKDIR /app

# Instalace závislostí
COPY package*.json ./
RUN npm ci

# Nastavení pro development
ENV NODE_ENV=development
ENV NEXT_TELEMETRY_DISABLED=1

# Kopírování zdrojových souborů
COPY . .

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -q --spider http://localhost:3000 || exit 1

# Spuštění v development módu
CMD ["npm", "run", "dev"]
