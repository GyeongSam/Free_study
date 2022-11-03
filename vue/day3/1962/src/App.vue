<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>appParentData: {{appParentData}}</p>
    <p>appChildData: {{appChildData}}</p>
    <AppParent :app-data="appData" :app-child-data="appChildData" :app-parent-data="appParentData" v-on:ParentInputToApp="ParentInputToApp" v-on:ChildInputToApp="ChildInputToApp"/>
  </div>
</template>

<script>
import AppParent from "./components/AppParent.vue"
export default {
  components:{
    AppParent
  },
  data(){
    return {
    appData : "",
    appChildData : "",
    appParentData : ""
    }
  },
  methods:{
    ParentInputToApp: function(inputData){
      this.appParentData=inputData;
    },
    ChildInputToApp: function(childData){
      this.appChildData=childData;
    }
  }
}
</script>

<style>
</style>
