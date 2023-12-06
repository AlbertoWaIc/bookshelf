<template>
  <v-app>
    <v-app-bar
      color="deep-purple accent-4"
      dark
      absolute
      clipped-left
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <span>書籍管理アプリ</span>
      <!-- <v-toolbar-title>My files</v-toolbar-title> -->
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute bottom temporary>
      <v-list>
        <v-list-item-group
          v-model="group"
          clipped-left
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item
            v-for="nav_list in nav_lists"
            :key="nav_list.id"
            @click="clickListItem(nav_list.id)"
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

    <v-sheet
      id="scrolling-techniques-7"
      class="overflow-y-auto"
      max-height="900"
    >
      <v-container>
        <v-main class="pt-10">
          <router-view />
        </v-main>
      </v-container>
    </v-sheet>
  </v-app>
</template>

<script>
// import TimelineInbox from "@/components/TimelineInbox";
// import AddNewBook from "@/components/AddNewBook";

export default {
  name: "App",
  // components: {
  //   TimelineInbox,
  //   AddNewBook
  // },
  data() {
    return {
      drawer: false,
      group: null,
      titleIcon: "mdi-square-rounded-badge-outline",
      title: "本棚",
      navigationId: 0,
      nav_lists: [
        // {
        //   id: 0,
        //   name: "タイムライン",
        //   icon: "mdi-square-rounded-badge-outline",
        // },
        { id: 0, name: "本棚", icon: "mdi-bookshelf" },
        { id: 1, name: "書籍登録", icon: "mdi-book-plus" },
        { id: 2, name: "分析", icon: "mdi-google-analytics" },
        { id: 3, name: "書籍を探す", icon: "mdi-magnify" },
        // { id: 3, name: "アカウント情報", icon: "mdi-view-dashboard" },
        // { id: 4, name: "設定", icon: "mdi-cog-outline" },
      ],
    };
  },
  watch: {
    group() {
      this.drawer = false;
    },
  },
  methods: {
    clickListItem(index) {
      if (this.navigationId !== index) {
        this.title = this.nav_lists[index].name;
        this.titleIcon = this.nav_lists[index].icon;
        this.navigationId = this.nav_lists[index].id;
        let targetRoute = null;

        switch (index) {
          case 0:
            targetRoute = { name: "BookPocket" };
            break;
          case 1:
            targetRoute = { name: "AddNewBook" };
            break;
          case 2:
            targetRoute = { name: "Wordcloud" };
            break;
          case 3:
            targetRoute = { name: "FindNewBook" };
            break;
          default:
            console.log("Unknown page.");
            targetRoute = { name: "BookPocket" };
            break;
        }

        if (targetRoute) {
          if (this.$route.name !== targetRoute.name) {
            this.$router.push(targetRoute);
          }
        }
      }
    },
  },
};
</script>

<style scoped>
.drawer {
  margin-top: 64px; /* v-app-barの高さに合わせて適切なマージンを設定 */
}
</style>
