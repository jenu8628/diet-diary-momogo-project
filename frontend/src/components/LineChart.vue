<script>
//Importing Line class from the vue-chartjs wrapper
import { Line } from "vue-chartjs";
import axios from 'axios';
import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL
//Exporting this so it can be used in other components
export default {
  extends: Line,
  data() {
    return {
      datacollection: {
        //Data to be represented on x-axis
        labels: ["D-6", "D-5", "D-4", "D-3", "D-2", "D-1", "D-day"],
        datasets: [
          {
            label: "칼로리 섭취량",
            backgroundColor: "white",
            pointBackgroundColor: "white",
            borderWidth: 10,
            pointBorderColor: "black",
            //Data to be represented on y-axis
            data: [],
            // padding-left: '20px'
          },
        ],
      },
      //Chart.js options that controls the appearance of the chart
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
                padding: 50,
              },
              gridLines: {
                display: true,
              },
            },
          ],
          xAxes: [
            {
              gridLines: {
                display: false,
              },
            },
          ],
        },
        legend: {
          display: true,
        },
        responsive: true,
        maintainAspectRatio: false,
      },
      seven : [],
      six : [],
      five : [],
      four : [],
      three : [],
      two : [],
      one : [],
    };
  },
  created() {
  },
  mounted() {
    //renderChart function renders the chart with the datacollection and options object.
    this.getToday()
    this.renderChart(this.datacollection, this.options);
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
    getToday () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      const date = this.$moment().format('YYYY-MM-DD')
      axios.get(`${SERVER_URL}/foods/${info.user_id}/get_userFood/`, config)
      .then((res)=>{
        const days = [this.one, this.two,this.three,this.four,this.five,this.six,this.seven]
        for (let i = 0; i < res.data.length; i++){
          for (let j = 0; j < 7; j++) {
            if (
              parseInt(res.data[i].created_at.slice(0,4)) === parseInt(date.slice(0,4)) &&
                parseInt(res.data[i].created_at.slice(5,7)) === parseInt(date.slice(5,7)) &&
                parseInt(res.data[i].created_at.slice(8,10)) === parseInt(date.slice(8,10) - j)
            ){
              days[j].push(res.data[i].kcal)
            }
          }
        }
        const reducer = (accumulator, currentValue) => accumulator + currentValue;
        if (this.seven.length !== 0) {
          this.datacollection.datasets[0].data.push(parseInt(this.seven.reduce(reducer)))
        } else {
          this.datacollection.datasets[0].data.push(0)
        }
        if (this.six.length !== 0) {
          this.datacollection.datasets[0].data.push(parseInt(this.six.reduce(reducer)))
        } else {
          this.datacollection.datasets[0].data.push(0)
        }
        if (this.five.length !== 0) {
          this.datacollection.datasets[0].data.push(parseInt(this.five.reduce(reducer)))
        } else {
          this.datacollection.datasets[0].data.push(0)
        }
        if (this.four.length !== 0) {
          this.datacollection.datasets[0].data.push(parseInt(this.four.reduce(reducer)))
        } else {
          this.datacollection.datasets[0].data.push(0)
        }
        if (this.three.length !== 0) {
          this.datacollection.datasets[0].data.push(parseInt(this.three.reduce(reducer)))
        } else {
          this.datacollection.datasets[0].data.push(0)
        }
        if (this.two.length !== 0) {
          this.datacollection.datasets[0].data.push(parseInt(this.two.reduce(reducer)))
        } else {
          this.datacollection.datasets[0].data.push(0)
        }
        if (this.one.length !== 0) {
          this.datacollection.datasets[0].data.push(parseInt(this.one.reduce(reducer)))
        } else {
          this.datacollection.datasets[0].data.push(0)
        }
        
      }).catch((err)=>{
        console.log(err)
      })
    }
  },
  
};
</script>
