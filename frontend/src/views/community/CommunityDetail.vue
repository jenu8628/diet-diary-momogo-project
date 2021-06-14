<template>
  <div class="detailMargin">
    <br>
    <h1>{{ community.title }}</h1>
    created at: {{ $moment(community.created_at).format('YY-MM-DD HH:mm') }} | updated at: {{ $moment(community.updated_at).format('YY-MM-DD HH:mm') }} | {{ community.user.nickname }}
    <br>
    <br>
    <h5 class="container">{{ community.content }}</h5>
    <span v-if="this.username === community.user.username">
      <b-button variant="outline-danger" @click="deleteCommunity">삭제</b-button> <b-button variant="outline-success" @click="moveToUpdateCommunity">수정</b-button> <router-link to="/community"><b-button variant="outline-primary">뒤로</b-button></router-link>
    </span>
    <span v-else>
      <router-link to="/community"><b-button variant="outline-primary">뒤로</b-button></router-link>
    </span>
    <br>
    <br>
    <hr>
    <Comments @createComment="createComment" />
    <CommentsList :comments="comments" :username="username" @deleteComment="deleteComment" />
  </div>
</template>

<script>
import axios from'axios'
import Comments from '@/components/Comments/Comments.vue'
import CommentsList from '@/components/Comments/CommentsList.vue'
import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommunityDetail',
  components: {
    Comments,
    CommentsList,
  },
  // props: {
  //   community_id: {
  //     type: Number,
  //   }
  // },
  data () {
    return {
     community_id: this.$route.params.community_id,
     community: [],
     username: '',
     comment: '',
     comments: [],
     commnet_id: '',
    }
  },
  methods: {
    setToken: function () {
      const config = {
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }
      return config
    },
    deleteCommunity: function() {
      const config = this.setToken();
  
      axios.delete(`${SERVER_URL}/communities/${this.community_id}/delete_update/`, config)
      .then(()=>{
        this.$router.push({ name: 'Community' })
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    moveToUpdateCommunity: function() {
      this.$router.push({name:'UpdateCommunity', params: {community_id: this.community_id}})
    },
    createComment: function (comment) {

      const config = this.setToken();
      const content = {
        content: comment,
      };

      axios.post(`${SERVER_URL}/communities/${this.community_id}/comments/`, content, config)
      .then((res) => {
        comment = ""
        this.comments.push(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getComments: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/communities/${this.community_id}/comments/get/`, config)
      .then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })

    },
    deleteComment: function (comment_id) {
      const config = this.setToken()
      this.comment_id = comment_id
      axios.delete(`http://127.0.0.1:8000/communities/comments/${this.comment_id}/delete`, config)
      .then((res) => {
        this.comments.pop(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    
    const config = this.setToken()

    axios.get(`${SERVER_URL}/communities/${this.community_id}/`, config)
    .then((res)=>{
      this.community = res.data;
      const hash = localStorage.getItem('jwt');
      const info = VueJwtDecode.decode(hash);
      const usernameFromJWT = info.username;
      localStorage.setItem('username', usernameFromJWT);
      this.username = usernameFromJWT;
    })
    .catch((err) => {
      console.log(err)
    })

  

    this.getComments()
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Single+Day&display=swap');
.detailMargin {
  margin-left: 400px;
  margin-top: 150px;
  font-family: 'Single Day', cursive;
}

</style>

