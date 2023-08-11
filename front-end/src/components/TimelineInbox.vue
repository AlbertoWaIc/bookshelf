<template>
  <v-container>
    <!--  データがないときは「データを登録しよう！」みたいなイメージを表示させたい  -->
    <v-row class="ma-5">
      <v-col align="center">
        <v-btn rounded>TODAY</v-btn>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col v-for="(item, i) in items" :key="i" cols="9">
        <v-card :color="item.color" dark class="hover-card">
          <div class="d-flex flex-no-wrap">
            <v-col cols="4" class="pa-3">
              <v-avatar size="100%" tile>
                <v-img
                  :src="item.src"
                  :style="{ 'max-width': '100%', 'max-height': '100%' }"
                ></v-img>
              </v-avatar>
            </v-col>

            <v-col cols="4" class="pa-3">
              <v-card-title class="text-h5">{{ item.title }}</v-card-title>
              <v-card-subtitle>{{ item.artist }}</v-card-subtitle>
              <v-card-text class="word-wrap normal">{{
                item.text
              }}</v-card-text>
              <v-card-actions>
                <v-list-item-avatar color="grey darken-3">
                  <v-img
                    class="elevation-6"
                    alt=""
                    src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                  ></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>Evan You</v-list-item-title>
                </v-list-item-content>
              </v-card-actions>
            </v-col>

            <v-col cols="4" class="pa-3">
              <v-card-text>{{ item.text }}</v-card-text>
            </v-col>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <!--    <div class="floating-button">-->
    <!--    <v-btn-->
    <!--      class="mx-2"-->
    <!--      fab-->
    <!--      dark-->
    <!--      color="indigo"-->
    <!--      @click="moveToAddNewBook()"-->
    <!--      v-if="navigationId === 1"-->
    <!--    >-->
    <!--      <v-icon dark>-->
    <!--        mdi-plus-->
    <!--      </v-icon>-->
    <!--    </v-btn>-->
    <!--  </div>-->
  </v-container>
</template>

<script>
// import axios from "axios";
export default {
  name: "TimelineInbox",
  data() {
    return {
      items: [
        {
          color: "#385F73",
          src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
          title: "Unlimited music now",
          artist: "superfly",
          text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
        {
          color: "#1F7087",
          src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
          title: "Supermodel",
          artist: "Foster the People",
          text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
        {
          color: "#952175",
          src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
          title: "Halcyon Days",
          artist: "Ellie Goulding",
          text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
        {
          color: "#148954",
          src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
          title: "Supermodel",
          artist: "Foster the People",
          text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
        },
        {
          color: "#909090",
          src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
          title: "Halcyon Days",
          artist: "Ellie Goulding",
          text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique",
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
  methods: {},
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
</style>
