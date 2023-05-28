<template>
  <div>
<!--    <TimelineInbox />-->
  </div>
</template>

<script>
// import TimelineInbox from "./TimelineInbox.vue";
// import axios from "axios";
export default {
  name: "Timeline",
  // components: {
  //   TimelineInbox,
  // },
  data() {
    return {
    };
  },
  watch: {
    group() {
      this.drawer = false;
    },
  },
  mounted() {
  },
  methods: {
  },
};
</script>
<style scoped>
</style>
