<template>
  <div>
    <Header style="min-height: 0px;" :isHeader="isHeader"/>
    <router-view />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import constants from './lib/constants'

export default {
  name: 'App',

  components: {
    Header
  },
  created() {
    let url = this.$route.name;
    this.checkUrl(url)
    // if (localStorage.length > 0) {
    //     for (var i = 0; i < localStorage.length; i++) {
    //       if (localStorage.key(i) != "loglevel:webpack-dev-server")
    //         this.Items.push(localStorage.key(i));
    //     }
    //   }
  },
  watch: {
    $route (to) {
      this.checkUrl(to.name);
    }
  },

  methods: {
    checkUrl(url) {
      let array = [
        constants.URL_TYPE.USER.LOGIN,
        constants.URL_TYPE.USER.JOIN,
        constants.URL_TYPE.HOME.HOME,
      ];
      let isHeader = true;
      array.map(path => {
        if (url === path)
          isHeader = false;
      })
      this.isHeader = isHeader;
    },
  },

  data: function () {
    return {
      isHeader: true,
      constants
    }
  }
};
</script>



<style>
  
</style>