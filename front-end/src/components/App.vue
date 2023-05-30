<template>
  <v-app>
    <v-app-bar
      fixed
      color="purple"
      class="header"
      max-height="64px"
      height="64px"
    >
      <!-- ハンバーガーメニューアイコン -->
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-icon class="ml-5 mr-2">{{ titleIcon }}</v-icon>
      <v-toolbar-title>{{ title }}</v-toolbar-title>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      class="drawer"
      absolute
      bottom
      temporary
      app
      clipped
    >
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

    <v-main class="pt-10">
      <router-view />
    </v-main>
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
      title: "タイムライン",
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
    clickListItem(index) {
      console.log(index);
      console.log(this.navigationId);
      if (this.navigationId !== index) {
        this.title = this.nav_lists[index].name;
        this.titleIcon = this.nav_lists[index].icon;
        this.navigationId = this.nav_lists[index].id;
        switch (index) {
          case 0:
            this.$router.push({ name: "TimelineInbox" });
            break;
          case 1:
            this.$router.push({ name: "BookPocket" });
            break;
          case 2:
            this.$router.push({ name: "AddNewBook" });
            break;
          case 3:
            this.$router.push({ name: "Wordcloud" });
            break;
          case 5:
            this.$router.push({ name: "AddNewBook" });
            break;
          default:
            console.log("Unknown page.");
            this.$router.push({ name: "Timeline" });
            break;
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
