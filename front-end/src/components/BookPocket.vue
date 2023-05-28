<template>
  <v-container class="mt-10">
    <!--  データがないときは「データを登録しよう！」みたいなイメージを表示させたい  -->
    <v-row>
      <v-col v-for="(item, i) in items" :key="i" cols="3">
        <v-card :color="item.color" class="hover-card white--text">
          <v-row class="text-center">
            <v-col cols="12" class="pa-3">
              <v-avatar size="auto" tile>
                <v-img
                  :src="item.src"
                  :style="{ 'max-width': '90%', 'max-height': '90%' }"
                ></v-img>
              </v-avatar>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" class="pa-3">
              <v-card-title class="text-h5">{{ item.title }}</v-card-title>
              <v-card-subtitle>{{ item.author }}</v-card-subtitle>
              <v-card-text>{{ item.category }}</v-card-text>
              <v-card-text class="word-wrap normal">{{
                item.wrap_up_text
              }}</v-card-text>
              <v-card-text class="word-wrap normal d-flex align-center">
                <!-- 編集ボタン押下したら★の編集が可能にしたい。クリックだけでAPIを更新したい -->
                <!-- APIで更新エラーの時だけトーストを表示する -->
                <template v-for="index in 5">
                  <v-icon
                    :key="index"
                    :class="
                      index <= item.star
                        ? 'mdi mdi-star yellow--text'
                        : 'mdi mdi-star-outline'
                    "
                  ></v-icon>
                </template>
                <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon class="white--text">mdi-pencil</v-icon>
                </v-btn>
              </v-card-text>
            </v-col>
          </v-row>

          <v-col>
            <v-expansion-panels>
              <v-expansion-panel class="transparent white--text">
                <v-expansion-panel-header>感想</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <!-- <div>{{ item.text }}</div> -->
                  <div v-if="!editMode">
                    <!-- 表示モードのコンテンツ -->
                    {{ item.summary }}
                    <v-btn icon @click="clickEditMode(item.summary)">
                      <v-icon class="white--text">mdi-pencil</v-icon>
                    </v-btn>
                  </div>
                  <div v-else>
                    <!-- 編集モードのコンテンツ -->
                    <v-textarea v-model="editedText" counter>{{
                      item.summary
                    }}</v-textarea>
                    <v-btn icon @click="saveEdit">
                      <v-icon class="white--text">mdi-check</v-icon>
                    </v-btn>
                    <v-btn icon @click="cancelEdit">
                      <v-icon class="white--text">mdi-close</v-icon>
                    </v-btn>
                  </div></v-expansion-panel-content
                >
              </v-expansion-panel>
            </v-expansion-panels>
          </v-col>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "BookPocket",
  data() {
    return {
      editMode: false,
      editedText: "",
      items: [
        {
          color: "#385F73",
          src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
          title: "Unlimited music now",
          author: "superfly",
          category: "ggggfdvfdvfd",
          star: 0,
          wrap_up_text:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
          summary:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
        {
          color: "#1F7087",
          src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
          title: "Supermodel",
          author: "Foster the People",
          category: "ggggfdvfdvfd",
          star: 2,
          wrap_up_text:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
          summary:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
        {
          color: "#952175",
          src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
          title: "Halcyon Days",
          author: "Ellie Goulding",
          category: "ggggfdvfdvfd",
          star: 3,
          wrap_up_text:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
          summary:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
        {
          color: "#148954",
          src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
          title: "Supermodel",
          author: "Foster the People",
          category: "ggggfdvfdvfd",
          star: 4,
          wrap_up_text:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
          summary:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
        {
          color: "#909090",
          src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
          title: "Halcyon Days",
          author: "Ellie Goulding",
          category: "ggggfdvfdvfd",
          star: 5,
          wrap_up_text:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
          summary:
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
      ],
    };
  },
  props: {
    navigationId: {
      type: Number,
      default: 0,
    },
  },
  methods: {
    clickEditMode(summary) {
      this.editedText = summary;
      this.editMode = true;
    },
    saveEdit() {
      // 編集内容を保存する処理を実装
      // 例えば、this.editedText を保存するAPIリクエストなどを行う

      // 編集モードを終了し、表示モードに切り替える
      this.editMode = false;
      // this.item.summary = this.editedText; // データの更新
    },
    cancelEdit() {
      // 編集をキャンセルし、表示モードに切り替える
      this.editMode = false;
    },
  },
};
</script>
<style scoped>
.hover-card {
  transition: transform 0.3s ease;
}
.hover-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.floating-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 9999; /* 必要に応じて指定 */
}
.transparent
  .v-expansion-panel__container
  .transparent
  .v-expansion-panel__header
  .transparent
  .v-expansion-panel__content {
  background-color: transparent !important;
}
</style>
