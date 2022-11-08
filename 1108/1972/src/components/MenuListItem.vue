<template>
  <div v-bind:class="menuListItemClassSet" v-on:click="selectMenu">
    <img class="menu-img" v-bind:src="menuName.image" alt="수경짱">
    <div class="menu-title">{{menuName.title}}</div>
    <div class="menu-price">{{menuName.price}}won</div>
  </div>
</template>




<script>


export default {
  name: 'MenuListItem',
  props:["menuName","menuListItemClassSet"],
  computed: {
    image(){
      return this.menu.image;
    }
  },
  methods:{
    selectMenu(){
      this.$emit("selectMenu",this.menuName.title)
    },
  },
}


</script>
<style scoped>
/* .menu-img, .menu-title, .menu-price{
  border: 1px solid black;
} */
.menu-list-item{
  display:flex;
  justify-content: space-between;
  padding:0 20px;
  border:1px solid grey;
  margin:10px;
  border-radius: 5px;
  height:50px;
}

.menu-img{
  height: 50px;
  width: 50px;
}
.menu-title,.menu-price{
  display:flex;
  justify-content: center;
  align-items: center;
}

.menu-list-item:hover{
  background-color: seagreen;
}

.selected {
  background-color: green;
}
</style>