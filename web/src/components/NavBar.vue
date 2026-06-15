<script setup lang="ts">
import { RouterLink } from 'vue-router'

import { useLocaleStore } from '@/stores/locale'
import { useThemeStore } from '@/stores/theme'

const localeStore = useLocaleStore()
const themeStore = useThemeStore()
</script>

<template>
  <header class="is-fixed-above-lg">
    <div class="container">
      <nav>
        <ul>
          <li>
            <strong><RouterLink to="/" class="contrast">Astrosky Web</RouterLink></strong>
          </li>
        </ul>
        <ul>
          <li>
            <details class="dropdown">
              <summary role="button" class="outline contrast">
                <i class="pi pi-language pico-color-cyan-500" />
              </summary>
              <ul dir="rtl">
                <li>
                  <a
                    href="#"
                    :aria-current="localeStore.locale === 'en' ? 'page' : undefined"
                    @click="localeStore.setLocale('en')"
                  >
                    🇺🇸 English
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    :aria-current="localeStore.locale === 'uk' ? 'page' : undefined"
                    @click="localeStore.setLocale('uk')"
                  >
                    🇺🇦 Українська
                  </a>
                </li>
              </ul>
            </details>
          </li>
          <li>
            <details class="dropdown">
              <summary role="button" class="outline contrast">
                <i
                  class="pi pi-palette"
                  :class="{
                    'pico-color-purple-600':
                      themeStore.theme === 'dark' && !themeStore.isSystemTheme,
                    'pico-color-yellow-100':
                      themeStore.theme === 'light' && !themeStore.isSystemTheme,
                    'pico-color-green-500': themeStore.isSystemTheme,
                  }"
                />
              </summary>
              <ul dir="rtl">
                <li>
                  <a
                    class="icon-text"
                    href="#"
                    dir="ltr"
                    :aria-current="themeStore.isSystemTheme ? 'page' : undefined"
                    @click="themeStore.setTheme('system')"
                  >
                    <i class="pi pi-desktop pico-color-green-500" />
                    {{ $t('nav.systemTheme') }}
                  </a>
                </li>
                <li>
                  <a
                    class="icon-text"
                    href="#"
                    dir="ltr"
                    :aria-current="themeStore.theme === 'dark' ? 'page' : undefined"
                    @click="themeStore.setTheme('dark')"
                  >
                    <i class="pi pi-moon pico-color-purple-600" />
                    {{ $t('nav.darkTheme') }}
                  </a>
                </li>
                <li>
                  <a
                    class="icon-text"
                    href="#"
                    dir="ltr"
                    :aria-current="themeStore.theme === 'light' ? 'page' : undefined"
                    @click="themeStore.setTheme('light')"
                  >
                    <i class="pi pi-sun pico-color-yellow-100" />
                    {{ $t('nav.lightTheme') }}
                  </a>
                </li>
              </ul>
            </details>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>
