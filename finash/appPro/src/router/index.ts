import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login.vue'
import index from '../views/HomeView.vue'
import Table from '../views/Table.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/index',
      name: 'index',
      component: index,
      children:[
        {
          path:'/table',
        component: Table
      }
      ]
    }
    
  
  ]
})

export default router
