<template>
  <v-container>
    <v-row class="text-center">
      <v-col>
        <v-card class="mx-auto px-6 py-8" max-width="344">
          <v-card-title>Signg in</v-card-title>
          <v-form>
            <v-text-field
              v-model="mail"
              label="メールアドレス"
              class="mb-2"
              :rules="[rules.emailFormat]"
            ></v-text-field>
            <v-text-field
              v-model="password"
              :type="showPass ? 'text' : 'password'"
              counter
              :append-inner-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append-inner="showPass = !showPass"
              label="パスワード"
              :rules="[rules.passwordLength]"
            ></v-text-field>
            <br />
            <v-btn
              block
              size="large"
              @click="clickLoginBtn"
              :disabled="mailFlg || passwordFlg"
              >ログイン</v-btn
            >
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { checkLoginValidation } from "../../plugins/validation.js";

export default {
  name: "SingIn",
  data() {
    return {
      mail: "",
      password: "",
      showPass: false,
      mailFlg: true,
      passwordFlg: true,
      rules: {
        emailFormat: (value) => this.checkEmailFormat(value),
        passwordLength: (value) => this.checkPasswordLength(value),
      },
    };
  },
  methods: {
    checkEmailFormat(value) {
      if (checkLoginValidation.emailFormat(value)) {
        this.mailFlg = false;
        return true;
      } else {
        return "Invalid email format.";
      }
    },
    checkPasswordLength(value) {
      if (checkLoginValidation.passwordLength(value)) {
        this.passwordFlg = false;
        return true;
      } else {
        return "Password must be at least 8 characters long.";
      }
    },
    // ログインボタンクリック
    clickLoginBtn() {
      let finalVlaueCheck = this.checkUserDataValidation();
      if (finalVlaueCheck) {
        this.resetUserData();
        return;
      }
      const param = {
        mail: this.mail,
        password: this.password,
      };
      this.$emit("clickLogin", param);
    },
    // emit前の値の存在チェック
    checkUserDataValidation() {
      return this.mail === "" || this.password === "" ? true : false;
    },
    // ユーザーが入力したデータを初期化させる
    resetUserData() {
      this.mail = "";
      this.password = "";
    },
  },
};
</script>
