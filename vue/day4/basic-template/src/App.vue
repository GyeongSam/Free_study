<template>
  <div id="app">
    <h1>App</h1>

  </div>
</template>

<script>
import ChildComp from "./components/ChildComp.vue"
export default {
  name: "App",
  components: {
    ChildComp
  },
  data() {
    return {
      appData: "App 데이터",
      childData: "Child 데이터",
      childData2: "Child 데이터2222",
      grandChildData: "GrandChild 데이터",
    };
  },
};
</script>

<style>
</style>
