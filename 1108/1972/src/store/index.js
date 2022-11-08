import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: "아메리카노",
        price: 3000,
        selected: false,
        image: "https://source.unsplash.com/featured/?americano",
      },
      {
        title: "카페라떼",
        price: 3500,
        selected: false,
        image: "https://source.unsplash.com/featured/?latte",
      },
      {
        title: "아이스티",
        price: 5000,
        selected: false,
        image: "https://source.unsplash.com/featured/?icetea",
      },
    ],
    sizeList: [
      {
        name: "소짜",
        price: 500,
        selected: false,
      },
      {
        name: "중짜",
        price: 1000,
        selected: false,
      },
      {
        name: "대짜",
        price: 1500,
        selected: false,
      },
      {
        name: "특",
        price: 2000,
        selected: false,
      },
    ],
  },
  mutations: {
    CHANGE_ORDER_LIST(state, newOrderList) {
      state.orderList = newOrderList;
    },
    CHANGE_MENU_LIST(state, newMenuList) {
      state.menuList = newMenuList;
    },
    CHANGE_SIZE_LIST(state, newSizeList) {
      state.sizeList = newSizeList;
    },
  },
  actions: {
    addOrder(context) {
      const menu = context.state.menuList.find(
        (menu) => menu.selected === true
      );
      const size = context.state.sizeList.find(
        (size) => size.selected === true
      );
      const order = {
        menu: menu,
        size: size,
      };
      const newOrderList = context.state.orderList;
      newOrderList.push(order);
      context.commit("CHANGE_ORDER_LIST", newOrderList);
    },
    updateMenuList(context, selectedMenu) {
      const newMenuList = context.state.menuList.map((menu) => {
        if (menu.title === selectedMenu.title) {
          menu.selected = true;
        } else {
          menu.selected = false;
        }
        return menu;
      });
      context.commit("CHANGE_MENU_LIST", newMenuList);
    },
    updateSizeList(context, selectedSize) {
      const newSizeList = context.state.sizeList.map((size) => {
        if (size.name === selectedSize.name) {
          size.selected = true;
        } else {
          size.selected = false;
        }
        return size;
      });
      context.commit("CHANGE_SIZE_LIST", newSizeList);
    },
  },
});