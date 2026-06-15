import { URL, fileURLToPath } from 'node:url'

import { defineConfig, loadEnv } from 'vite'
import vueDevTools from 'vite-plugin-vue-devtools'

import vue from '@vitejs/plugin-vue'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, fileURLToPath(new URL('..', import.meta.url)), '')

  return {
    plugins: [vue(), vueDevTools()],

    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },

    define: {
      __API_URL__: JSON.stringify(env.API_URL),
    },
  }
})
