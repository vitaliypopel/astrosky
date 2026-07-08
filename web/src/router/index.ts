import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/general/HomeView.vue'),
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: () => import('@/views/catalog/CatalogView.vue'),
    },
    {
      path: '/constellations',
      name: 'constellations',
      component: () => import('@/views/catalog/ConstellationsView.vue'),
    },
    {
      path: '/constellations/:id',
      name: 'constellation',
      component: () => import('@/views/catalog/ConstellationView.vue'),
    },
    {
      path: '/stars',
      name: 'stars',
      component: () => import('@/views/catalog/StarsView.vue'),
    },
    {
      path: '/stars/:id',
      name: 'star',
      component: () => import('@/views/catalog/StarView.vue'),
    },
    {
      path: '/observation',
      name: 'observation',
      component: () => import('@/views/observation/ObservationView.vue'),
    },
  ],
})

export default router
