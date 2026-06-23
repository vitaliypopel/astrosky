<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { RouterLink } from 'vue-router'

import { getCatalogs } from '@/api/catalog'
import type { Catalog } from '@/api/catalog/types'

const catalogs = ref<Catalog[]>([])
const loading = ref(false)

const loadCatalogs = async () => {
  loading.value = true

  try {
    catalogs.value = await getCatalogs()
  } catch (error) {
    if (error instanceof Error) {
      alert(error.message)
      return
    }
    alert('Unknown error')
  } finally {
    loading.value = false
  }
}

onMounted(() => loadCatalogs())
</script>

<template>
  <header>
    <h1>{{ $t('catalogs.title') }}</h1>
    <p>{{ $t('catalogs.subtitle') }}</p>
  </header>
  <p align="center" aria-busy="true" v-if="loading">
    {{ $t('common.loading') }}
  </p>
  <section class="grid" v-else-if="catalogs.length">
    <article v-for="catalog in catalogs">
      <header>
        <h3 class="m-0 p-0">
          <RouterLink :to="`/catalogs/${catalog.code}`" class="contrast">
            {{ catalog.name }}
          </RouterLink>
        </h3>
      </header>
      <p>
        {{ catalog.description }}
      </p>
      <table>
        <tbody>
          <tr>
            <th>{{ $t('common.code') }}</th>
            <td>{{ catalog.code }}</td>
          </tr>
          <tr>
            <th>{{ $t('catalog.stats.starsCount') }}</th>
            <td>{{ catalog.stars_count }}</td>
          </tr>
          <tr>
            <th>{{ $t('catalog.stats.namedStarsCount') }}</th>
            <td>{{ catalog.named_stars_count }}</td>
          </tr>
        </tbody>
      </table>
    </article>
  </section>
  <p v-else>
    {{ $t('catalogs.empty.title') }}
  </p>
</template>
