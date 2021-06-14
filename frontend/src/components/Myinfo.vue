<template>
  <div id="Myinfo">
  <v-app id="inspire">
    <v-form>
      <v-container>
        <table class="tg" style="undefined;table-layout: fixed; width: 700px;">
<colgroup>
<col style="width: 220px">
<col style="width: 180px">
<col style="width: 180px">
<col style="width: 120px">
</colgroup>
<thead>
  <tr>
    <th class="tg-gvcd">My page</th>
    <th class="tg-gvcd"></th>
    <th class="tg-gvcd"></th>
    <th class="tg-gvcd">
      <v-btn
        depressed
        rounded
        color="primary"
        @click="upDate"
      >
        수정 완료
      </v-btn></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-gvcd" rowspan="3"><img src="data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 448 512'%3e%3cpath fill='%23000000' d='M436 160c6.6 0 12-5.4 12-12v-40c0-6.6-5.4-12-12-12h-20V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48v416c0 26.5 21.5 48 48 48h320c26.5 0 48-21.5 48-48v-48h20c6.6 0 12-5.4 12-12v-40c0-6.6-5.4-12-12-12h-20v-64h20c6.6 0 12-5.4 12-12v-40c0-6.6-5.4-12-12-12h-20v-64h20zm-228-32c35.3 0 64 28.7 64 64s-28.7 64-64 64-64-28.7-64-64 28.7-64 64-64zm112 236.8c0 10.6-10 19.2-22.4 19.2H118.4C106 384 96 375.4 96 364.8v-19.2c0-31.8 30.1-57.6 67.2-57.6h5c12.3 5.1 25.7 8 39.8 8s27.6-2.9 39.8-8h5c37.1 0 67.2 25.8 67.2 57.6v19.2z'/%3e%3c/svg%3e" alt="Image" width="100" height="100"></td>
    <td class="tg-gvcd" colspan="3">
      <v-col
            cols="12"
            sm="6"
          >
            <v-text-field
              v-model="user.username"
              label="아이디"
              disabled
              dense
            >
            </v-text-field>

          </v-col>
          </td>
  </tr>

  <tr>
    <td class="tg-gvcd" colspan="3">
      <v-col
            cols="12"
            sm="6"
          >
            <v-text-field
              v-model="user.nickname"
              label="닉네임"
              dense
            ></v-text-field>
          </v-col>
    </td>
  </tr>
  <tr>
    <td class="tg-gvcd">
      <v-col
            cols="12"
            sm="6"
          >
            <v-text-field
              v-model="user.sex"
              label="성별"
              dense
            ></v-text-field>
          </v-col>
    </td>
    <td class="tg-gvcd" colspan="2">
      <v-col
            cols="12"
            sm="4"
          >
            <v-text-field
              v-model="user.age"
              label="나이"
              dense
            ></v-text-field>
          </v-col>
    </td>
  </tr>
  <tr>
    <td class="tg-gvcd" rowspan="2"></td>
    <td class="tg-gvcd">
      <v-col
            cols="12"
            sm="4"
          >
            <v-text-field
              v-model="user.height"
              label="키"
              dense
            ></v-text-field>
          </v-col>
    </td>
    <td class="tg-gvcd" colspan="2">
      <v-col
            cols="12"
            sm="4"
          >
            <v-text-field
              v-model="user.weight"
              label="몸무게"
              dense
            ></v-text-field>
          </v-col>
    </td>
  </tr>
  <tr>
    <td class="tg-gvcd" colspan="3">
      <v-col
            cols="12"
            sm="11"
          >
            <v-text-field
              v-model="target"
              label="목표"
              dense
            ></v-text-field>
          </v-col>
    </td>
  </tr>
</tbody>
</table>
      </v-container>
    </v-form>
  </v-app>
</div>
</template>

<script>
import axios from 'axios';
import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "Myinfo",
  data () {
    return {
      user : {},
      // e_mail: 'asdfg@gmail.com',
      // nickname: '싸피간판',
      // sex: '여',
      // age: '27',
      // height: '165',
      // weight: '50',
      user_id : 0,
      target: '',
      memo: '',
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getMyName () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then((res)=>{
        this.user = res.data
      }).catch((err)=> {
        console.log(err)
      })
    },
    upDate() {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      const user = {
        user_info : this.user,
        user_id : info.user_id,
      }
      axios.put(`${SERVER_URL}/accounts/update/`,user, config)
      .then(()=> {
        this.$router.push({path:'/main'})
      }).catch((err)=>{
        console.log(err)
      })
    }
  },
  created: function () {
    this.getMyName()
  },
};
</script>

<style type="text/css" scoped>
#Myinfo {
  margin-left: 200px;
  margin-top: 100px;
}
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:#ffffff;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:#ffffff;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-gvcd{background-color:#ffffff;border-color:#ffffff;color:#000000;font-size:24px;text-align:center;vertical-align:top;vertical-align:middle}
</style>
