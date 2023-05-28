<template>
  <v-container class="mt-4">
    <v-row justify="center">
      <v-col cols="6">
        <v-text-field v-model="search" prepend-inner-icon="mdi-magnify" label="キーワード検索"></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "AddNewBook",
  data() {
    return {
      search:""
    }
  },
  // props: {
  // },
  // methods: {
  // },
};
</script>

<style scoped>
.card-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 200px;
  border-radius: 8px;
  background-color: #f0f0f0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-button-content {
  width: 100%;
  height: 100%;
  font-size: 24px;
}
</style>