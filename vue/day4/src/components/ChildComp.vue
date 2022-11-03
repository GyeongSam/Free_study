<template>
  <div class="child-comp">
    <h2>ChildComp</h2>
    <div>
      {{ childData }}
    </div>
    <div>
      {{ childData2 }}
    </div>

    <GrandChild
      v-bind:app-data="appData"
      v-bind:grand-child-data="grandChildData"
    />
  </div>
</template>

<script>
import GrandChild from "./GrandChild.vue";
export default {
  components: { GrandChild },
  name: "ChildComp",
  props: ["childData", "childData2", "appData", "grandChildData"],
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
</style>
