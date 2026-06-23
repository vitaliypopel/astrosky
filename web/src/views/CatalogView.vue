<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { getCatalog } from '@/api/catalog'
import type { Catalog } from '@/api/catalog/types'

const route = useRoute()

const catalog = ref<Catalog | null>(null)
const loading = ref(false)

const loadCatalog = async () => {
  loading.value = true

  try {
    const code = route.params.code as string
    catalog.value = await getCatalog(code)
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

onMounted(() => loadCatalog())
</script>

<template>
  <h3 align="center" aria-busy="true" v-if="loading">
    {{ $t('common.loading') }}
  </h3>
  <template v-else>
    <header>
      <h1>{{ catalog !== null ? catalog.name : $t('catalog.title') }}</h1>
    </header>
    <section class="grid" v-if="catalog !== null">
      <article>
        <h3>{{ $t('common.description') }}</h3>
        <p>{{ catalog.description }}</p>
      </article>
      <article>
        <h3>{{ $t('common.information') }}</h3>
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
            <tr>
              <th>{{ $t('common.created') }}</th>
              <td>{{ catalog.created_at.slice(0, catalog.created_at.indexOf('T')) }}</td>
            </tr>
            <tr>
              <th>{{ $t('common.updated') }}</th>
              <td>{{ catalog.updated_at.slice(0, catalog.created_at.indexOf('T')) }}</td>
            </tr>
          </tbody>
        </table>
      </article>
    </section>
    <p v-else>
      {{ $t('catalog.empty.title') }}
    </p>
  </template>
</template>
