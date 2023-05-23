<template>
  <div>
    <v-app-bar color="deep-purple" dark app clipped-left>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-icon class="ml-5 mr-2">{{ titleIcon }}</v-icon>
      <v-toolbar-title>{{ titile }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-app-bar>

    <!-- ナビゲーションバーのメニュー一覧 -->
    <v-navigation-drawer v-model="drawer" absolute bottom temporary app clipped>
      <v-list>
        <v-list-item-group
          v-model="group"
          clipped-left
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item
            v-for="nav_list in nav_lists"
            :key="nav_list.id"
            @click="clickListItem(nav_list)"
          >
            <v-list-item-icon>
              <v-icon>{{ nav_list.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ nav_list.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <TimelineInbox v-if="navigationId === 0" />
  </div>
</template>

<script>
import TimelineInbox from "./TimelineInbox.vue";
// import axios from "axios";
export default {
  name: "Timeline",
  components: {
    TimelineInbox,
  },
  data() {
    return {
      drawer: false,
      group: null,
      titleIcon: "mdi-square-rounded-badge-outline",
      titile: "タイムライン",
      navigationId: 0,
      nav_lists: [
        {
          id: 0,
          name: "タイムライン",
          icon: "mdi-square-rounded-badge-outline",
        },
        { id: 1, name: "本棚", icon: "mdi-bookshelf" },
        { id: 2, name: "書籍登録", icon: "mdi-book-plus" },
        { id: 3, name: "分析", icon: "mdi-google-analytics" },
        { id: 4, name: "アカウント情報", icon: "mdi-view-dashboard" },
        { id: 5, name: "設定", icon: "mdi-cog-outline" },
      ],
    };
  },
  watch: {
    group() {
      this.drawer = false;
    },
  },
  // mounted() {
  // },
  methods: {
    clickListItem(item) {
      this.titile = item.name;
      this.titleIcon = item.icon;
      this.navigationId = item.id;
      //   switch (item.id) {
      //     case 0:
      //       this.$router.push("/timelineInbox");
      //       break;
      //     case 1:
      //       this.$router.push("/timelineInbox");
      //       break;
      //     case 2:
      //       this.$router.push("/timelineInbox");
      //       break;
      //     case 3:
      //       this.$router.push("/timelineInbox");
      //       break;
      //     case 4:
      //       this.$router.push("/timelineInbox");
      //       break;
      //     case 5:
      //       this.$router.push("/timelineInbox");
      //       break;
      //     default:
      //       this.$router.push("/timelineInbox");
      //       break;
      //   }
    },
  },
};
</script>
<style scoped>
/* .centered-title {
  display: flex;
  justify-content: center;
  align-items: center;
} */
</style>
