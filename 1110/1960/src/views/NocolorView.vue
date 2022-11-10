<template>
  <div>
    <ImgCard
      v-bind:nowCharacterState="nowCharacterState"
      v-bind:CharacterName="CharacterName"
      v-bind:imgScr="imgScr"
      v-bind:beforeUrl="beforeUrl"
      v-bind:afterUrl="afterUrl"
    />
  </div>
</template>

<script>
import ImgCard from "../components/ImgCard.vue"
export default {
  components: { ImgCard },
  data(){
    return{
      nowCharacterState:"시작",
      CharacterName:"싸플링",
      imgScr:"/img/ssafling.png",
      beforeUrl:"/",
      afterUrl:"/ssafeaf",
    }
  }
}
</script>
