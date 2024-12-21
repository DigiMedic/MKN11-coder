# Build stage
FROM node:20-alpine AS builder

WORKDIR /app

# Kopírování package souborů
COPY package*.json ./
RUN npm ci
RUN npm install sharp

# Kopírování zdrojových souborů
COPY . .

# Build aplikace
ENV NEXT_TELEMETRY_DISABLED 1
RUN npm run build

# Production stage
FROM node:20-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED 1
ENV NEXT_PUBLIC_API_URL=http://backend:8000  # Interní URL backendu

# Vytvoření neprivilegovaného uživatele
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs && \
    chown -R nextjs:nodejs /app

# Kopírování buildu a potřebných souborů
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT=3000
ENV HOSTNAME=0.0.0.0

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -q --spider http://localhost:3000 || exit 1

CMD ["npm", "run", "start", "--", "--port", "3000"]
