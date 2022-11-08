<template>
  <div id="MenuList">
    <div>
      <h1>1. 음료를 고르세요.</h1>
      <ul>
        <li v-for="(menu, index) in menuList" v-bind:key="index">
          <MenuListItem 
          v-bind:menuName="menu" 
          v-bind:menuListItemClassSet="menuListItemClassSet[index]"
          v-on:selectMenu="selectMenu" />
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import MenuListItem from "./MenuListItem.vue";
export default {
  components: {
    MenuListItem,
  },
  data() {
    return {
      menuListItemClassSet: [],
      length: -1,
    };
  },
  created() {
    this.length = this.$store.state.menuList.length;
    for (let i = 0; i < this.length; i++) {
      this.menuListItemClassSet.push(["menu-list-item"]);
    }
  },
  computed: {
    menuList() {
      return this.$store.state.menuList;
    },
  },
  methods: {
    selectMenu(title) {
      const idx = this.$store.state.menuList.findIndex((menu) => {
        return menu.title === title;
      });
      for (let i = 0; i < this.length; i++) {
        if (i === idx) {
          this.menuListItemClassSet[i].push("selected");
          this.$store.dispatch(
            "updateMenuList",
            this.$store.state.menuList[idx]
          );
        } else {
          this.menuListItemClassSet[i].splice(1);
        }
      }
      console.log(this.$store.state.menuList);
    },
  },
};
</script>

<style scoped>
h2 {
  margin-bottom: 10px;
}

#menu-list {
  margin: 10px;
  padding: 10px;
  border-radius: 5px;
  background-color: white;
}
</style>