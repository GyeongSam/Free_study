<template>
  <div id="app">
    <h1>App</h1>
    {{ appData }}
    <ChildComp
      v-bind:child-data="childData"
      v-bind:child-data2="childData2"
      v-bind:app-data="appData"
      v-bind:grand-child-data="grandChildData"
    />
  </div>
</template>

<script>
import ChildComp from "./components/ChildComp.vue";

export default {
  name: "App",
  components: {
    ChildComp,
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
