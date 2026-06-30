<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <header>
    <h1>{{ $t('nav.home') }}</h1>
  </header>
  <section>
    <article>
      <header>
        <h3 class="m-0 p-0">
          <RouterLink to="/catalogs" class="contrast">
            {{ $t('catalogs.title') }}
          </RouterLink>
        </h3>
      </header>
      {{ $t('catalogs.subtitle') }}
    </article>
    <article>
      <header>
        <h3 class="m-0 p-0">
          <RouterLink to="/constellations" class="contrast">
            {{ $t('constellations.title') }}
          </RouterLink>
        </h3>
      </header>
      {{ $t('constellations.subtitle') }}
    </article>
    <article>
      <header>
        <h3 class="m-0 p-0">
          <RouterLink to="/stars" class="contrast">
            {{ $t('stars.title') }}
          </RouterLink>
        </h3>
      </header>
      {{ $t('stars.subtitle') }}
    </article>
  </section>
</template>
