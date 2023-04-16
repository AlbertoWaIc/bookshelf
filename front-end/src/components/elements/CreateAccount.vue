<template>
  <v-container>
    <v-row class="text-center">
      <v-col>
        <v-card class="mx-auto px-6 py-8" max-width="344">
          <v-card-title>パスワードの再登録</v-card-title>
          <v-form>
            <v-text-field
              v-model="mail"
              label="メールアドレス"
              class="mb-2"
              :rules="[rules.emailFormat]"
            ></v-text-field>
            <v-text-field
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              counter
              :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append-inner="showPassword = !showPassword"
              label="パスワード"
              :rules="[rules.passwordLength]"
              class="mb-2"
            ></v-text-field>
            <v-text-field
              v-model="prePassword"
              :type="showPrePassword ? 'text' : 'password'"
              counter
              :append-inner-icon="showPrePassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append-inner="showPrePassword = !showPrePassword"
              label="確認用パスワード"
              :rules="[rules.comparePrePassword]"
              class="mb-2"
            ></v-text-field>
            <br />
            <v-btn
              block
              size="large"
              @click="clickRegisterNewAccount"
              :disabled="mailFlg || prePasswordFlg || passwordFlg"
              >登録</v-btn
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
  name: "CreateAccount",

  data() {
    return {
      mail: "",
      prePassword: "",
      password: "",
      mailFlg: true,
      prePasswordFlg: true,
      passwordFlg: true,
      showPassword: false,
      showPrePassword: false,
      rules: {
        emailFormat: (value) => this.checkEmailFormat(value),
        passwordLength: (value) => this.checkPasswordLength(value),
        comparePrePassword: (value) => this.comparePrePassword(value),
      },
    };
  },
  computed: {},
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
    comparePrePassword(value) {
      if (this.password === "") {
        return;
      }
      if (!checkLoginValidation.passwordLength(value)) {
        return "Password must be at least 8 characters long.";
      }
      if (!checkLoginValidation.comparePrePassword(value, this.password)) {
        return "prePassword is not same as Password";
      }
      this.prePasswordFlg = false;
      return true;
    },
    clickRegisterNewAccount() {
      const param = {
        mail: this.mail,
        password: this.password,
      };
      this.$emit("registerNewAccount", param);
    },
  },
};
</script>
