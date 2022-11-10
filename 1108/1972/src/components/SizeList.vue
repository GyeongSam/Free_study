<template>
  <div id="SizeList">
    <div>
      <h1>2. 사이즈를 고르세요.</h1>
      <ul>
        <li v-for="(size, index) in sizeLists" v-bind:key="index">
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
  },
  data() {
    return {
      sizeListItemClassSet: [],
      length: -1,
    };
  },
  created() {
    this.length = this.$store.state.sizeList.length;
    for (let i = 0; i < this.length; i++) {
      this.sizeListItemClassSet.push(["size-item"]);
    }
  },
  methods: {
    selectSize(name) {
      const idx = this.$store.state.sizeList.findIndex((size) => {
        return size.nmae === name;
      });
      for (let i = 0; i < this.length; i++) {
        if (i === idx) {
          this.sizeListItemClassSet[i].push("selected");
          this.$store.dispatch(
            "updateSizeList",
            this.$store.state.sizeList[idx]
          );
        } else {
          this.sizeListItemClassSet[i].splice(1);
        }
      }
      console.log(this.$store.state.sizeList);
    },
  },
};
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