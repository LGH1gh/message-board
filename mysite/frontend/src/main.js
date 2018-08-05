// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import 'bootstrap-vue'
import feather from 'vue-icon'

Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.use(feather, 'v-icon')
/* eslint-disable no-new */

router.beforeEach((to, from, next) => {
  if (to.path === '/login') {
    sessionStorage.removeItem('user')
  }
  let user = sessionStorage.getItem('user')
  if (!user && (to.path === '/')) {
    next({path: '/login'})
  } else {
    next()
  }
})

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
