<template>
  <div class="home">
    <h1>home</h1>
    <div>
      <button v-on:click="test">axios 테스트</button>
    </div>
    <div>
      <div class="id-input-wrapper">
        <input type="text" v-model="userid" />
      </div>
      <div class="password-input-wrapper">
        <input type="password" v-model="userpw" />
      </div>
      <button v-on:click="login">로그인</button>
    </div>
    <div>
      <button v-on:click="logout">로그아웃</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      userid: "",
      userpw: "",
      URL: "http://localhost:8000/",
      TOKEN: "",
    };
  },
  methods: {
    async test() {
      try {
        const response = await axios({
          method: "get",
          url: this.URL + "api/v1/articles/",
          headers: {
            Authorization: "Token " + this.TOKEN
          },
        });
        if (response.data) {
          console.log(response.data);
        }
      } catch (error) {
        console.log(error);
      }
    },
    async login() {
      try {
        console.log(this.userid);
        console.log(this.userpw);
        const response = await axios.post(this.URL + "accounts/login/", {
          username: this.userid,
          password: this.userpw,
        });
        if (response.data) {
          console.log(response.data);
          this.TOKEN = response.data.key;
        }
      } catch (error) {
        console.log(error);
      }
    },
    async logout() {
      try {
        const response = await axios.post(this.URL + "accounts/logout/");
        if (response.data) {
          console.log(response.data);
          this.TOKEN = "";
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>