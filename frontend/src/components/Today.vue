<template>
  <div id="app">
    <v-app id="inspire">
      <table
        class="tg"
        style="undefined;table-layout: fixed; width: 1300px; margin-top: 100px; margin-left: 200px"
      >
        <colgroup>
          <col style="width: 1300px" />
        </colgroup>
        <thead>
          <tr>
            <th class="tg-hrrh">
              <h2>Today 총 섭취량 : {{breakfastCal + lunchCal + dinnerCal + dessertCal}} Kcal </h2>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="tg-hrrh">
              <!-- 아침     -->
              <v-data-table
                :headers="Breakfast"
                :items="breakfasts"
                :items-per-page="5"
                class="elevation-1"
                dense
              >
                <template v-slot:top>
                  <v-toolbar flat>
                    <v-toolbar-title>아침 총 섭취량: {{ breakfastCal }} Kcal </v-toolbar-title>
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-spacer></v-spacer>
                    <v-dialog
                      v-model="breakfasts_dialogDelete"
                      max-width="500px"
                    >
                      <v-card>
                        <v-card-title class="headline"
                          >Are you sure you want to delete this
                          item?</v-card-title
                        >
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="breakfasts_closeDelete"
                            >Cancel</v-btn
                          >
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="breakfasts_deleteItemConfirm"
                            >OK</v-btn
                          >
                          <v-spacer></v-spacer>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                  <v-icon small @click="breakfasts_deleteItem(item)">
                    mdi-delete
                  </v-icon>
                </template>
              </v-data-table>

              <!-- 아침    -->
            </td>
          </tr>
          <tr>
            <td class="tg-hrrh">
              <!-- 점심     -->
              <v-data-table
                :headers="Lunch"
                :items="lunchs"
                :items-per-page="5"
                sort-by="calories"
                class="elevation-1"
                dense
              >
                <template v-slot:top>
                  <v-toolbar flat>
                    <v-toolbar-title>점심 총 섭취량 : {{ lunchCal }} Kcal</v-toolbar-title>
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-spacer></v-spacer>
                    
                    <v-dialog v-model="lunchs_dialogDelete" max-width="500px">
                      <v-card>
                        <v-card-title class="headline"
                          >Are you sure you want to delete this
                          item?</v-card-title
                        >
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="lunchs_closeDelete"
                            >Cancel</v-btn
                          >
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="lunchs_deleteItemConfirm"
                            >OK</v-btn
                          >
                          <v-spacer></v-spacer>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                  <v-icon small @click="lunchs_deleteItem(item)">
                    mdi-delete
                  </v-icon>
                </template>
              </v-data-table>

              <!-- 점심    -->
            </td>
          </tr>
          <tr>
            <td class="tg-hrrh">
              <!-- 저녁     -->
              <v-data-table
                :headers="Dinner"
                :items="dinners"
                :items-per-page="5"
                sort-by="calories"
                class="elevation-1"
                dense
              >
                <template v-slot:top>
                  <v-toolbar flat>
                    <v-toolbar-title>저녁 총 섭취량 : {{dinnerCal}} Kcal </v-toolbar-title>
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-spacer></v-spacer>
                    
                    <v-dialog v-model="dinners_dialogDelete" max-width="500px">
                      <v-card>
                        <v-card-title class="headline"
                          >Are you sure you want to delete this
                          item?</v-card-title
                        >
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="dinners_closeDelete"
                            >Cancel</v-btn
                          >
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="dinners_deleteItemConfirm"
                            >OK</v-btn
                          >
                          <v-spacer></v-spacer>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                  <v-icon small @click="dinners_deleteItem(item)">
                    mdi-delete
                  </v-icon>
                </template>
              </v-data-table>

              <!-- 저녁    -->
            </td>
          </tr>
          <tr>
            <td class="tg-hrrh">
              <!-- 간식     -->
              <v-data-table
                :headers="Dessert"
                :items="desserts"
                :items-per-page="5"
                sort-by="calories"
                class="elevation-1"
                dense
              >
                <template v-slot:top>
                  <v-toolbar flat>
                    <v-toolbar-title>간식 총 섭취량: {{dessertCal}} Kcal </v-toolbar-title>
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-spacer></v-spacer>
                    
                    <v-dialog v-model="desserts_dialogDelete" max-width="500px">
                      <v-card>
                        <v-card-title class="headline"
                          >Are you sure you want to delete this
                          item?</v-card-title
                        >
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="desserts_closeDelete"
                            >Cancel</v-btn
                          >
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="desserts_deleteItemConfirm"
                            >OK</v-btn
                          >
                          <v-spacer></v-spacer>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                  <v-icon small @click="desserts_deleteItem(item)">
                    mdi-delete
                  </v-icon>
                </template>
              </v-data-table>
              <!-- 간식    -->
            </td>
          </tr>
        </tbody>
      </table>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"


const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: "today",
  data() {
    return {
      food : 0,
      breakfasts_dialogDelete: false,
      lunchs_dialogDelete: false,
      dinners_dialogDelete: false,
      desserts_dialogDelete: false,
      breakfastCal: 0,
      lunchCal: 0,
      dinnerCal: 0,
      dessertCal: 0,
      Breakfast: [
        {
          text: "식품명",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "섭취량", value: "intakeSize", sortable: false },
        { text: "단위", value: "unit", sortable: false },
        { text: "칼로리(Kcal)", value: "calories", sortable: false },
        { text: "지방", value: "fat", sortable: false },
        { text: "탄수화물", value: "carbs", sortable: false },
        { text: "단백질", value: "protein", sortable: false },
        { text: "나트륨", value: "salt", sortable: false },
        { text: "당류", value: "sugars", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
      Lunch: [
        {
          text: "Foods",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "섭취량", value: "intakeSize", sortable: false },
        { text: "단위", value: "unit", sortable: false },
        { text: "칼로리(Kcal)", value: "calories", sortable: false },
        { text: "지방", value: "fat", sortable: false },
        { text: "탄수화물", value: "carbs", sortable: false },
        { text: "단백질", value: "protein", sortable: false },
        { text: "나트륨", value: "salt", sortable: false },
        { text: "당류", value: "sugars", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
      Dinner: [
        {
          text: "Foods",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "섭취량", value: "intakeSize", sortable: false },
        { text: "단위", value: "unit", sortable: false },
        { text: "칼로리(Kcal)", value: "calories", sortable: false },
        { text: "지방", value: "fat", sortable: false },
        { text: "탄수화물", value: "carbs", sortable: false },
        { text: "단백질", value: "protein", sortable: false },
        { text: "나트륨", value: "salt", sortable: false },
        { text: "당류", value: "sugars", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
      Dessert: [
        {
          text: "Foods",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "섭취량", value: "intakeSize", sortable: false },
        { text: "단위", value: "unit", sortable: false },
        { text: "칼로리(Kcal)", value: "calories", sortable: false },
        { text: "지방", value: "fat", sortable: false },
        { text: "탄수화물", value: "carbs", sortable: false },
        { text: "단백질", value: "protein", sortable: false },
        { text: "나트륨", value: "salt", sortable: false },
        { text: "당류", value: "sugars", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
      breakfasts: [],
      lunchs: [],
      dinners: [],
      desserts: [],
    }
  },

  computed: {
  },

  watch: {
  },

  created() {
  },

  mounted() {
    this.getFood()
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
    getFood (){
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      const date = this.$moment().format('YYYY-MM-DD')
      axios.get(`${SERVER_URL}/foods/${info.user_id}/get_userFood/`, config)
      .then((res)=>{
        const meal = ["아침", "점심", "저녁", "간식"]
        const mealTime = [this.breakfasts, this.lunchs, this.dinners, this.desserts]

        for (let i = 0; i < res.data.length; i++){
          if (res.data[i].created_at.slice(0,10) === date){
            for (let j=0; j<4; j++){
              if (res.data[i].time === meal[j]) {
                mealTime[j].push(
                  {
                    id : res.data[i].id,
                    name: res.data[i].foodName,
                    intakeSize: res.data[i].amount,
                    unit: res.data[i].unit,
                    calories: res.data[i].kcal,
                    fat: res.data[i].fat,
                    carbs: res.data[i].carbohydrate,
                    protein: res.data[i].protein,
                    salt: res.data[i].natrium,
                    sugars: res.data[i].sugars,
                  }
                )
              }
            }
          }
        }
        this.calori()
      }).catch((err)=>{
        console.log(err)
      })
    },
    deleteCal(event, j){
      if (event === 1) {
        for (let i = 0; i < this.breakfasts.length; i++){
          if (this.breakfasts[i].id ===j) {
            this.breakfastCal -= this.breakfasts[i].calories
          }
        }
      }
      if (event === 2) {
        for (let i = 0; i < this.lunchs.length; i++){
          if (this.lunchs[i].id ===j) {
            this.lunchCal -= this.lunchs[i].calories
          }
        }
      }
      if (event === 3) {
        for (let i = 0; i < this.dinners.length; i++){
          if (this.dinners[i].id ===j) {
            this.dinnerCal -= this.dinners[i].calories
          }
        }
      }
      if (event === 4) {
        for (let i = 0; i < this.desserts.length; i++){
          if (this.desserts[i].id ===j) {
            this.dessertCal -= this.desserts[i].calories
          }
        }
      }
    },
    calori () {
      if (this.breakfasts) {
        for (let i = 0; i < this.breakfasts.length; i++){
          this.breakfastCal += this.breakfasts[i].calories
        }
      }
      if (this.lunchs) {
        for (let i = 0; i < this.lunchs.length; i++){
          this.lunchCal += this.lunchs[i].calories
        }
      }
      if (this.dinners) {
        for (let i = 0; i < this.dinners.length; i++){
          this.dinnerCal += this.dinners[i].calories
        }
      }
      if (this.desserts) {
        for (let i = 0; i < this.desserts.length; i++){
          this.dessertCal += this.desserts[i].calories
        }
      }
    },

    breakfasts_deleteItem(item) {
      this.breakfasts_dialogDelete = true;
      this.foodId = item.id
    },

    breakfasts_deleteItemConfirm() {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/foods/${this.foodId}/delete/`, config)
      .then(()=>{
        this.deleteCal(1, this.foodId)
        this.breakfasts = this.breakfasts.filter((data)=>data.id !== this.foodId)
        this.breakfasts_closeDelete();
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    breakfasts_closeDelete() {
      this.breakfasts_dialogDelete = false;
    },


    lunchs_deleteItem(item) {
      this.lunchs_dialogDelete = true;
      this.foodId = item.id
    },

    lunchs_deleteItemConfirm() {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/foods/${this.foodId}/delete/`, config)
      .then(()=>{
        this.deleteCal(2, this.foodId)
        this.lunchs = this.lunchs.filter((data)=>data.id !== this.foodId)
        this.lunchs_closeDelete();
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    lunchs_closeDelete() {
      this.lunchs_dialogDelete = false;
    },

    dinners_deleteItem(item) {
      this.dinners_dialogDelete = true;
      this.foodId = item.id
    },

    dinners_deleteItemConfirm() {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/foods/${this.foodId}/delete/`, config)
      .then(()=>{
        this.deleteCal(3, this.foodId)
        this.dinners = this.dinners.filter((data)=>data.id !== this.foodId)
        this.dinners_closeDelete();
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    dinners_closeDelete() {
      this.dinners_dialogDelete = false;
    },

    desserts_deleteItem(item) {
      this.desserts_dialogDelete = true;
      this.foodId = item.id
    },

    desserts_deleteItemConfirm() {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/foods/${this.foodId}/delete/`, config)
      .then(()=>{
        this.deleteCal(4, this.foodId)
        this.desserts = this.desserts.filter((data)=>data.id !== this.foodId)
        this.desserts_closeDelete();
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    desserts_closeDelete() {
      this.desserts_dialogDelete = false;
    },

  },
};
</script>

<style type="text/css" scoped>
.tg {
  border-collapse: collapse;
  border-spacing: 0;
}
.tg td {
  border-color: black;
  border-style: solid;
  border-width: 1px;
  font-family: Arial, sans-serif;
  font-size: 14px;
  overflow: hidden;
  padding: 10px 5px;
  word-break: normal;
}
.tg th {
  border-color: black;
  border-style: solid;
  border-width: 1px;
  font-family: Arial, sans-serif;
  font-size: 14px;
  font-weight: normal;
  overflow: hidden;
  padding: 10px 5px;
  word-break: normal;
}
.tg .tg-nu5p {
  background-color: #ffffff;
  border-color: #000000;
  color: #000000;
  text-align: left;
  vertical-align: top;
}
</style>
