<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { RouterLink } from 'vue-router'

import { getConstellations } from '@/api/constellation'
import type { Constellation } from '@/api/constellation/types'

const constellations = ref<Constellation[]>([])
const loading = ref(false)

const loadConstellations = async () => {
  loading.value = true

  try {
    constellations.value = await getConstellations()
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

onMounted(() => loadConstellations())
</script>

<template>
  <header>
    <h1>{{ $t('constellations.title') }}</h1>
    <p>{{ $t('constellations.subtitle') }}</p>
  </header>
  <p align="center" aria-busy="true" v-if="loading">
    {{ $t('common.loading') }}
  </p>
  <section v-else-if="constellations.length">
    <article v-for="constellation in constellations">
      <header>
        <h3 class="m-0 p-0">
          <RouterLink :to="`/constellations/${constellation.id}`" class="contrast">
            {{ constellation.name }}
          </RouterLink>
        </h3>
      </header>
      <table>
        <tbody>
          <tr>
            <th>{{ $t('common.code') }}</th>
            <td>{{ constellation.code }}</td>
          </tr>
          <tr>
            <th>{{ $t('properties.area') }}</th>
            <td>{{ constellation.area }}</td>
          </tr>
          <tr>
            <th>{{ $t('properties.areaPercent') }}</th>
            <td>{{ constellation.area_pct }}</td>
          </tr>
        </tbody>
      </table>
    </article>
  </section>
  <p v-else>
    {{ $t('constellations.empty.title') }}
  </p>
</template>
