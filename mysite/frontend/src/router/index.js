import Vue from 'vue'
import Router from 'vue-router'
import pageData from '@/components/pageData'
import login from '@/components/login'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'pageData',
      component: pageData,
      meta: {
        requireAuth: true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
})
