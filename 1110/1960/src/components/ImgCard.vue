<template>
  <div>
    <h2>{{nowCharacterState}}</h2>
    <button v-on:click="moveBefore">뒤로</button>
    <img v-bind:src="imgSrc" v-bind:alt="imgSrc" height="300" />
    <button v-on:click="moveAfter">앞으로</button>
    <h2>{{CharacterName}}</h2>
  </div>
</template>


<script>
export default{
  props:[
    "nowCharacterState",
    "CharacterName",
    "imgSrc",
    "beforeUrl",
    "afterUrl",
  ],
  methods:{
    moveBefore(){
      if(this.beforeUrl===null){
        alert("이전으론 못가삼!")
        return;
      }
      this.$router.push(this.beforeUrl);
    },
    moveAfter(){
      if(this.afterUrl==='/'){
        alert("홈으로 돌아간닷!")
      }
      this.$router.push(this.afterUrl);
    }
  }
}
</script>
