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
          <RouterLink to="/catalog" class="contrast">
            {{ $t('catalog.title') }}
          </RouterLink>
        </h3>
      </header>
      {{ $t('catalog.subtitle') }}
    </article>
  </section>
</template>
