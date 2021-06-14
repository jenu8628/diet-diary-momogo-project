<template>
  <div class="confirm">
		<div>
			<h1 style="font-family: 'Jua', sans-serif;">
				비밀번호 확인
			</h1>
			<hr style="width:70vw; background-color:gainsboro; height:0.2vh;">
			<div class="comment">
				<p style="font-family: 'Noto Serif KR', serif; font-size:1.6em;">
					개인 정보 조회를 위해서는 인증이 필요합니다.
				</p>
				<p style="font-family: 'Noto Serif KR', serif; font-size:1.6em;">
					비밀번호 입력 후 확인 버튼을 클릭해 주세요.
				</p>

				<!-- 비밀번호 확인 입력받는 곳 -->
				<v-app id="inspire">
					<div>
						<v-text-field
							label="비밀번호 확인"
							style="margin-top:3vh;"
              v-model="password"
              @keyup.enter="passwordconfirm"
              type="password"
						>
						</v-text-field>
					</div>
				</v-app>

				<!-- 확인버튼 -->
				<v-app id="">
					<v-btn @click="passwordconfirm" class="confirmButton">
						확인
					</v-btn>
				</v-app>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
// import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
	data() {
    return {
      password : ""
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization : `JWT ${token}`,
        }
      }
      return config
    },
    passwordconfirm () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/accounts/password/`, config)
      .then((res)=>{
        if (this.password === res.data.password) {
          this.$router.push('/myinfo')
        }
      }).catch((err)=> {
        console.log(err)
      })
    }
  },
}
</script>

<style scoped>
	@import url('https://fonts.googleapis.com/css2?family=Gugi&family=Noto+Serif+KR&display=swap');
	.confirm {
		margin-left: 20vw;
		margin-top: 15vh;
	}
	.comment {
		width:40vw;
		position:relative;
		top: 12vh;
		left: 13vw;
		text-align: center;
	}
	.confirmButton{
		position:relative;
		left:15vw;
		top:1vh;
		width: 10vw !important;
		background-color: rgb(13, 62, 119) !important;
		color: white;
	}
</style>