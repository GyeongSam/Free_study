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
      nowCharacterState:"2단계",
      CharacterName:"싸플라워",
      imgScr:"/img/ssaflower.png",
      beforeUrl:null,
      afterUrl:"/",
    }
  }
}
</script>
