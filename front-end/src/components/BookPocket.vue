<template>
  <v-container class="mt-10">
    <v-row justify="center">
      <v-col style="font-size: 25px">{{
        "本棚には" + items.length + "冊あります。"
      }}</v-col>
    </v-row>
    <!--  データがないときは「データを登録しよう！」みたいなイメージを表示させたい  -->
    <v-row>
      <v-col v-for="(item, i) in items" :key="i" cols="3">
        <v-card :color="item.color" class="hover-card white--text">
          <v-row class="text-center">
            <v-col cols="12" class="pa-3">
              <v-avatar size="100%" tile>
                <v-img :src="item.src" class="max-img"></v-img>
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
                    @click="updateSelectedStar(index, i)"
                  ></v-icon>
                </template>
                <v-spacer></v-spacer>
                <v-btn v-if="!item.editStar" icon @click="canEditStar(i)">
                  <v-icon class="white--text">mdi-pencil</v-icon>
                </v-btn>
                <v-btn v-else icon @click="canEditStar(i)">
                  <v-icon class="white--text">mdi-check</v-icon>
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
                    <v-textarea v-model="editedText" counter="1000">{{
                      item.summary
                    }}</v-textarea>
                    <v-btn icon @click="saveEdit(i)">
                      <v-icon class="white--text">mdi-check</v-icon>
                    </v-btn>
                    <v-btn icon @click="cancelEdit(i)">
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
import axios from "axios";
export default {
  name: "BookPocket",
  data() {
    return {
      editMode: false,
      editedText: "",
      tmpSummary: "",
      tmpStar: 0,
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
          editStar: false,
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
          editStar: false,
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
          editStar: false,
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
          editStar: false,
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
          editStar: false,
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
      this.tmpSummary = summary;
      this.editMode = true;
    },
    saveEdit(index) {
      // 入力文字数が1000文字以上の場合は切り上げる
      if (this.editedText && this.editedText.length > 1000) {
        this.editedText = this.editedText.slice(0, 1000);
      }
      this.items[index].summary = this.editedText;
      let param = {
        item: this.items[index],
      };
      axios
        .post("http://127.0.0.1:8000/book/update_user_summary", param)
        .then((res) => {
          try {
            let data = JSON.parse(JSON.stringify(res.data));
            console.log(data);
            // ローディング付けたい
          } catch (e) {
            console.log(e);
            this.items[index].summary = this.tmpSummary;
          } finally {
            this.editMode = false;
            this.makeInitInfo();
          }
        });
    },
    cancelEdit(index) {
      // 編集をキャンセルし、表示モードに切り替える
      this.items[index].summary = this.tmpSummary;
      this.editMode = false;
      this.makeInitInfo();
    },
    canEditStar(index) {
      this.tmpStar = this.items[index].star;
      this.items[index].editStar = !this.items[index].editStar;
    },
    updateSelectedStar(num, index) {
      if (this.items[index].editStar) {
        this.items[index].star = num; // クリックされた星のインデックスを取得し、selectedStarに代入
      }
      let param = {
        item: this.items[index],
      };
      axios
        .post("http://127.0.0.1:8000/book/update_user_summary", param)
        .then((res) => {
          try {
            let data = JSON.parse(JSON.stringify(res.data));
            console.log(data);
            // ローディング付けたい
          } catch (e) {
            console.log(e);
            this.items[index].star = this.tmpStar;
          } finally {
            this.editMode = false;
            this.makeInitInfo();
          }
        });
    },
    makeInitInfo() {
      this.editedText = "";
      this.tmpSummary = "";
      this.tmpStar = 0;
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
.max-img {
  max-width: 100%;
  max-height: 100%;
}
</style>
