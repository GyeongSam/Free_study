<template>
  <div id="app">
    <h1>AppParent</h1>
    <input type="text" v-model="appParentInput" v-on:input="ParentInputToApp" v-on:ChildInputToApp="ChildInputToApp">
    <p>appData: {{appData}}</p>
    <p>appChildData: {{appChildData}}</p>


    <AppChild :app-data="appData" :app-child-data="appChildData" :app-parent-data="appParentData"/>
  </div>
</template>

<script>
import AppChild from "./AppChild.vue"
export default {
  components:{
    AppChild
  },
  data(){
    return {
    appParentInput : "",
    }
  },
  props:['appData','appChildData','appParentData'],
  methods:{
    ParentInputToApp : function(){
      this.$emit('ParentInputToApp',this.appParentInput)
    },
    ChildInputToApp : function(childinput){
      this.$emit('ChildInputToApp',childinput)
    }
  }

}
</script>

<style>
</style>