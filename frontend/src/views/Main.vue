<template>
  <section class="container">
    <div class="columns" style="width:30vw;">
      <div class="column" style="margin-left: 7vw; margin-top: 20vh; width:30px; height:40vh;">
        <div style="width: 30vw; height: 50vh; position:absolute; ">
          <p class="mainCaption">
            {{user.nickname}}님의<br>일주일간 칼로리 섭취 추이
          </p>
          <br>
          <line-chart
            style="width: 30vw; height: 50vh; min-height: 20px !important"
          ></line-chart>
        </div>

        <div style="position: absolute; top:21.5vh; right:12vw; width: 30vw; height: 50vh;">
          <p class="mainCaption">
            오늘 영양 섭취 현황
          </p>
          <br>

          <!-- 표에 해당하는 부분 -->
          <div id="graph">
            <v-app id="inspire">
              <v-simple-table>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left" style="border-top:1px solid; font-size:1em;">
                        항목
                      </th>
                      <th class="text-left" style="border-top:1px solid; border-left:1px solid; border-right:1px solid; font-size:1em;">
                        1일권장량
                      </th>
                      <th class="text-left" style="border-top:1px solid; font-size:1em;">
                        섭취량
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td class="text-left">
                        열량
                      </td>
                      <td class="text-left" style="border-left:1px solid; border-right:1px solid">
                        {{ calSuggest }} Kcal
                      </td>
                      <td class="text-left">
                        {{cal}} Kcal
                      </td>
                    </tr>
                    <tr>
                      <td class="text-left">
                        탄수화물
                      </td>
                      <td class="text-left" style="border-left:1px solid; border-right:1px solid">
                        {{ carbSuggest }} g
                      </td>
                      <td class="text-left">
                        {{carb}} g
                      </td>
                    </tr>
                    <tr>
                      <td class="text-left">
                        단백질
                      </td>
                      <td class="text-left" style="border-left:1px solid; border-right:1px solid">
                        {{ proteinSuggest }} g
                      </td>
                      <td class="text-left">
                        {{protein}} g
                      </td>
                    </tr>
                    <tr>
                      <td class="text-left" style="border-bottom:1px solid;">
                        지방
                      </td>
                      <td class="text-left" style="border-bottom:1px solid; border-left:1px solid; border-right:1px solid">
                        {{ fatSuggest }} g
                      </td>
                      <td class="text-left" style="border-bottom:1px solid;">
                        {{ fat }} g
                      </td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-app>
          </div>

        </div>
      </div>
    </div>
  </section>
</template>



<script>
import LineChart from "@/components/LineChart";
import axios from 'axios';
import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: "VueChartJS",
  data() {
    return {
      calSuggest : 0,
      carbSuggest : 0, //탄수화물 일일권장량
      proteinSuggest : 0,
      fatSuggest : 0,
      cal: 0,
      carb : 0,
      protein: 0,
      fat:0,
      user: {},
    }
  },
  components: {
    LineChart,
  },
  mounted() {
    this.getToken()
    this.getUserInfo()
    this.getToday()
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
    getUserInfo () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then((res)=>{
        this.user = res.data
        const weight = parseInt(res.data.weight)
        this.carbSuggest = weight * 5
        if (res.data.sex === "man"){
          if (parseInt(res.data.age) < 30){
            this.calSuggest = 2600
            this.proteinSuggest= 125
            this.fatSuggest = 56
          }else {
            this.calSuggest = 2400
            this.proteinSuggest= 110
            this.fatSuggest = 51
          }
        }else {
          if (parseInt(res.data.age) < 30){
            this.calSuggest = 2100
            this.proteinSuggest= 100
            this.fatSuggest = 48
          }else {
            this.calSuggest = 1900
            this.proteinSuggest= 94
            this.fatSuggest = 42
          }
        }
      }).catch((err)=> {
        console.log(err)
      })
    },
    getToday () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      const date = this.$moment().format('YYYY-MM-DD')
      axios.get(`${SERVER_URL}/foods/${info.user_id}/get_userFood/`, config)
      .then((res)=>{
        for (let i = 0; i < res.data.length; i++){
          if (res.data[i].created_at.slice(0,10) === date){
            this.cal += res.data[i].kcal
            this.carb += res.data[i].carbohydrate
            this.protein += res.data[i].protein
            this.fat += res.data[i].fat
          }
        }
      }).catch((err)=>{
        console.log(err)
      })
    }
  },
};
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Single+Day&display=swap');
  .container{
    font-family: 'Single Day', cursive;
  }
  td {
    height: 9vh !important;
  }

  .mainCaption {
    justify-content: center;
    text-align: center;
    font-size: 1.4em;
  }

</style>