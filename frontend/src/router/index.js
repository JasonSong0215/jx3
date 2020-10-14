import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/home',
    children: [{
      path: 'home',
      name: 'home',
      component: () => import('@/views/home/home'),
      meta: { title: 'jx3衍天宗计算器', icon: 'dashboard' }
    }]
  },
  {
    path: '/log',
    component: Layout,
    children: [{
      path: 'log',
      name: 'log',
      component: () => import('@/views/home/log'),
      meta: { title: '计算器说明', icon: 'people' }
    }]
  },
  {
    path: '/acc',
    component: Layout,
    children: [{
      path: 'acc',
      name: 'acc',
      component: () => import('@/views/home/acc'),
      meta: { title: '加速阈值', icon: 'education' }
    }]
  },
  {
    path: '/test',
    component: Layout,
    children: [{
      path: 'test',
      name: 'test',
      component: () => import('@/views/home/test'),
      meta: { title: '模块化测试', icon: 'bug' }
    }]
  },
  {
    path: '/pwd',
    component: Layout,
    hidden:true,
    children: [{
      path: 'pwd',
      name: 'pwd',
      component: () => import('@/views/home/pwd'),
      meta: { title: '密码簿', icon: 'education' }
    }]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
