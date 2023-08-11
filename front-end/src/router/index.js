import Vue from 'vue'
import VueRouter from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import LoginStart from '../components/Login.vue'
// import Timeline from '../components/Timeline.vue'
// import TimelineInbox from '../components/TimelineInbox.vue'
import BookPocket from '../components/BookPocket.vue'
import AddNewBook from '../components/AddNewBook.vue'
import Wordcloud from '../components/Wordcloud.vue'
// import Main from '../components/Main.vue'
// import App from '../components/App.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/login_start',
        name: 'LoginStart',
        component: LoginStart
      },
      {
        path: '',
        name: 'BookPocket',
        component: BookPocket
      },
      {
        path: 'BookPocket',
        name: 'BookPocket',
        component: BookPocket
      },
      {
        path: '/add_new_book',
        name: 'AddNewBook',
        component: AddNewBook
      },
      {
        path: '/wordcloud',
        name: 'Wordcloud',
        component: Wordcloud
      },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
