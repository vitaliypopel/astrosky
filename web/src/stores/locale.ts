import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Composer } from 'vue-i18n'

import { i18n } from '@/i18n'

export type Locale = 'en' | 'uk'

const storageKey = 'locale'

export const useLocaleStore = defineStore('locale', () => {
  const locale = ref<Locale>('en')

  const setLocale = (newLocale: Locale) => {
    locale.value = newLocale
    localStorage.setItem(storageKey, newLocale)
    document.documentElement.setAttribute('lang', newLocale)

    const composer = i18n.global as unknown as Composer
    composer.locale.value = newLocale
  }

  const initLocale = () => {
    const savedLocale = localStorage.getItem(storageKey) as Locale

    if (['en', 'uk'].includes(savedLocale)) {
      setLocale(savedLocale)
      return
    }

    setLocale('en')
  }

  return { locale, setLocale, initLocale }
})
