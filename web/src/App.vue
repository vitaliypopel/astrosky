<script setup lang="ts">
import { RouterView } from 'vue-router'

import ContainerLayout from '@/components/ContainerLayout.vue'
import NavBar from '@/components/NavBar.vue'
</script>

<template>
  <NavBar />
  <ContainerLayout>
    <RouterView />
  </ContainerLayout>
</template>
