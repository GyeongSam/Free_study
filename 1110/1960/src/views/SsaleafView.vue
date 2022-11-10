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
      nowCharacterState:"1단계",
      CharacterName:"싸리프",
      imgScr:"/img/ssaleaf.png",
      beforeUrl:null,
      afterUrl:"/ssaflower",
    }
  }
}
</script>
