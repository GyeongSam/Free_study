<template>
    <div v-bind:class="sizeListItemClassSet" v-on:click="selectSize">
    <span>{{sizeName.name}}</span>
    <span>{{sizeName.price}}</span>

</div>
</template>

<script>


export default {
  name: 'SizeListItem',
  props: ["sizeName","sizeListItemClassSet"],
  methods:{
    selectSize(){
      this.$emit("selectSize",this.sizeName.name)
    },
  },
  
}


</script>
<style scoped>

.size-item{
  display:flex;
  justify-content: space-between;
  padding:0 10px;
  border:1px solid grey;
  margin:10px;
  border-radius: 5px;
  height:50px;
  align-items: center;
}

.size-item:hover{
  background-color: seagreen;
}
.selected {
  background-color: green;
}
</style>