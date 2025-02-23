import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    proxy: {
      // Forward /generate-parliament to Flask server
      '/generate-parliament': {
        target: 'http://localhost:5000', // Flask's default port
        changeOrigin: true
      }
    }
  }
}) 