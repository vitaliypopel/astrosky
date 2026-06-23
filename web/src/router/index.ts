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
      path: '/catalogs',
      name: 'catalogs',
      component: () => import('@/views/CatalogsView.vue'),
    },
    {
      path: '/catalogs/:code',
      name: 'catalog',
      component: () => import('@/views/CatalogView.vue'),
    },
  ],
})

export default router
