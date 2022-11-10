<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <button v-on:click="moveToHome">Home</button>
    <button v-on:click="moveToStart">Start</button>
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    moveToHome() {
      if (this.$route.path !== "/") {
        this.$router.push("/");
      }
    },
    moveToStart() {
      if (this.$route.path !== "/nocolor") {
        this.$router.push("/nocolor");
      }
    },
  },
};
</script>
