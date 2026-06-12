import '@/assets/main.scss'

import { createPinia } from 'pinia'
import { createApp } from 'vue'

import { i18n } from '@/i18n'
import router from '@/router'
import { useLocaleStore } from '@/stores/locale'
import { useThemeStore } from '@/stores/theme'

import App from '@/App.vue'

const app = createApp(App)
const pinia = createPinia()

app.use(i18n)
app.use(pinia)
app.use(router)

const localeStore = useLocaleStore()
const themeStore = useThemeStore()

localeStore.initLocale()
themeStore.initTheme()

app.mount('#app')
