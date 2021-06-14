<template>

  <div class="font">
    <div class="margin_1">
      <h2>Community</h2>
      <!-- style="float:right; margin-right: 340px" -->
      <div class="box">
        <router-link class="router" to="/createcommunity">글쓰기</router-link>
      </div>
    </div>
    

    <table class="margin_2">
      <tr>
        <th>NO</th>
        <th>TITLE</th>
        <th>NAME</th>
        <th>DATE</th>
      </tr>
      <tr class="hov" v-for="(community, idx) in currentCommunity" :key="idx" @click="detail(community.id)">
        <th style="color:#3b6566">{{ community.id }}</th>
        <!-- <th style="color:#3b6566">{{ community.title }}</th> -->
        <th style="color:#3b6566">{{ community.title }}</th>
        <th style="color:#3b6566">{{ community.user.nickname }}</th>
        <th style="color:#3b6566">{{ community.created_at.slice(2,4)}}{{community.created_at.slice(4)}}</th>
      </tr>
    </table>
      <div class="margin_2 bbttnn">
        <p @click="prev">prev</p>
        <p @click="pageNation(num)" v-for="(num, index) in currentPageNum" :key="index">
          {{num}}
        </p>
        <p @click="next">next</p>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'Community',
  data () {
    return {
      pageNum : [],
      currentPageNum: [],
      communities: [],
      currentCommunity: [],
    }
  },
  methods: {
    detail (event) {
      this.$router.push({name: 'CommunityDetail', params: {community_id: event}})
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getCommunities () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/communities/`, config)
      .then((res) => {
        this.communities = res.data
        for (let i = 0 ; i < this.communities.length; i++){
          this.communities[i].created_at = this.communities[i].created_at.slice(0,10)
        }
        this.pageNation(1)
        for (let i=0; i<this.communities.length / 10; i++){
          this.pageNum.push(i+1)
          }
        for (let j = 1; j < 6; j++){
          this.currentPageNum.push(j)
          if (j === this.pageNum.length)break
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    pageNation (event) {
      this.currentCommunity = []
      const num = parseInt(event) - 1
      for (let i = 0; i<10; i++) {
        let idx = i + (10*num)
        if (idx === this.communities.length) break;
        this.currentCommunity.push(this.communities[idx])
      }
    },
    next() {
      const index = this.currentPageNum.length - 1
      const idx = this.currentPageNum[index]
      const lastIndex = this.pageNum.length - 1
      if (idx !==  this.pageNum[lastIndex]) {
        this.currentPageNum = []
        for (let i = idx+1; i < idx + 6; i++) {
          this.currentPageNum.push(i)
          if (i === this.pageNum[lastIndex]) break
        }
        this.currentCommunity = []
        for (let i = 0; i<10; i++) {
          let inedex = i + (10*(this.currentPageNum[0]-1))
          if (inedex === this.communities.length) break;
          this.currentCommunity.push(this.communities[inedex])
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
        this.currentCommunity = []
        for (let i = 0; i<10; i++) {
          let idx = i + (10*(this.currentPageNum[0]-1))
          this.currentCommunity.push(this.communities[idx])
        }
      }
    },
  },
  mounted() {
    this.getCommunities()
  }, 
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Single+Day&display=swap');
.font {
  position: absolute;
  font-family: 'Single Day', cursive;
  font-size:1.2rem;
  top: 15vh;
  left: 20vw;
  width: 70vw
}
.td_datetime {
    width: 110px;
    text-align: center;
}

table {
  width: 100%;
  height: 80%;
  /* margin: auto; */
  text-align: center;
}

tr {
  border-bottom: 1px solid black;
}
.hov:hover {
  background: rgb(222, 235, 233);
  cursor: pointer;
}
.margin_1 h2{
  display: flex;
  justify-content: center;
}
/* .margin_2 {
  margin-left: 350px;
  margin-top: 20px;
} */
.box {
  display: flex;
  justify-content: flex-end;
}
.router{
  text-decoration:none;
  color:#29c9cc;
}
.bbttnn {
  display: flex;
  justify-content: center;
  margin-top:1em;
  font-size: 1.2em;
}
.bbttnn:hover {
  cursor: pointer;
}
.bbttnn p {
  position: relative;
  display: inline-block;
  margin-left: 1.2em;
}
</style>