<template>
  <v-app id="app" v-if="isHeader">
    <v-app id="inspire">
      <v-app id="keep">
        <v-app-bar app clipped-left color="green lighten-2">
          <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
          <span
            style="font-family: 'Gugi', cursive; font-size: 1.8em"
            class="logo ml-5 mr-10"
            @click="toMain"
            >MOMOGO
            <!-- <span class="font-weight-light">Keep</span> -->
          </span>

          <!--여기까지 MOMOGO로고  -->
          <v-text-field
            solo-inverted
            flat
            hide-details
            label="Search"
            v-model="foodSearch"
            @keyup.enter="search"
            style="margin-left: 8vw; width: 40vw"
          >
          </v-text-field>
          <!-- 여기까지 입력부분 -->
          <v-spacer></v-spacer>
          <!-- spacer는 간격을 만들어주는 역할 -->
          <span>
            <v-avatar id="myInfo" color="" size="30px" @click="toMyInfo">
              <v-icon dark size="28px"> mdi-account-circle </v-icon>
            </v-avatar>
          </span>
          <button
            style="position: relative; padding-left: 10px"
            @click="logout"
          >
            Logout
          </button>
          <!-- 여기 부분은 header 오른쪽 상단에 프로필 -->
        </v-app-bar>
        <!-- 여기까지가 상단의 app-bar -->

        <v-navigation-drawer
          v-model="drawer"
          app
          clipped
          color="grey lighten-4"
          style="width: 180px"
        >
          <!-- 여기까지가 v-navigation-drawer 배경 -->

          <v-list dense class="grey lighten-4">
            <!-- 리스트를 생성...dense는 높이를 최대한으로 조밀하게 만든다. -->

            <template v-for="(item, i) in items">
              <v-divider
                v-if="item.divider"
                :key="i"
                dark
                class="my-4"
              ></v-divider>
              <!-- dat에 혹시 item.divider이면 줄이 생성 -->
              <v-row v-else-if="item.heading" :key="i">
                <v-col cols="6">
                  <v-subheader
                    v-if="item.heading"
                    style="width: 150px; font-size: 8px; margin-left: 5px"
                  >
                    {{ item.heading }}
                  </v-subheader>
                </v-col>
              </v-row>
              <!-- 음식 카테고리 -->

              <v-list-item v-else :key="i" link>
                <v-list-item-title
                  v-if="item.to"
                  style="justify-content: center; text-align: center"
                >
                  <router-link :to="item.to" tag="v-list-item-title">
                    <b>
                      {{ item.text }}
                    </b>
                  </router-link>
                </v-list-item-title>
                <!-- 일단 라우터링크가 존재하면, 거기로 이동하게 한다. -->

                <v-list-item-title
                  v-else
                  style="justify-content: center; text-align: center"
                >
                  <b>
                    {{ item.text }}
                  </b>
                </v-list-item-title>
                <!-- 나중에 라우터링크 다 만들면 위에 부분은 삭제한다. v-if도 -->
              </v-list-item>
            </template>
          </v-list>
        </v-navigation-drawer>
      </v-app>
    </v-app>
  </v-app>
</template>

<script>
import constants from "@/lib/constants.js";

export default {
  name: "Header",
  components: {},
  props: ["isHeader"],
  computed: {},
  watch: {},
  mounted() {
    const token = localStorage.getItem("jwt");
    if (token) {
      this.Login = true;
    }
  },
  created() {
    // this.drawer = false
  },
  methods: {
    logout() {
      localStorage.removeItem("jwt");
      localStorage.removeItem("username");
      this.Login = false;
      alert("로그아웃되었습니다.");
      this.$router.push({ name: "login" })
    },
    search() {
      this.$router.push({
        name: "FoodSearch",
        query: { title: this.foodSearch },
      });
      location.reload();
    },
    toMain() {
      this.$router.push("/main");
    },
    toMyInfo() {
      this.$router.push("/passwordconfirm");
    },
  },

  data: function () {
    return {
      foodSearch: "",
      Login: false,
      constants,
      drawer: null,
      items: [
        { text: "TODAY", to: "/today" },
        { text: "식단달력", to: "/calendar" },
        { text: "추천", to: "/suggest" },

        { divider: true },
        { text: "커뮤니티", to: "/community" },

        
        { divider: true },
        { heading: "음식카테고리" },
        { text: "밥류", to: {name:"FoodSearch", query: {title :"국밥"}}},
        { text: "구이류", to: {name:"FoodSearch", query: {title :"구이"}}},
        { text: "국류", to: {name:"FoodSearch", query: {title :"국"}}},
        { text: "반찬류",to: {name:"FoodSearch", query: {title :"김치"}} },
        { text: "면류", to: {name:"FoodSearch", query: {title :"면"}} },
        { text: "튀김", to: {name:"FoodSearch", query: {title :"튀김"}} },
        { text: "볶음", to: {name:"FoodSearch", query: {title :"볶음"}} },
      ],
    };
  },
};
</script>


<style>
@import url("https://fonts.googleapis.com/css2?family=Gugi&display=swap");

#keep .v-navigation-drawer__border {
  display: none;
}

.logo:hover {
  color: gray;
  cursor: pointer;
}

#myInfo:hover {
  cursor: pointer;
}

.v-application--wrap {
  min-height: 0px !important;
}
</style>