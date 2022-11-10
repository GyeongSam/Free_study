// App.vue

<template>
  <div id="app">
    <p>Counter: {{ $store.state.counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  data: function() {
    return {
      counter: 0,
    }
  },
  methods: {
    increase(){
      this.$store.dispatch('change_cnt',1)
    },
    decrease(){
      this.$store.dispatch('change_cnt',-1)
    }
  },
  computed: {
    counterDouble: function () {
      return this.$store.state.counter * 2
    },
  },
}
</script>

<style>
</style>