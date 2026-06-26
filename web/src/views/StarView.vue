<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { getStar } from '@/api/star'
import type { Star } from '@/api/star/types'

const route = useRoute()

const star = ref<Star | null>(null)
const loading = ref(false)

const loadStar = async () => {
  loading.value = true

  try {
    const id = Number(route.params.id as string)
    star.value = await getStar(id)
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

onMounted(() => loadStar())
</script>

<template>
  <h3 align="center" aria-busy="true" v-if="loading">
    {{ $t('common.loading') }}
  </h3>
  <template v-else>
    <header>
      <h1>{{ star !== null ? star.names[0] : $t('star.title') }}</h1>
      <p v-if="star !== null && star.names.length > 1">
        {{ star.names.slice(1).join(', ') }}
      </p>
    </header>
    <template v-if="star !== null">
      <section>
        <article>
          <h3>{{ $t('common.information') }}</h3>
          <table>
            <tbody>
              <tr>
                <th>{{ $t('constellation.title') }}</th>
                <td>{{ star.con || $t('common.unknown') }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.ra') }}</th>
                <td>{{ star.ra !== null ? `${star.ra}°` : '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.dec') }}</th>
                <td>{{ star.dec !== null ? `${star.dec}°` : '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.bayer') }}</th>
                <td>{{ star.bayer || '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.flamseed') }}</th>
                <td>{{ star.flam !== null ? star.flam : '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.distance') }}</th>
                <td>{{ star.dist !== null ? `${star.dist} ${$t('units.pc')}` : '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.magnitude') }}</th>
                <td>{{ star.mag !== null ? star.mag : '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.absoluteMagnitude') }}</th>
                <td>{{ star.absmag !== null ? star.absmag : '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.spectralType') }}</th>
                <td>{{ star.spect || '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.colorIndex') }}</th>
                <td>{{ star.ci !== null ? star.ci : '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.radialVelocity') }}</th>
                <td>{{ star.rv !== null ? `${star.rv} ${$t('units.kmSec')}` : '-' }}</td>
              </tr>
              <tr>
                <th>{{ $t('properties.luminosity') }}</th>
                <td>{{ star.lum !== null ? star.lum : '-' }}</td>
              </tr>
            </tbody>
          </table>
        </article>
      </section>
    </template>
    <p v-else>
      {{ $t('star.empty.title') }}
    </p>
  </template>
</template>
