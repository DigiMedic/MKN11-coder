/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  images: {
    unoptimized: true,
  },
  // Nastavení basePath pro produkci
  basePath: '',
  // Nastavení assetPrefix pro produkci
  assetPrefix: process.env.NEXT_PUBLIC_URL || '',
  // Povolení CORS pro API
  async headers() {
    return [
      {
        source: '/api/:path*',
        headers: [
          { key: 'Access-Control-Allow-Origin', value: '*' },
          { key: 'Access-Control-Allow-Methods', value: 'GET,POST,OPTIONS' },
          { key: 'Access-Control-Allow-Headers', value: '*' },
        ],
      },
    ]
  },
  // Přesměrování API požadavků
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: process.env.NEXT_PUBLIC_BACKEND_URL ? 
          `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/:path*` : 
          'http://backend:8000/api/:path*',
      },
    ]
  },
}

module.exports = nextConfig
