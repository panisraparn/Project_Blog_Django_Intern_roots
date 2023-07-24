import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import FeedView from '../views/FeedView.vue'
import MessageView from '../views/MessageView.vue'
import searchView from '../views/SearchView.vue'
import ProfileView from '../views/ProfileView.vue'
import DeleteView from '../views/DeleteView.vue'

import BlogView from '../views/Blog.vue'
import testView from '../views/testView.vue'
import showBlogView from '../views/showBlog.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/feed',
      name: 'feed',
      component: FeedView
    },
    {
      path: '/message',
      name: 'message',
      component: MessageView
    },
    {
      path: '/search',
      name: 'search',
      component: searchView
    },
    {
      path: '/blog',
      name: 'blog',
      component: BlogView,
      children: [
        {
          path: '/blog/record/:id',
          name: 'show',
          component: showBlogView
        }
      ]
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/delete/:id',
      name: 'delete',
      component: DeleteView
    },
    {
      path: '/test',
      name: 'test',
      component: testView
    },
    


  ]
})

export default router
