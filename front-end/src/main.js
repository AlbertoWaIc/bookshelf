import Vue from 'vue'
import App from './components/App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

const app = new Vue({
  router,
  store,
  vuetify,
  components: { App },
  template: "<App/>",
  render: h => h(App)
}).$mount('#app')

export default app;
