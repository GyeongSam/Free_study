<template>
  <div class="grand-child">
    <h3>GrandChild</h3>
    <div>GrandChild에서 받은 {{ appData }}</div>
    <div>드디어 받은 {{ grandChildData }}</div>
  </div>
</template>

<script>
export default {
  name: "GrandChild",
  props: ["appData", "grandChildData"],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
