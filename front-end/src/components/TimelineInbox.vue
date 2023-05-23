<template>
  <v-container>
    <v-row dense>
      <v-col v-for="(item, i) in items" :key="i" cols="12">
        <v-card :color="item.color" dark>
          <div class="d-flex flex-no-wrap">
            <v-col cols="3" md="3">
              <v-avatar class="ma-3" :size="isMobile ? '200' : '400'" tile>
                <v-img :src="item.src"></v-img>
              </v-avatar>
            </v-col>
            <v-col cols="9" md="9">
              <v-card-title class="text-h5">{{ item.title }}</v-card-title>
              <v-card-subtitle>{{ item.artist }}</v-card-subtitle>
              <v-card-text>{{ item.text }}</v-card-text>
              <v-card-actions>
                <v-btn class="ml-2 mt-5" outlined rounded small>
                  START RADIO
                </v-btn>
              </v-card-actions>
            </v-col>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import axios from "axios";
export default {
  name: "TimelineInbox",
  //   components: {
  //   },
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
      ],
      //   texts: [
      //     {
      //       avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
      //       title: "Brunch this weekend?",
      //       subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
      //     },
      //     {
      //       avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
      //       title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
      //       subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
      //     },
      //     {
      //       avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
      //       title: "Oui oui",
      //       subtitle:
      //         '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
      //     },
      //     {
      //       avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
      //       title: "Birthday gift",
      //       subtitle:
      //         '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
      //     },
      //     {
      //       avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
      //       title: "Recipe to try",
      //       subtitle:
      //         '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
      //     },
      //   ],
    };
  },
  //   watch: {
  //   },
  // mounted() {
  // },
  //   methods: {
  //   },
};
</script>
<style scoped></style>
