import Vue from 'vue'
import VueRouter from 'vue-router'

// 로그인전 홈페이지
import Home from '@/Home.vue'

// 회원가입, 로그인
import Join from '../views/Join.vue'
import Login from '../views/Login.vue'

// 헤더
import Header from '../components/Header.vue'

// 추천
import Suggest from '../components/Suggest'

// 메인페이지 관련
import Main from '../views/Main.vue'
import Calendar from '../components/Calendar.vue'
import CalendarDay from '@/components/CalendarDay.vue'
import Myinfo from '../components/Myinfo.vue'
import Today from '../components/Today.vue'
import PasswordConfirm from '../components/PasswordConfirm.vue'

// 커뮤니티
import Community from '../views/community/Community.vue'
import CreateCommunity from '../views/community/CreateCommunity.vue'
import CommunityDetail from '../views/community/CommunityDetail'
import UpdateCommunity from '../views/community/UpdateCommunity.vue'

// 검색페이지 관련
import FoodSearch from '@/views/food/foodSearch.vue'
// import { component } from 'vue/types/umd'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/user/join',
    name: 'join',
    component: Join
  },
  {
    path: '/user/login',
    name: 'login',
    component: Login
  },
  {
    path: '/header',
    name: 'Header',
    component: Header
  },
  {
    path: '/main',
    name: 'Main',
    component: Main
  },
  {
    path: '/calendar',
    name: 'Calendar',
    component: Calendar
  },
  {
    path: '/calendarday',
    name: 'CalendarDay',
    component: CalendarDay
  },
  {
    path: '/today',
    name: 'Today',
    component: Today
  },
  {
    path: '/myinfo',
    name: 'Myinfo',
    component: Myinfo
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/createcommunity',
    name: 'CreateCommunity',
    component: CreateCommunity
  },
  {
    path: '/communitydetail',
    name: 'CommunityDetail',
    component: CommunityDetail
  },
  {
    path: '/updatecommunity',
    name: 'UpdateCommunity',
    component: UpdateCommunity,
    props: true,
  },
  {
    path: '/foodsearch',
    name: 'FoodSearch',
    component: FoodSearch
  },
  {
    path: '/passwordconfirm',
    name: 'PasswordConfirm',
    component: PasswordConfirm
  },
  {
    path: '/suggest',
    name: 'Suggest',
    component: Suggest
  },
]

let router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
