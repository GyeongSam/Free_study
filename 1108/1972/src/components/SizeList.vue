<template>
  <div id="SizeList">
    <div>
      <h1>2. 사이즈를 고르세요.</h1>
      <ul>
        <li v-for="(size, idx) in sizeLists" v-bind:key="idx">
          <SizeListItem 
          v-bind:sizeListItemClassSet="sizeListItemClassSet[index]"
          v-on:selectSize="selectSize" 
          v-bind:sizeName="size" /></li>

      </ul>
    </div>
  </div>
</template>

<script>
import SizeListItem from './SizeListItem.vue'


export default {
  name: 'SizeList',
  components: {
    SizeListItem
  },
  computed:{
    sizeLists(){
      return this.$store.state.sizeList;
    }
  }
}
</script>

<style scoped>

h2 {
  margin-bottom:10px;
}

#size-list{
  margin:10px;
  padding:10px;
  border-radius:5px;
  background-color: white;
}

</style>