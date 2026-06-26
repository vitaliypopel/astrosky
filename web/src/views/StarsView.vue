<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import { getStars } from '@/api/star'
import type { Star } from '@/api/star/types'

const route = useRoute()
const router = useRouter()

const stars = ref<Star[]>([])
const loading = ref(false)

const nextUrl = ref<string | null>(null)
const previousUrl = ref<string | null>(null)

const page = computed(() => {
  const value = Number(route.query.page)

  return Number.isInteger(value) && value > 0 ? value : 1
})

const getPageFromUrl = (url: string | null): number | null => {
  if (!url) {
    return null
  }

  const value = Number(new URL(url).searchParams.get('page'))

  return Number.isInteger(value) && value > 0 ? value : 1
}

const nextPage = computed(() => getPageFromUrl(nextUrl.value))
const previousPage = computed(() => getPageFromUrl(previousUrl.value))

const setPage = async (page: number) => {
  const query = { ...route.query }

  if (page === 1) {
    delete query.page
  } else {
    query.page = String(page)
  }

  await router.push({ query })
}

const loadStars = async () => {
  loading.value = true

  try {
    const data = await getStars({ page: page.value })

    stars.value = data.results
    nextUrl.value = data.next
    previousUrl.value = data.previous
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

watch(
  () => route.query.page,
  () => loadStars(),
  { immediate: true },
)
</script>

<template>
  <header>
    <h1>{{ $t('stars.title') }}</h1>
    <p>{{ $t('stars.subtitle') }}</p>
  </header>
  <p align="center" aria-busy="true" v-if="loading">
    {{ $t('common.loading') }}
  </p>
  <template v-else-if="stars.length">
    <section v-for="star in stars">
      <article>
        <header>
          <h3 class="m-0 p-0">
            <RouterLink :to="`/stars/${star.id}`" class="contrast">
              {{ star.names[0] }}
            </RouterLink>
          </h3>
          <p class="m-0 p-0" v-if="star.names.length > 1">
            {{ star.names.slice(1).join(', ') }}
          </p>
        </header>
        <table>
          <tbody>
            <tr>
              <th>{{ $t('constellation.title') }}</th>
              <td>{{ star.con || $t('common.unknown') }}</td>
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
              <th>{{ $t('properties.spectralType') }}</th>
              <td>{{ star.spect || '-' }}</td>
            </tr>
          </tbody>
        </table>
      </article>
    </section>
    <section class="grid">
      <button class="outline contrast" @click="setPage(previousPage)" v-if="previousPage !== null">
        {{ $t('nav.previous') }}
      </button>
      <button class="outline contrast" @click="setPage(nextPage)" v-if="nextPage !== null">
        {{ $t('nav.next') }}
      </button>
    </section>
  </template>
  <p v-else>
    {{ $t('stars.empty.title') }}
  </p>
</template>
