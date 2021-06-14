<template>
  <div class="container">
    <div class="box">
      <!--밑에는 식품정보 뜨는 칸! -->
      <div class="tit">
        <p class="name">식품이름</p>
        <p class="kcal">칼로리</p>
        <p class="amount">1회 제공량</p>
      </div>
      <hr style="margin-top: 5">
      <div @click="modalopen(food)" class="tit hov" v-for="(food, index) in foodNow" :key="index">
          <p class="name">{{ food.식품명 }}</p>
          <p class="kcal">{{ food.에너지 }}kcal</p>
          <p class="amount">{{ food.제공량 }} {{ food.단위}}</p>
          <!-- <button @click="foodContain(food)">담기</button> -->
      </div>
      <hr>
      <div class="bbttnn">
        <button @click="prev">prev</button>
        <button @click="pageNation(num)" v-for="(num, i) in currentPageNum" :key="i">{{num}}</button>
        <button @click="next">next</button>
      </div>
    </div>
    <!-- 여기밑으로 모달 -->
    <div v-if="modal" class="food-modal">
      <div class="food-box">
        <div class="food-box-title">
          식단에 음식 담기
        </div>
        <br>
        <div class="amount" style="font-size:1.2em;">
          먹은양을 입력하세요 : <input class="input-style" type="text" v-model="foodAmount" style="text-align: center;"> {{modalFood.단위}}
          <select v-model="meal" name="food" id="food">
            <option value="">선택</option>
            <option value="아침">아침</option>
            <option value="점심">점심</option>
            <option value="저녁">저녁</option>
            <option value="간식">간식</option>
            <!-- <option @click="Time('아침')">아침</option>
            <option @click="Time('점심')">점심</option>
            <option @click="Time('저녁')">저녁</option>
            <option @click="Time('간식')">간식</option> -->
          </select>
        </div>
        <div class="food-mid">
          <div class="food-box-content-title">
            <p>식품명</p>
            <p>칼로리</p>
            <p>단백질</p>
            <p>탄수화물</p>
            <p>지방</p>
          </div>
          <div class="food-box-content">
            <p>{{modalFood.식품명}} </p>
            <p>{{(modalFood.에너지/modalFood.제공량 *foodAmount).toFixed(2)}} kcal </p>
            <p>{{(modalFood.단백질/modalFood.제공량 *foodAmount).toFixed(2)}} </p>
            <p>{{(modalFood.탄수화물/modalFood.제공량 *foodAmount).toFixed(2)}} </p>
            <p>{{(modalFood.지방/modalFood.제공량 *foodAmount).toFixed(2)}} </p>
          </div>
        </div>

        <div class="but">
          <button @click="foodContain(modalFood)" class="a">식단에담기</button>
          <button @click="modalopen">닫기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import foodInfo from '@/foodInfo.json'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data () {
    return {
      foodAmount: 0,
      foodInfo : foodInfo, // 전체 푸드들의 정보
      foodTitle : this.$route.query.title, // 검색어 정보
      foods : [], // 검색어와 일치하는 모든 푸드들
      foodNow : [],
      pageNum : [], // 페이지네이션 넘버들
      currentPageNum: [], // 현재 페이지네이션 넘버들
      modal: false, //모달 오픈 닫기기능 할 놈
      modalFood: [],
      meal:"",
    }
  },
  computed: {
  },
  created () {
  },
  mounted() {
    // 검색어와 일치하는 food들을 this.foods에 담는다
    // 1번째 방법
    // for (let i = 0; i <this.foodInfo.length; i++){
    //   if (this.foodInfo[i].식품명.includes(this.foodTitle)){
    //     this.foods.push(this.foodInfo[i])
    //   }
    // }
    //2번째 방법
    this.foods = this.foodInfo.filter((data) => {
      return data.식품명.includes(this.foodTitle)
    })
    // 이것은 제외하고 가져오는 방법!
    // this.foods = this.foodInfo.filter((data) => {
    //   return data.식품명.includes(this.foodTitle)
    // })

    // 검색어와 일치하는 푸드들을 10개씩 보여줄건데 그에 대한 페이지네이션 갯수 구하기
    for (let i = 0; i < this.foods.length / 10; i++) {
      this.pageNum.push(i+1)
    }
    // 첫페이지 페이지네이션 숫자들
    for (let j = 1; j < 6; j++){
      this.currentPageNum.push(j)
      if (j === this.pageNum.length)break
    } 
    this.pageNation(1) // 첫번째 페이지 보여주기 위함.
  },
  methods: {
    pageNation (event) {
      this.foodNow = []
      const num = parseInt(event) - 1
      for (let i = 0; i < 10; i ++){
        let idx = i + (10*num)
        if (idx === this.foods.length) break;
        this.foodNow.push(this.foods[idx])
      }
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization : `JWT ${token}`,
        }
      }
      return config
    },
    modalopen (event) {
      this.modalFood = event
      this.foodAmount = event.제공량
      this.modal= !this.modal
    },
    foodContain (event) {
      const config = this.setToken()
      const amount = parseInt(this.foodAmount)
      const foodSelect = {
        time : this.meal,
        foodName: event.식품명,
        amount : Math.round(amount),
        kcal :Math.round((parseInt(event.에너지)/parseInt(event.제공량))*amount),
        carbohydrate : Math.round(parseInt(event.탄수화물)/parseInt(event.제공량)*amount),
        protein : Math.round(parseInt(event.단백질)/parseInt(event.제공량)*amount),
        fat : Math.round(parseInt(event.지방)/parseInt(event.제공량)*amount),
        unit : this.modalFood.단위,
        natrium : Math.round(parseInt(this.modalFood.나트륨)/parseInt(event.제공량)*amount),
        sugars : Math.round(parseInt(this.modalFood.총당류)/parseInt(event.제공량)*amount),
      }
        //parseInt("15")
        //Number("15")
        // "15"*1 = 숫자로 자동형변환
      axios.post(`${SERVER_URL}/foods/`,foodSelect, config)
      .then(() => {
        this.modal= !this.modal
        this.meal = ""
        alert(event.식품명 +'을(를) 담았습니다.')
      })
      .catch((err) => {
        if (this.meal==="") {
          alert('식사시간을 선택하세요!')
        }
        console.log(err)
      })
    },
    // 검색한 단어 들어가있으면 담는 함수
    // calData() {
    //   this.foods = this.foodInfo.filter((data) => {
    //     return data.식품명.includes(this.foodTitle)
    //   }).slice(0);
    // },
    next () {
      const index = this.currentPageNum.length - 1
      const idx = this.currentPageNum[index]
      const lastIndex = this.pageNum.length - 1
      if (idx !== this.pageNum[lastIndex]) {
        this.currentPageNum = []
        for (let i = idx+1; i < idx + 6; i++) {
          this.currentPageNum.push(i)
          if (i === this.pageNum[lastIndex]) break
        }
        this.foodNow = []
        for (let i = 0; i<10; i++) {
          let idx = i + (10*(this.currentPageNum[0]-1))
          if (idx === this.foods.length) break;
          this.foodNow.push(this.foods[idx])
        }
      }
    },
    prev () {
      const index = this.currentPageNum[0] // 6 맨앞의 숫자
      if (index !== this.pageNum[0]) {
        this.currentPageNum = []
        for (let i = index-5; i < index; i++) {
          this.currentPageNum.push(i)
        }
        this.foodNow = []
        for (let i = 0; i<10; i++) {
          let idx = i + (10*(this.currentPageNum[0]-1))
          this.foodNow.push(this.foods[idx])
        }
      }
    },
  },
}
</script>

<style scoped>
/* @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;900&display=swap");
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gaegu&display=swap'); */
@import url('https://fonts.googleapis.com/css2?family=Single+Day&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300&display=swap');
.container {
  position: absolute;
  font-family: 'Noto Serif KR', serif;
  /* font-family: 'Do Hyeon', sans-serif; */
  /* font-family: 'Single Day', cursive; */
  font-size: 1.3 em;
  top:10vh;
  left: 16vw;
  max-width: 77vw;
  
}
/* .box {
  max-width: 65vw;
} */
div p {
  margin-bottom: 0;
  overflow: hidden;
  white-space:nowrap;
  text-overflow:ellipsis;
}
.tit {
  display: flex;
  align-content: center;
}
.name {
  /* border-right: 2px solid black; */
  display: block;
  overflow: hidden;
  white-space:nowrap;
  text-overflow:ellipsis;
  width:28vw;
  margin-left: 5vw;
  margin-bottom: 2vh;
  font-size: 1.4em;
}
.amount{
  overflow: hidden;
  white-space:nowrap;
  text-overflow:ellipsis;
  font-size: 1.4em;
  /* margin-bottom: 10px; */

}
.kcal {
  overflow: hidden;
  white-space:nowrap;
  text-overflow:ellipsis;
  width: 23vw;
  font-size: 1.4em;

}
.bbttnn {
  margin-top:2em;
  display: flex;
  justify-content: center;
}
.bbttnn button {
  margin-right: 3vw;
  font-size:1.2em;
}
hr{
  margin: 0;
}
.hov:hover {
  color: rgb(124, 194, 164);
  cursor: pointer;
}
.food-modal{
  display: flex;
  justify-content: center;
  align-content: center;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 50%;
  left: 45%;
  transform: translate(-50%, -50%) scale(1);
  backdrop-filter: saturate(180%) blur(3px);
}
.food-box {
  margin-top:7em;
  width: 50%;
  height: 70%;
  background: rgb(255, 255, 255);
  border:solid 1px;
  /* background: rgb(202, 231, 215); */
  border-radius: 0.5em;
}
.food-box-title{
  margin-top: 1em;
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  font-size: 1.5em;
}
.food-mid {
  background: rgb(231, 242, 243);
  width: 100%;
  position: relative;
  display: flex;
  margin-top:3vh;
  margin-bottom:5vh;
  height:27vh;
  min-height: 160px !important;
}
.food-box-content{
  padding-top: 0.5vh;
  margin: 1em 0;
  display: inline-block;
  position: relative;
  width: 50%;
  height: 100%;
  padding-left: 10%;
  overflow: hidden;
  white-space:nowrap;
  text-overflow:ellipsis;
  font-size: 1.2em;
}
.food-box-content-title{
  padding-top: 0.5vh;
  margin: 1em 0;
  display: inline-block;
  padding-left: 15%;
  position: relative;
  width: 50%;
  height: 100%;
  font-size: 1.2em;
}
.but{
  display: flex;
  margin-top: 1vw;
  margin-right: 1.2em;
  font-size: 1.2em;
}
.a{
  margin-left: auto;
  margin-right: 2em;
}
.input-style{
  border:solid 1px;
  width:7vw; 
  margin-left: 0.5vw;
  margin-right: 0.5vw;
  border-radius: 0.3em;
}
.amount {
  font-size: 1.4em;
  display: flex;
  /* margin: 0.5em; */
  justify-content: center;
}
.amount select{
  width: 5vw;
  margin-left: 1em;
  border-radius: 0.3em;
}
@media(max-width: 900px) {
  .food-box {
    width: 70%;
  }
}

.food-box-content-title p{
  line-height: 4.5vh;
}

.food-box-content p{
  line-height: 4.5vh;
}
</style>