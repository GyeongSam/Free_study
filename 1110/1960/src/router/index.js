import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import NoPageView from "../views/NoPageView.vue";
import NocolorView from "../views/NocolorView.vue";
import SsaleafView from "../views/SsaleafView.vue";
import SsaflowerView from "../views/SsaflowerView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/nocolor",
    name: "Nocolor",
    component: NocolorView,
  },
  {
    path: "/nopage",
    name: "NoPage",
    component: NoPageView,
  },
  {
    path: "/ssaleaf",
    name: "Ssaleaf",
    component: SsaleafView,
  },
  {
    path: "/ssaflower",
    name: "Ssaflower",
    component: SsaflowerView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  to.name ? next() : next({ name: "NoPage" });
});

export default router;
