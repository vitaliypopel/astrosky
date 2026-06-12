import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export type Theme = 'system' | 'dark' | 'light'
export type ResolvedTheme = Exclude<Theme, 'system'>

const storageKey = 'theme'

const getSystemTheme = (): ResolvedTheme =>
  window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'

const resolveTheme = (theme: Theme): ResolvedTheme =>
  theme === 'system' ? getSystemTheme() : theme

export const useThemeStore = defineStore('theme', () => {
  const theme = ref<Theme>('system')

  const isSystemTheme = computed<boolean>(() => theme.value === 'system')

  const resolvedTheme = computed<ResolvedTheme>(() => resolveTheme(theme.value))

  const setTheme = (newTheme: Theme) => {
    theme.value = newTheme
    localStorage.setItem(storageKey, newTheme)
    document.documentElement.setAttribute('data-theme', resolveTheme(newTheme))
  }

  const initTheme = () => {
    const savedTheme = localStorage.getItem(storageKey) as Theme

    if (['system', 'dark', 'light'].includes(savedTheme)) {
      setTheme(savedTheme)
      return
    }

    setTheme('system')
  }

  return { theme, isSystemTheme, resolvedTheme, setTheme, initTheme }
})
