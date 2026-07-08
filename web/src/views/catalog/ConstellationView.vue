<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { getConstellation } from '@/api/constellation'
import type { Constellation } from '@/api/constellation/types'

const route = useRoute()

const constellation = ref<Constellation | null>(null)
const loading = ref(false)

const loadConstellation = async () => {
  loading.value = true

  try {
    const id = Number(route.params.id as string)
    constellation.value = await getConstellation(id)
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

onMounted(() => loadConstellation())
</script>

<template>
  <h3 align="center" aria-busy="true" v-if="loading">
    {{ $t('common.loading') }}
  </h3>
  <template v-else>
    <header>
      <h1>{{ constellation !== null ? constellation.name : $t('constellation.title') }}</h1>
    </header>
    <template v-if="constellation !== null">
      <section>
        <article>
          <h3>{{ $t('common.information') }}</h3>
          <table>
            <tbody>
              <tr>
                <th>{{ $t('common.code') }}</th>
                <td>{{ constellation.code }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.ra') }}</th>
                <td>{{ constellation.ra }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.dec') }}</th>
                <td>{{ constellation.dec }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.area') }}</th>
                <td>{{ constellation.area }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.areaPercent') }}</th>
                <td>{{ constellation.area_pct }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.season') }}</th>
                <td>{{ constellation.season }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.equatorialZone') }}</th>
                <td>{{ constellation.eq }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.eclipticZone') }}</th>
                <td>{{ constellation.ecl }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.milkyWayZone') }}</th>
                <td>{{ constellation.mw }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.quadrant') }}</th>
                <td>{{ constellation.quad }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.nameOrigin') }}</th>
                <td>{{ constellation.origin }}</td>
              </tr>
            </tbody>
          </table>
        </article>
      </section>
    </template>
    <p v-else>
      {{ $t('constellation.empty.title') }}
    </p>
  </template>
</template>
