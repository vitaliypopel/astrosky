import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue'),
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: () => import('@/views/CatalogView.vue'),
    },
    {
      path: '/constellations',
      name: 'constellations',
      component: () => import('@/views/ConstellationsView.vue'),
    },
    {
      path: '/constellations/:id',
      name: 'constellation',
      component: () => import('@/views/ConstellationView.vue'),
    },
    {
      path: '/stars',
      name: 'stars',
      component: () => import('@/views/StarsView.vue'),
    },
    {
      path: '/stars/:id',
      name: 'star',
      component: () => import('@/views/StarView.vue'),
    },
  ],
})

export default router
