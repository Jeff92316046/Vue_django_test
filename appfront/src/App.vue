<!-- <template>
  <div class="container">
    <line-chart
      v-if="loaded"
      :chartdata="chartdata"
      />
  </div>
</template> -->
<template>
  <div class="container">
    <Line
    id="chart"
    v-if="loaded"
    :options="chartOptions"
    :data="chartData"
    />
  </div>
  
  <div>
    <input class="input" v-model="stock" placeholder="0050">
  </div>
  <div>
    <!--<a>大股東上下限</a>-->
    <input class="input" v-model="number_min" placeholder="小">
    <input class="input" v-model="number_max" placeholder="大">
  </div>
  <div>
    <button @click="getData()">aaaa</button>
  </div>
  <table >
    <thead>
      <tr>
        <th>日期</th>
        <th>人數</th>
        <th>張數</th>
      </tr>
    </thead>
    <tbody>
      
      <td >
        <tr v-for="i in chartData.labels">{{ i }} </tr>
      </td>
      <td >
        <tr v-for="i in chartData.datasets[0].data">{{ i }}</tr>
      </td>
      <td>
        <tr v-for="i in chartData.datasets[1].data">{{ i }}</tr>
      </td>
    </tbody>
  </table>

  
  
  
  <!--<div>{{ chartData}}</div>
   <div>{{ chartData.datasets[0].data.length }}</div>
  <div>{{ chartData.labels.length }}</div> -->
</template>
<script>
import axios from 'axios'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
BarElement
} from 'chart.js'
import { Line } from 'vue-chartjs'


ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend
)
export default{
  name: 'LineChart',
  components: { Line },

  data:()=> ({
      loaded : false,
      stock : '0050',
      number_min : '15',
      number_max : '15',
      average : 0,
      chartData: {
        labels: [],
        datasets: [
          {
            type :'bar',
            label: 'people',
            yAxisID: 'A',
            backgroundColor: 'rgb(240 ,50, 50)',
            
            data: [],
            fill: true,
            tension: 0.4,
            order : 2
          },
          {
            type :'line',
            label: 'share',
            yAxisID: 'B',
            
            backgroundColor: 'rgb(255, 255, 255)',
            borderColor : 'rgb(50, 200, 255)',
            data: [],
            fill: true,
            order : 1
          }
        ]
      },
      chartOptions: {
        responsive: true,
        scales: {
            A: {
                type: 'linear',
                position: 'left',
                
            },
            B: {
                type: 'linear',
                position: 'right',
                

            }
        }
      }
  }),
  methods:{
    async getData(){
      this.loaded = false
      try {
        await axios
          .get('http://127.0.0.1:8000/api/stockdata/sql_cursor/',
              { params : 
                { stock : this.stock, 
                  number_min : this.number_min,
                  number_max : this.number_max } })
          .then((response) => {
            this.chartData.datasets[0].data = response.data[1]
            this.chartData.labels = response.data[0]
            this.chartData.datasets[1].data = response.data[2]
        })
        this.loaded =true
      } catch (e) {
        console.error(e)
      }
    }
  }
}
/* export default {
  name: 'LineChartContainer',
  components: { LineChart  },
  data: () => ({
    loaded: true,
    chartdata: null
  }),
  async mounted () {
    this.loaded = true

    try {
      axios
        .get('http://127.0.0.1:8000/api/stockdata/sql_cursor/',
            { params : {stock : '0050',number:'1' } })
        .then((response) => {
          this.chartdata = response.data
      })

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
*/
</script> 
<style>
  .container{
    margin: 5%;
  }
</style>