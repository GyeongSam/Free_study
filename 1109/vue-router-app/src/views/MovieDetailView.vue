<template>
  <div>
    <h1>여기는 {{movieId}}번째 영화 페이지삼!</h1>
  </div>
</template>

<script>
export default {
  computed:{
    movieId(){
      return this.$route.params.movieId
    }
  }
}
</script>
