<template>
  <div id="app">
    <h1>AppChild</h1>
    <input type="text" v-model="appChildInput" v-on:input="ChildInputToApp">
    <p>appData: {{appData}}</p>
    <p>appChildData: {{appChildData}}</p>
    <p>appParentData: {{appParentData}}</p>
  </div>
</template>

<script>
export default {
  data(){
    return {
      appChildInput:""
    }
  },
  props:['appData','appChildData','appParentData'],
  methods:{
    ChildInputToApp: function(){
      this.$emit('ChildInputToApp',this.appChildInput)
    }
  }
}
</script>

<style>
</style>