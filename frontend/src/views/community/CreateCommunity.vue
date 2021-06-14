<template>
  <div class="all">
    <div>
    <label for="title">title:    </label>
    <input type="text" v-model="title">
    </div>
    <div>
    <label for="content">content: </label>
    <textarea name="content" id="content" cols="30" rows="10" v-model="content"></textarea>
    </div>
    <b-button variant="outline-info" @click="createCommunity">글쓰기</b-button>
  </div>
  
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateCommunity',
  data () {
    return {
      title: '',
      content: '',
    }
  },
  methods: { 
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    createCommunity () {
      const config = this.setToken()

      const communityItem = {
        title: this.title,
        content: this.content,
      }

      if (communityItem.title) {
        axios.post(`${SERVER_URL}/communities/`, communityItem, config)
          .then(() => {
            // console.log(res)
            this.$router.push({ name: 'Community' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Single+Day&display=swap');
  .all {
  font-family: 'Single Day', cursive;
  font-size: 1.5em;
  margin-left: 400px;
  margin-top: 150px;
  }

</style>