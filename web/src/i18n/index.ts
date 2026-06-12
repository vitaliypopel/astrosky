import { createI18n } from 'vue-i18n'

import en from '@/i18n/locales/en.json'
import uk from '@/i18n/locales/uk.json'
import type { MessageSchema } from '@/i18n/schema'

export const i18n = createI18n<[MessageSchema], 'en' | 'uk'>({
  legacy: false,
  locale: 'en',
  fallbackLocale: 'en',
  messages: {
    en,
    uk,
  },
})
