<template>
  <v-container class="mt-6">
    <v-row justify="center">
      <v-col cols="6">
        <!-- ここのアイテムの表示や要素の取得はもっと綺麗にしたい -->
        <!-- v-selectの表示位置がおかしい -->
        <v-select
          v-model="selectedItem"
          :items="getKeys(items)"
          label="ワードクラウドでまとめたい項目"
          outlined
        ></v-select>
      </v-col>
      <v-col cols="2" class="text-center mt-2">
        <v-btn @click="generateWordCloud" color="primary"
          >ワードクラウドの作成</v-btn
        ></v-col
      >
    </v-row>
    <v-row justify="center">
      <v-col cols="auto" class="text-center">
        <!-- 一時的にローカルで生成した画像をフロントのアプリに設置して表示している。 -->
        <img :src="require('../assets/img/wordcloud.png')" alt="Word Cloud" />
        <!-- <img :src="imagePath" alt="Word Cloud" /> -->
      </v-col>
      <v-col cols="auto" class="text-center">
        <v-data-table
          :headers="headers"
          :items="wordRankList"
          hide-default-footer
          no-data-text="ワードクラウドを作成してください"
          class="elevation-1"
          :page.sync="page"
          :items-per-page="itemsPerPage"
          @page-count="pageCount = $event"
        >
        </v-data-table>
        <v-pagination v-model="page" :length="pageCount" circle></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "Wordcloud",
  data() {
    return {
      // dataに設置はいやだ
      items: {
        タイトル: 0,
        概要: 1,
        著者: 2,
        本の感想: 3,
      },
      selectedItem: "",
      wordcloudImage: "",
      wordRankList: [],
      page: 1,
      pageCount: 0,
      itemsPerPage: 10,
      headers: [
        {
          text: "単語",
          value: "word",
        },
        { text: "使用回数", value: "usedTimes" },
      ],
    };
  },
  methods: {
    getKeys(obj) {
      return Object.keys(obj);
    },
    generateWordCloud() {
      // 選択された項目に基づいてワードクラウドを生成する処理を実装
      console.log("Selected item:", this.selectedItem);
      //  itemsのvalueを引数にしてDBにあるに各データを取得したい。
      let param = {
        wordcloud_target: this.selectedItem,
      };
      axios
        .post("http://127.0.0.1:8000/book/createWordcloud", param)
        .then((res) => {
          try {
            let data = res.data;
            console.log(data);
            this.wordcloudImage = data.image_path;
            this.wordRankList = data.word_rank;
          } catch (e) {
            console.log(e);
          }
        });
    },
  },
};
</script>

<style scoped></style>
