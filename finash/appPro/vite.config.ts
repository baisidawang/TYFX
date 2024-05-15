import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/

// export default defineConfig({
//   plugins: [
//     vue(),
//   ],
//   server: {
//     proxy: {
//       '/query': {
//         target: 'http://127.0.0.1:8000', // 后端API的地址
//         changeOrigin: true,
//         rewrite: (path) => path
//       }
//     }
//   },
//   resolve: {
//     alias: {
//       '@': fileURLToPath(new URL('./src', import.meta.url))
//     }
//   }
// });
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
