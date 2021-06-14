<template>
  <body class="local-nav-sticky">
    <div class="box">
      <div class="container">
        <nav class="local-nav">
          <div class="local-nav-links">
            <router-link style="font-family: 'Gugi', cursive;" class="router-link product-name" to="/">MOMOGO</router-link>
            <router-link v-if="Login" class="router-link" @click.native="logout" to="#" >Logout</router-link>
            <router-link v-else class="router-link" to="/user/login" >Login</router-link>
          </div>
        </nav>
        <section class="scroll-section" id="scroll-section-0" style="">
          <div class="sticky-elem-img">
            <img id="img-0" width="1920" height="1080" :src="require('@/assets/img/home/food1.jpg')" alt="">
          </div>
          <div id="message-0" class="mid">
            <p>행복한 고민의 시작</p>
            <h1 style="font-family: 'Gugi', cursive;">MOMOGO!</h1> 
          </div>
        </section>
        <section class="scroll-section" id="scroll-section-1" style="">
          <div class="sticky-elem sticky-elem-canvas">
            <!-- <canvas id="video-canvas-0" width="1920" height="1080"></canvas> -->
            <img width="1920" height="1080" id="video-canvas-0" :src="require(`@/assets/img/home/youtube/${img_src}.jpg`)" alt="">
          </div>
          <div class="sticky-elem main-message a">
            <p>수만가지의<br> 음식정보를<br>한번에!</p>
          </div>
          <div class="sticky-elem main-message b">
            <p>싫어하는 음식을 제외하고 <br> 음식을 추천!</p>
          </div>
          <div class="sticky-elem main-message c">
            <p>캘린더를 통해 <br>먹은 음식을 <br> 한 눈에 파악! </p>
          </div>
          <div class="sticky-elem main-message d">
            <p>영양소 비교를 통한<br>식단 관리를 <br>지금 시작하세요!</p>
          </div>
        </section>
        <section class="scroll-section" id="scroll-section-2" style="">
          <p class="description">
            <strong style="font-family: 'Gugi', cursive;">MOMOGO</strong>
            모모고는 무엇을 먹을지 고민하는 여러분들을 위해 고안되었습니다. 여러분들의 신체정보를 통해 필요한 영양소, 칼로리를 계산하고 오늘 부족한 영양분은 어떤 것인지 파악하여 그에 따른 음식을 추천해 드리고 있습니다. <br>
          </p>
        </section>
        <section class="scroll-section" id="scroll-section-3" style="">
          <div class="sticky-elem main-message a">
            <p style="font-family: 'Gugi', cursive;">
              <small>뭐먹을지 고민될땐?</small>
              MOMOGO!
            </p>
          </div>
        </section>
      </div>
      <footer class="footer">
        제작자: 최주아, 이현우, 이호석, 박성준, 김병수
      </footer>
    </div>
  </body>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      Login: false,
      sceneInfo : [],
      yOffset: 0, //window.pageYOffset 대신 쓸 변수
      prevScrollHeight : 0, // 현재 스크롤 위치(yOffset)보다 이전에 위치한 스크롤 섹션들의 높이값의 합
      currentScene : 0, // 현재 활성화된(눈 앞에 보고있는) 씬(scroll-section)
      enterNewScene : false, //새로운 scene이 시작된 순간 true
      img : [],
      img_src:"0",
      acc:0.02,
      delayedYOffset:0,
      rafState: false,
      rafId: 0,
    }
  },
  watch: {
    },
  computed: {
    },
  created() {
    // window.addEventListener('re')
    window.addEventListener("scroll", ()=> {
    this.yOffset = window.pageYOffset
    this.scrollLoop()
    if (!this.rafState) {
      this.rafId = requestAnimationFrame(this.loop);
      this.rafState = true;
      } 
    });
    window.addEventListener("resize", () =>{
    if (window.innerWidth > 600) {
      this.setLayout();
      }
    })
    // 핸드폰 뒤집을 때
    window.addEventListener('orientationchange', this.setLayout)
    // window.addEventListener("load", this.setData);
    // window.addEventListener('load',this.setLayout);
    // window.addEventListener('load', this.scrollLoop);
    

    

    
  },
  mounted() {
    this.setData()
    this.setLayout()
    this.scrollLoop()
    const token = localStorage.getItem('jwt')
    if (token) {
      this.Login = true
      this.$router.push({path:'/main'})
      }
    for (let i = 1; i < 271; i++) {
      this.img.push({src:i});
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('jwt')
      this.Login = false
      alert('로그아웃되었습니다.')
      this.$router.push({name:'login'})
      },
    setData(){
      this.sceneInfo = [
      //각 구간(4개)에대한 객체 정보 입력
        {
          //0
          type: 'sticky',
          heightNum:0.5,
          scrollHeight: 0,
          objs: {
            container: document.querySelector('#scroll-section-0'),
          },
          values: {
            message_opacity_out :[1,0,{start:0,end:0.8}],
            img_opacity_out:[1,0,{start:0,end:0.8}],
            message_translateY_out:[0, -25,{start:0,end:0.8}],
          }
        },
        {
          //1
          type: 'sticky',
          heightNum:5, //브라우저 높이의 5배로 scrollHeight 세팅
          scrollHeight: 0, //여러화면에서 볼 수 있도록 높이를 스크린의 높이의 배수, 유동적으로 할 수 있게 0으로 시작
          //html객체를 만들어놓기
          objs: {
            container: document.querySelector('#scroll-section-1'),
            messageA: document.querySelector('#scroll-section-1 .main-message.a'),
            messageB: document.querySelector('#scroll-section-1 .main-message.b'),
            messageC: document.querySelector('#scroll-section-1 .main-message.c'),
            messageD: document.querySelector('#scroll-section-1 .main-message.d'),
            canvas: document.querySelector('#video-canvas-0'),
            // context: document.querySelector('#video-canvas-0').getContext('2d'),
            videoImages: []
          },
          values: {
            imageSequence: [0, 270],
            canvas_opacity_in:[0, 1, {start:0, end: 0.1}],
            canvas_opacity_out:[1, 0, {start:0.9, end: 1}],
            messageA_opacity_in: [0, 1, { start: 0.1, end: 0.2 }],
            messageB_opacity_in: [0, 1, { start: 0.3, end: 0.4 }],
            messageC_opacity_in: [0, 1, { start: 0.5, end: 0.6 }],
            messageD_opacity_in: [0, 1, { start: 0.7, end: 0.8 }],
            messageA_translateY_in: [30, 0, { start: 0.1, end: 0.2 }],
            messageB_translateY_in: [30, 0, { start: 0.3, end: 0.4 }],
            messageC_translateY_in: [30, 0, { start: 0.5, end: 0.6 }],
            messageD_translateY_in: [30, 0, { start: 0.7, end: 0.8 }],
            messageA_opacity_out: [1, 0, { start: 0.25, end: 0.3 }],
            messageB_opacity_out: [1, 0, { start: 0.45, end: 0.5 }],
            messageC_opacity_out: [1, 0, { start: 0.65, end: 0.7 }],
            messageD_opacity_out: [1, 0, { start: 0.85, end: 0.9 }],
            messageA_translateY_out: [0, -30, { start: 0.25, end: 0.3 }],
            messageB_translateY_out: [0, -30, { start: 0.45, end: 0.5 }],
            messageC_translateY_out: [0, -30, { start: 0.65, end: 0.7 }],
            messageD_translateY_out: [0, -30, { start: 0.85, end: 0.9 }]
          }
        },
        {
          //2
          type: 'normal',
          // heightNum:5,
          scrollHeight: 0,
          objs: {
            container: document.querySelector('#scroll-section-2'),
            content: document.querySelector('#scroll-section-2 .description')
          }
        },
        {
          //3
          type: 'sticky',
          heightNum: 1,
          scrollHeight: 0,
          objs: {
            container: document.querySelector('#scroll-section-3'),
            messageA: document.querySelector('#scroll-section-3 .a'),
          },
          values: {
            messageA_translateY_in: [40, 0, { start: 0.05, end: 0.15 }],
            messageA_opacity_in: [0, 1, { start: 0.05, end: 0.15 }],
          }
        },
      ]
    },
    setLayout() {
    // 각 스크롤 섹션의 높이 세팅
    for (let i = 0; i < this.sceneInfo.length; i++){
      if (this.sceneInfo[i].type === 'sticky') {
        this.sceneInfo[i].scrollHeight = this.sceneInfo[i].heightNum * window.innerHeight;
        // 일반적으로 문자열을 쓰니, 빽틱 달러의 중괄호 내부에는 변수를 넣을수 있음
      } else  if (this.sceneInfo[i].type === 'normal') {
        this.sceneInfo[i].scrollHeight = this.sceneInfo[i].objs.container.offsetHeight
      }
      this.sceneInfo[i].objs.container.style.height = `${this.sceneInfo[i].scrollHeight}px`
    }
      let totalScrollHeight = 0;
      for (let i = 0; i < this.sceneInfo.length; i++) {
        totalScrollHeight += this.sceneInfo[i].scrollHeight;
        if (totalScrollHeight >= this.yOffset) {
          this.currentScene = i
          break;
        }
      }
      document.body.setAttribute('id',`show-scene-${this.currentScene}`);

      const heightRatio = (window.innerHeight / 1080);
      const widthRatio = (window.innerWidth/1920);
      const canvas = document.querySelector('#video-canvas-0')
      canvas.style.transform = `translate3d(-50%, -50%, 0) scale(${heightRatio})`
      const img = document.querySelector('#img-0')
      if (widthRatio< 0.5) {
        img.style.transform = `translate3d(-50%, -50%, 0) scale(${heightRatio})`
      }else{
        img.style.transform = `translate3d(-50%, -50%, 0) scale(${widthRatio}, ${heightRatio})`
      }
      // this.sceneInfo.objs.canvas.style.transform = `scale(${heightRatio})`
    },
    scrollLoop () {
      this.enterNewScene = false;
      this.prevScrollHeight = 0
      for (let i = 0; i<this.currentScene; i++) {
        this.prevScrollHeight += this.sceneInfo[i].scrollHeight;
      }
      if (this.yOffset > this.prevScrollHeight + this.sceneInfo[this.currentScene].scrollHeight) {
        this.enterNewScene = true;
        this.currentScene++;
        document.body.setAttribute('id',`show-scene-${this.currentScene}`); 
      }
      if(this.yOffset < this.prevScrollHeight) {
        this.enterNewScene = true;
        if(this.currentScene===0) return;
        this.currentScene--;
        document.body.setAttribute('id',`show-scene-${this.currentScene}`); 
      }
      if(this.enterNewScene) return;
      this.playAnimation();
    },
    loop() {
			this.delayedYOffset = this.delayedYOffset + (this.yOffset - this.delayedYOffset) * this.acc;
      const currentYOffset = this.delayedYOffset - this.prevScrollHeight;
      const values = this.sceneInfo[this.currentScene].values;

      if (this.currentScene === 1){
        let sequence = Math.round(this.calcValues(values.imageSequence, currentYOffset));
        if (this.img[sequence]) {
          this.img_src = this.img[sequence].src
        }
      }

			this.rafId = requestAnimationFrame(this.loop);

			if (Math.abs(this.yOffset - this.delayedYOffset) < 1) {
				cancelAnimationFrame(this.rafId);
				this.rafState = false;
			}
		},
    calcValues(values, currentYOffset) {
      let rv;
      // 현재씬(스크롤섹션)에서 스크롤된 범위를 비율로 구하기
      const scrollHeight = this.sceneInfo[this.currentScene].scrollHeight;
      const scrollRatio = currentYOffset / scrollHeight;

      if (values.length === 3) {
        //start ~ end 사이에 애니매이션 실행
        const partScrollStart = values[2].start * scrollHeight
        const partScrollEnd = values[2].end * scrollHeight
        const partScrollHeight = partScrollEnd - partScrollStart
        
        if (currentYOffset >= partScrollStart && currentYOffset <= partScrollEnd) {
          rv = (currentYOffset - partScrollStart)/partScrollHeight * (values[1] - values[0]) + values[0];
        } else if (currentYOffset < partScrollStart) {
          rv = values[0];
        } else if (currentYOffset > partScrollEnd) {
          rv = values[1];
        }
      } else {
        rv = scrollRatio * (values[1] - values[0]) + values[0];
      }
      return rv;
      },
    
    playAnimation () {
      const objs = this.sceneInfo[this.currentScene].objs;
      const values = this.sceneInfo[this.currentScene].values;
      const currentYOffset = this.yOffset - this.prevScrollHeight;
      const scrollHeight = this.sceneInfo[this.currentScene].scrollHeight;
      const scrollRatio = currentYOffset / scrollHeight // yOffset/현재 씬의 scrollHeight

      switch(this.currentScene) {
        case 0:{
          const img = document.querySelector('#img-0')
          const message0 = document.querySelector('#message-0')
          message0.style.opacity = this.calcValues(values.message_opacity_out, currentYOffset)
          message0.style.transform = `translate3d(0, ${this.calcValues(values.message_translateY_out, currentYOffset)}%, 0)`
          img.style.opacity = this.calcValues(values.img_opacity_out, currentYOffset)
          break;
        }
        case 1:{
          const back = document.querySelector('.sticky-elem-canvas')

          // let sequence = Math.round(this.calcValues(values.imageSequence, currentYOffset));
          // if (scrollRatio < 0.99) {
          //   this.img_src = this.img[sequence].src
          // }
          // const canvas = document.querySelector('#video-canvas-0')
          if (scrollRatio <= 0.3) {
            back.style.opacity = this.calcValues(values.canvas_opacity_in, currentYOffset)
          }
          else {
            back.style.opacity = this.calcValues(values.canvas_opacity_out, currentYOffset)
          }
          // canvas.style.opacity = this.calcValues(values.canvas_opacity_out, currentYOffset)

          if (scrollRatio <= 0.22) {
            objs.messageA.style.opacity = this.calcValues(values.messageA_opacity_in, currentYOffset)
            objs.messageA.style.transform = `translate3d(0, ${this.calcValues(values.messageA_translateY_in, currentYOffset)}%, 0)`
            // objs.messageA.style.transform = `translateY(${this.calcValues(values.messageA_translateY_in, currentYOffset)}%)`
          } else {
            objs.messageA.style.opacity = this.calcValues(values.messageA_opacity_out, currentYOffset)
            objs.messageA.style.transform = `translate3d(0, ${this.calcValues(values.messageA_translateY_out, currentYOffset)}%, 0)`
            // objs.messageA.style.transform = `translateY(${this.calcValues(values.messageA_translateY_out, currentYOffset)}%)`
          }

          if (scrollRatio <= 0.42) {
            // in
            objs.messageB.style.opacity = this.calcValues(values.messageB_opacity_in, currentYOffset);
            objs.messageB.style.transform = `translate3d(0, ${this.calcValues(values.messageB_translateY_in, currentYOffset)}%, 0)`;
          } else {
            // out
            objs.messageB.style.opacity = this.calcValues(values.messageB_opacity_out, currentYOffset);
            objs.messageB.style.transform = `translate3d(0, ${this.calcValues(values.messageB_translateY_out, currentYOffset)}%, 0)`;
          }

          if (scrollRatio <= 0.62) {
            // in
            objs.messageC.style.opacity = this.calcValues(values.messageC_opacity_in, currentYOffset);
            objs.messageC.style.transform = `translate3d(0, ${this.calcValues(values.messageC_translateY_in, currentYOffset)}%, 0)`;
          } else {
            // out
            objs.messageC.style.opacity = this.calcValues(values.messageC_opacity_out, currentYOffset);
            objs.messageC.style.transform = `translate3d(0, ${this.calcValues(values.messageC_translateY_out, currentYOffset)}%, 0)`;
          }

          if (scrollRatio <= 0.82) {
            // in
            objs.messageD.style.opacity = this.calcValues(values.messageD_opacity_in, currentYOffset);
            objs.messageD.style.transform = `translate3d(0, ${this.calcValues(values.messageD_translateY_in, currentYOffset)}%, 0)`;
          } else {
            // out
            objs.messageD.style.opacity = this.calcValues(values.messageD_opacity_out, currentYOffset);
            objs.messageD.style.transform = `translate3d(0, ${this.calcValues(values.messageD_translateY_out, currentYOffset)}%, 0)`;
            }
          break;
        }

        case 3:{
            // in
          objs.messageA.style.opacity = this.calcValues(values.messageA_opacity_in, currentYOffset);
          objs.messageA.style.transform = `translate3d(0, ${this.calcValues(values.messageA_translateY_in, currentYOffset)}%, 0)`;
          break
        }
      }
    }
  },
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Gugi&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;900&display=swap");
.box {
  font-family: 'Noto Sans KR', sans-serif;
  /* 가로스크롤 안생기게 가로 밖으로 나가면 숨김 */
  overflow: hidden;
  /* color: rgb(233, 233, 236); */
  /* 자간 */
  letter-spacing: -0.05em;
  background: white;
}
p {
  /* 문간 */
  margin: 0;
  line-height: 1.6;
}
.router-link{
  color: rgb(3, 3, 3);
  /* 밑줄 없애기 */
  text-decoration: none;
}
.local-nav {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 10;
  width: 100%;
  height: 52px;
  padding: 0 1rem;
  /* border-bottom: 1px solid #ddd; */
}
.local-nav-links {
  display: flex;
  align-items: center;
  max-width: 1000px;
  height: 100%;
  margin: 0 auto;
  font-size: 1.2rem;
  font-weight: bold;
}
.local-nav-sticky .local-nav {
  position: fixed;
  top:0;
  background: rgba(255,255,255,0.1);
  backdrop-filter: saturate(180%) blur(3px);
  /* backdrop-filter: brightness(1); */
  /* backdrop-filter: contrast(.2); */
  /* backdrop-filter: drop-shadow(5px 5px red); */
}
.local-nav-links .product-name {
  margin-right: auto;
  font-size: 1.2rem;
}
.scroll-section {
  padding-top: 50vh;
}
#scroll-section-1 {
  color: rgb(233, 233, 236);
}
/* #scroll-section-1 h1{
  position: relative;
  top: -10vh;
  z-index: 5;
  font-size: 4rem;
  text-align: center;
  margin: 0;
} */
.main-message {
  display: flex;
  align-items: center;
  justify-content: center;
  top: 35vh;
  margin: 5px 0;
  height: 3em;
  font-size:2.5rem;
  opacity: 0;
}
.main-message p {
  font-weight: bold;
  text-align: center;
  line-height: 1.2;
}
.mid h1{
  display: flex;
  position: relative;
  top: -10vh;
  font-size:4.5rem;
  justify-content: center;
}
.mid p {
  display: flex;
  position: relative;
  justify-content: center;
  top: -10vh;
  font-weight: bold;
  text-align: center;
  line-height: 1.2;
  font-size:1.5rem;
  /* backdrop-filter: saturate(180%) blur(0.1px); */
  /* backdrop-filter: brightness(1.05); */
  backdrop-filter: contrast(.8);
  /* backdrop-filter: drop-shadow(5px 5px red); */
}
.main-message small {
  display:block;
  margin-bottom: 0.5em;
  font-size:1.2rem;
}
#scroll-section-3 .main-message{
  font-size:3.5rem;
}
.description {
  max-width: 1000px;
  margin:0 auto;
  padding: 0 1rem;
  font-size:1.2rem;
  color:#888;
}
.description strong {
  float: left;
  margin-right:0.2em;
  font-size: 3rem;
  color: rgb(29,29,31);
}
/* .desc-message {
  width:50%;
  font-weight:bold;
}
.pin {
  width: 100px;
  height: 1px;
  background: rgb(29,29,31);
}

#scroll-section-3 .c {
  top: 15%;
  left: 45%;
} */
.mid-message {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 1rem;
  font-size: 2rem;
  color:#888;
}
.mid-message strong {
  color: rgb(29,29,31);
}
/* .canvas-caption {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 1rem;
  color: #888;
  font-size: 1.2rem;
  text-align: center;
} */
.footer {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: -64;
  left:-64.4px;
  width:100vw;
  height: 7rem;
  color: white;
  background: rgb(176, 193, 166);
}
.sticky-elem {
  display: none;
  position: fixed;
  left: 0;
  width: 100%
}
#scroll-section-0{
  display: flex;
  justify-content: center;
  color: rgb(255, 255, 255);
}

#show-scene-0 #scroll-section-0 .sticky-elem,
#show-scene-1 #scroll-section-1 .sticky-elem,
#show-scene-2 #scroll-section-2 .sticky-elem,
#show-scene-3 #scroll-section-3 .sticky-elem {
  display: block;
}
.sticky-elem-canvas {
	top: 0;
	height: 100%;
  background: rgb(12, 12, 12);
}
.sticky-elem-canvas img {
  position: absolute;
  top: 50%;
  left: 50%;
}
.sticky-elem-img {
  top: 0;
	height: 100%;
}
.sticky-elem-img img{
  position: absolute;
  top: 50%;
  left: 50%;
}
@media(min-width: 1024px) {
  #scroll-section-3 h1 {
    font-size: 9vw;
  }
  .main-message {
    font-size: 4vw;
  }
  .description {
    font-size: 2rem;
  }
  .description strong {
    font-size: 6rem;
  }
  #scroll-section-3 .main-message {
    font-size: 6vw;
  }
  .main-message small {
    font-size: 1.5vw
  }
  .desc-message {
    width: 20%;
  }
  /* #scroll-section-3 .b {
  top: 20%;
  left: 53%;
  }
  #scroll-section-3 .c {
    left: 55%;
  } */
  .mid-message {
    font-size: 4vw;
  }
  /* .canvas-caption {
    font-size: 2rem;
  } */
}
</style>