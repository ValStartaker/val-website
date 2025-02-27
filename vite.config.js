import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  server: {
    proxy: {
      // Forward /generate-parliament to Flask server
      '/generate-parliament': {
        target: 'http://localhost:5000', // Flask's default port
        changeOrigin: true
      }
    }
  },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        parliament: resolve(__dirname, 'parliament.html'),
        parliament_doc: resolve(__dirname, 'parliament_doc.html')
      }
    },
    assetsDir: 'assets',
    // This ensures CSS is properly handled during build
    cssCodeSplit: true
  }
}) 