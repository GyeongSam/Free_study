<template>
  <div id="app">
    <h1>Hello!!!!</h1>
    <img v-bind:src="catUrl" alt="dfsaf" height="500"/>
    <button v-on:click="getCat">get cat</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      catUrl: "",
    };
  },
  created() {
    this.getCat();
  },
  methods: {
    async getCat() {
      try{
        const url = "https://api.thecatapi.com/v1/images/search";
        const response = await axios.get(url);
        if (response.data){
          this.catUrl = response.data[0].url;
        }
      } catch (error){
        console.log(error);
      }
    }
  }
}
</script>

<style>
</style>
