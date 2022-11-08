<template>
  <div id="app">
    <header class="app-title">
      <h1>Coffe order App</h1>
    </header>
    <main class="meun-size-wrapper">
      <section class="menu-list">
        <MenuList />
      </section>
      <section class="size-list">
        <SizeList />
      </section>
    </main>
    <section class="cart-btn-wrapper">
      <button class="cart-btn">장바구니 담기</button>
    </section>

  </div>
</template>

<script>
import MenuList from './components/MenuList.vue'
import SizeList from './components/SizeList.vue'
export default {
  name: 'App',
  components: {
    MenuList,
    SizeList
  },
}


</script>


<style>
*{
  padding: 0;
  margin: 0;
}

ul{
  list-style: none;
}

.app-title {
  text-align: center;
}
.meun-size-wrapper{
  display: grid;
  grid-template-columns: 1fr 1fr;
  background-color: rgb(199, 199, 199);
  border-radius: 5px;
  padding:10px;
}
.menu-list, .size-list{
  border: 1px solid black;
  background-color: white;
  border-radius: 5px;
}
.menu-list{
  margin-right:10px;
}
.size-list{
  margin-left:10px;
}
.cart-btn{
  display:block;
  width:100%;
  color:white;
  background-color: seagreen;
  border-radius: 5px;
  height: 70px;
  font-size:1.5rem;
  margin-top:10px;
}
</style>