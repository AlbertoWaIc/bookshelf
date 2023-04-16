<template>
  <v-container>
    <v-row class="text-center">
      <v-col>
        <v-card class="mx-auto px-6 py-8" max-width="344">
          <v-card-title>あなたのメールアドレスを入力</v-card-title>
          <v-form>
            <v-text-field
              v-model="mail"
              counter
              label="メールアドレス"
              :rules="[rules.emailFormat]"
              class="mb-2"
            ></v-text-field>
            <br />
            <v-btn block size="large" @click="clickUserMail" :disabled="mailFlg"
              >確認</v-btn
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
  name: "ForgetPassword",

  data() {
    return {
      mail: "",
      mailFlg: true,
      rules: {
        emailFormat: (value) => this.checkEmailFormat(value),
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
    clickUserMail() {
      const param = {
        mail: this.mail,
      };
      this.$emit("CheckUserMail", param);
    },
    // clickRegisterNewPassword() {
    //   const param = {
    //     password: this.password,
    //   };
    //   this.$emit("registerNewPassword", param);
    // },
  },
};
</script>
