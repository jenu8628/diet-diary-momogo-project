<template>
  <div>
    <div
      style="margin-left: 17vw; margin-top: 17vh; width: 80vw"
      v-if="foodlength > 1"
    >
      <!-- 내가 만들어나갈 부분 -->
      <div style="margin-top: 15vh; width: 75vw">
        <div
          style="
            width: 75vw;
            height: 6vh;
            position: absolute;
            left: 17.8vw;
            top: 100px;
          "
        >
          <v-btn class="goback" @click="toOriginal">처음으로</v-btn>
          <v-btn class="find" @click="excluderice" :disabled="this.check[0]">밥싫어!</v-btn>
          <v-btn class="find" @click="excludesoup" :disabled="this.check[1]">국싫어!</v-btn>
          <v-btn class="find" @click="excludefried" :disabled="this.check[2]">튀김싫어!</v-btn>
          <v-btn class="find" @click="excludechina" :disabled="this.check[3]">중식싫어!</v-btn>
          <v-btn class="find" @click="excludejapan" :disabled="this.check[4]">일식싫어!</v-btn>
          <v-btn class="find" @click="excludesnack" :disabled="this.check[5]">간식싫어!</v-btn>
          <v-btn class="find" @click="excludenoodle" :disabled="this.check[6]">면싫어!</v-btn>
          <v-btn class="find" @click="excludehot" :disabled="this.check[7]">매운거싫어!</v-btn>
          <v-btn class="find" @click="excludesalad" :disabled="this.check[8]">샐러드싫어!</v-btn>
          <v-btn class="find" @click="excludewest" :disabled="this.check[9]">양식싫어!</v-btn>
          <v-btn class="find" @click="excludebbq" :disabled="this.check[10]">고기구이싫어!</v-btn>
          <v-btn class="find" @click="excludeheat" :disabled="this.check[11]">볶음,찜싫어!</v-btn>
          <v-btn class="find" @click="excludesalt" :disabled="this.check[12]">짠거싫어!</v-btn>
          <v-btn class="find" @click="excludesea" :disabled="this.check[13]">바다싫어!</v-btn>
          <v-btn class="find" @click="excludepig" :disabled="this.check[14]">돼지싫어!</v-btn>
          <v-btn class="find" @click="excludecow" :disabled="this.check[15]">소싫어!</v-btn>
          <v-btn class="find" @click="excludebird" :disabled="this.check[16]">새싫어!</v-btn>
        </div>

        <transition-group
          tag="ul"
          class="list"
          style="position: absolute; left: 16vw; top: 250px"
        >
          <li
            v-for="(fooditem, index) in filteredFoodList"
            :data-index="index"
            :key="fooditem"
            class="item"
            @click="doRemoveFood(fooditem)"
          >
            {{ fooditem }}
          </li>
        </transition-group>
      </div>
    </div>
    <div v-if="foodlength === 0">
      <div
        class="final0"
        style="position:absolute; left:20vw; top:20vh; font-family: 'Do Hyeon', sans-serif;"
      >
        <h1 style="font-size:5em">까다로운 분이시군요,,,,</h1>
        <h1 style="font-size:5em">아쉽지만 모든 후보가 사라져버렸습니다.</h1>
        <h1 style="font-size:5em">굶으세요</h1>
      </div>
      <div style="position:absolute; left:20vw; top:65vh;" class="refresh">
        <v-btn icon color="success" x-large @click="toOriginal">
          <v-icon style="color:blue !important;">mdi-cached</v-icon>
        </v-btn>
        <p style="font-family: 'Do Hyeon', sans-serif; font-size:1.1em;">싫으면ㄱ</p>
      </div>
    </div>

    <div v-if="foodlength === 1">
      <div
        class="final0"
        style="position:absolute; left:20vw; top:20vh; font-family: 'Do Hyeon', sans-serif;"
      >
        <h1 style="font-size:5em">축하합니다!</h1>
        <h1 style="font-size:5em">당신이 오늘 먹게 될 음식은,,,</h1>
        <h1 style="font-size:5em">{{ this.foodlist[0]}} 입니다!</h1>
      </div>
      <div style="position:absolute; left:20vw; top:65vh;" class="refresh">
        <v-btn icon color="success" x-large @click="toOriginal">
          <v-icon style="color:blue !important;">mdi-cached</v-icon>
        </v-btn>
        <p style="font-family: 'Do Hyeon', sans-serif; font-size:1.1em;">싫으면ㄱ</p>
      </div>
    </div>
  </div>
</template>

<script>
import foodlist from "./SuggestData/suggest";
import originalfoodlist from "./SuggestData/originalsuggest";
import norice from "./SuggestData/밥싫어";
import nosoup from "./SuggestData/국싫어";
import nofried from "./SuggestData/튀김싫어";
import nochina from "./SuggestData/중식싫어";
import nojapan from "./SuggestData/일식싫어";
import nosnack from "./SuggestData/간식싫어";
import nonoodle from "./SuggestData/면싫어";
import nohot from "./SuggestData/매운거싫어";
import nosalad from "./SuggestData/샐러드싫어";
import nowest from "./SuggestData/양식싫어";
import nobbq from "./SuggestData/고기구이싫어";
import noheat from "./SuggestData/볶음찜싫어";
import nosalt from "./SuggestData/짠거싫어";
import nosea from "./SuggestData/바다싫어";
import nopig from "./SuggestData/돼지싫어";
import nocow from "./SuggestData/소싫어";
import nobird from "./SuggestData/새싫어";

export default {
  data() {
    return {
      current: false,
      originalfoodlist: originalfoodlist,
      foodlist: foodlist,
      norice: norice,
      nosoup: nosoup,
      nofried: nofried,
      nochina: nochina,
      nojapan: nojapan,
      nosnack: nosnack,
      nonoodle: nonoodle,
      nohot: nohot,
      nosalad: nosalad,
      nowest: nowest,
      nobbq: nobbq,
      noheat: noheat,
      nosalt: nosalt,
      nosea: nosea,
      nopig: nopig,
      nocow: nocow,
      nobird: nobird,
      check: [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
    };
  },
  created() {
    this.foodlist = this.originalfoodlist.slice(0);
    // const count = this.foodlist.length;
    // console.log(count);
  },
  computed: {
    // filteredList() {
    //   return this.list.filter(el => el % this.current === 0)
    // },
    filteredFoodList() {
      return this.foodlist;
    },
    foodlength() {
      return this.foodlist.length;
      // console.log(foodl)
    },
  },

  methods: {
    doRemoveFood(fooditem) {
      this.foodlist.splice(this.foodlist.indexOf(fooditem), 1);
      console.log(this.foodlist.length);
    },
    toOriginal() {
      this.foodlist = this.originalfoodlist.slice(0);
      for (let i = 0; i <17; i++) {
        if (this.check[i] === true) {
          this.check[i] = false;
        }
      }
      
    },
    excluderice() {
      console.log(norice);
      for (let i = 0; i < this.norice.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j] === this.norice[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[0] = true
    },
    excludesoup() {
      for (let i = 0; i < this.nosoup.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nosoup[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[1] = true
    },
    excludefried() {
      for (let i = 0; i < this.nofried.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nofried[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[2] = true
    },
    
    excludechina() {
      for (let i = 0; i < this.nochina.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nochina[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[3] = true
    },
    excludejapan() {
      for (let i = 0; i < this.nojapan.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j].includes(this.nojapan[i])) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[4] = true
    },
    excludesnack() {
      for (let i = 0; i < this.nosnack.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nosnack[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[5] = true
    },
    excludenoodle() {
      for (let i = 0; i < this.nonoodle.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nonoodle[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[6] = true
    },
    excludehot() {
      for (let i = 0; i < this.nohot.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nohot[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[7] = true
    },
    excludesalad() {
      for (let i = 0; i < this.nosalad.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nosalad[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[8] = true
    },
    excludewest() {
      for (let i = 0; i < this.nowest.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nowest[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[9] = true
    },
    excludebbq() {
      for (let i = 0; i < this.nobbq.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nobbq[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[10] = true
    },
    excludeheat() {
      for (let i = 0; i < this.noheat.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.noheat[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[11] = true
    },
    excludesalt() {
      for (let i = 0; i < this.nosalt.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nosalt[i]) {
            console.log(foodlist[j]);
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[12] = true
    },
    excludesea() {
      for (let i = 0; i < this.nosea.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nosea[i]) {
            console.log(foodlist[j]);
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[13] = true
    },
    excludepig() {
      for (let i = 0; i < this.nopig.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nopig[i]) {
            console.log(foodlist[j]);
            console.log(nopig[i])
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[14] = true
    },
    excludecow() {
      for (let i = 0; i < this.nocow.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nocow[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[15] = true
    },
    excludebird() {
      for (let i = 0; i < this.nobird.length; i++) {
        for (let j = 0; j < this.foodlist.length; j++) {
          if (this.foodlist[j]===this.nobird[i]) {
            this.foodlist.splice(j, 1);
          }
        }
      }
      this.check[16] = true
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding:wght@700&display=swap');
.list {
  width: 80vw;
  padding: 0;
  /* margin-bottom: 2vh; */
}
.item {
  font-size: 0.8em;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 2vh;
  margin-right: 0.5vw;
  width: 50px;
  min-width: 120px;
  height: 4vh;
  min-height: 25px;
  background: #ece8e2;
}

/* 트랜지션 전용 스타일 */
.v-enter-active,
.v-leave-active,
.v-move {
  transition: opacity 1s, transform 1s;
}
.v-leave-active {
  position: absolute;
}
.v-enter {
  opacity: 0;
  transform: translateY(-20px);
}
.v-leave-to {
  opacity: 0;
  transform: translateY(20px);
}



.final0 {
  display: inline-block;
  /* background: yellow; */
  padding: 10px;
  animation: fadein 1s;
  -moz-animation: fadein 1s; /* Firefox */
  -webkit-animation: fadein 1s; /* Safari and Chrome */
  -o-animation: fadein 1s; /* Opera */
}
.refresh {
  display: inline-block;
  /* background: yellow; */
  padding: 10px;
  animation: fadein 5s;
  -moz-animation: fadein 5s; /* Firefox */
  -webkit-animation: fadein 5s; /* Safari and Chrome */
  -o-animation: fadein 5s; /* Opera */
}
@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-moz-keyframes fadein {
  /* Firefox */
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadein {
  /* Safari and Chrome */
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-o-keyframes fadein {
  /* Opera */
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.find {
  margin-right:0.9vw;
  margin-bottom:8px;
  width:7.2vw;
  background-color:rgb(198, 186, 212) !important;
  /* font-family: 'Do Hyeon', sans-serif !important; */
  font-family: 'Nanum Gothic Coding', monospace;
  font-size:15px;
}
.goback {
  margin-right:0.9vw;
  margin-bottom:8px;
  width:7.2vw;
  background-color:rgb(229, 182, 184) !important;
  /* font-family: 'Do Hyeon', sans-serif !important; */
  font-family: 'Nanum Gothic Coding', monospace;
  font-size:15px;
}
</style>