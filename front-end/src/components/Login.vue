<template>
  <v-container fluid>
    <v-row align="center">
      <v-col cols="12" md="12" align-self="center" class="login">
        <div v-if="showScreen !== 0">
          <v-icon @click="backToTop" class="ml-5">mdi-arrow-left-bold</v-icon
          >ログイン画面へ戻る
        </div>
        <v-spacer></v-spacer>
        <!-- Singinの要素 -->
        <SingIn v-if="showScreen === 0" @clickLogin="clickLogin" />
        <!-- メールアドレスを入力してユーザー情報を取得 -->
        <CheckUsermail v-if="showScreen === 1" @CheckUserMail="CheckUserMail" />
        <!-- ユーザー情報を取得後にパスワードを更新する -->
        <ForgetPassword
          v-if="showScreen === 2"
          :userId="userId"
          @registerNewPassword="registerNewPassword"
        />
        <CreateAccount
          v-if="showScreen === 3"
          @registerNewAccount="registerNewAccount"
        />
        <!-- 初期表示。パスワード忘れ -->
        <v-row class="text-center" v-if="showScreen === 0">
          <v-col cols="12">
            <v-btn @click="showForgertPassword">パスワードを忘れた方</v-btn>
          </v-col>
          <v-col cols="12">
            <v-btn @click="createNewAccount">初回登録はこちら </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import SingIn from "./elements/SingIn.vue";
import ForgetPassword from "./elements/ForgetPassword.vue";
import CheckUsermail from "./elements/CheckUsermail.vue";
import CreateAccount from "./elements/CreateAccount.vue";
import axios from "axios";
export default {
  name: "LoginStart",
  components: {
    SingIn,
    ForgetPassword,
    CheckUsermail,
    CreateAccount,
  },
  data() {
    return {
      mail: "",
      password: "",
      showScreen: 0,
      userId: 0,
    };
  },
  // mounted() {
  // },
  methods: {
    // 動作確認用のテスト
    clickLogin(data) {
      console.log(data);
      axios.post("http://127.0.0.1:8000/login/loginApi", data).then((res) => {
        try {
          let data = JSON.parse(JSON.stringify(res.data));
          console.log(data);
        } catch (e) {
          console.log(e);
        }
      });
    },
    //新規ユーザー登録
    registerNewAccount(data) {
      console.log(data);
      axios
        .post("http://127.0.0.1:8000/login/registerNewAccount", data)
        .then((res) => {
          try {
            let data = JSON.parse(JSON.stringify(res.data));
            console.log(data);
          } catch (e) {
            console.log(e);
          }
        });
      this.backToTop();
    },
    CheckUserMail(data) {
      console.log(data);
      axios
        .post("http://127.0.0.1:8000/login/checkUserMail", data)
        .then((res) => {
          try {
            let data = JSON.parse(JSON.stringify(res.data));
            console.log(data);
            if (data.error !== "") {
              this.showUsermail();
              console.log("errorがあります。");
            } else if (data.user_id === "") {
              this.userId = data.user_id;
              this.showUsermail();
              console.log("user_idがない。");
            } else {
              this.showForgertPassword();
            }
          } catch (e) {
            console.log(e);
          }
        });
      this.backToTop();
    },
    // パスワードの再登録
    registerNewPassword(data) {
      console.log(data);
      this.$router.push("/HelloWorld");
      axios
        .post("http://127.0.0.1:8000/login/registerNewPassword", data)
        .then((res) => {
          try {
            let data = JSON.parse(JSON.stringify(res.data));
            console.log(data);
          } catch (e) {
            console.log(e);
          }
        });
      // this.backToTop();
    },
    backToTop() {
      this.showScreen = 0;
    },
    showUsermail() {
      this.showScreen = 1;
    },
    showForgertPassword() {
      this.showScreen = 2;
    },
    createNewAccount() {
      this.showScreen = 3;
    },
  },
};
</script>
<style scoped>
.login {
  margin: 150px 0 0 0px;
}
</style>
