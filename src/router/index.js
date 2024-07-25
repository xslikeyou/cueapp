import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import QuestionView from '../views/QuestionView.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/question',
    name: 'Question',
    component: QuestionView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;