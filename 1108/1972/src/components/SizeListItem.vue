<template>
  <div class="size-list-item">
    <div class="size-item">
      <span>{{sizeName.name}}</span>
      <span>{{sizeName.price}}</span>
    </div>
  </div>
</template>

<script>


export default {
  name: 'MenuListItem',
  props: ["sizeName"],
}


</script>
<style scoped>
/* .menu-img, .menu-title, .menu-price{
  border: 1px solid black;
} */
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

</style>