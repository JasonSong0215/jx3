<template>
  <div class="home">
    <div>
      <el-table
        :data="tableData"
        stripe
        style="width: 100%">
        <el-table-column
          prop="acc"
          label="加速数值"
          width="180">
        </el-table-column>
        <el-table-column
          prop="GCD"
          label="1.5GCD(单位：秒)"
          width="180">
        </el-table-column>
        <el-table-column
          prop="po"
          label="破招(单位：秒)"
          width="180">
        </el-table-column>
        <el-table-column
          prop="bing"
          label="兵主逆(单位：秒)"
          width="180"
        >
        </el-table-column>
      </el-table>
    </div>





  </div>
</template>
<style>
  .log {
    padding: 8px 16px;
    background-color: #fff6f7;
    border-radius: 4px;
    border-left: 5px solid #1482f0;
    margin: 20px 0;
  }
  .warning {
    padding: 8px 16px;
    background-color: #fff6f7;
    border-radius: 4px;
    border-left: 5px solid #fe6c6f;
    margin: 20px 0;
  }
</style>
<script>
  // import { mapGetters } from 'vuex'
  import { cal } from '@/api/cal'

  export default {
    name: 'acc',
    data() {
      return {
        tableData: [
          {
          acc:'0',
          GCD: '1.5',
          po: '10',
          bing: '3'
          },
          {
            acc:'43',
            GCD: '1.4375',
            po: '9.6875',
            bing: '2.8125'
          },
          {
            acc:'1457',
            GCD: '',
            po: '9.375',
            bing: ''
          },
          {
            acc:'1928',
            GCD: '1.375',
            po: '',
            bing: ''
          },
          {
            acc:'2956',
            GCD: '',
            po: '9.0625',
            bing: '2.625'
          },
          {
            acc:'4027',
            GCD: '1.3125',
            po: '',
            bing: ''
          },
          {
            acc:'4541',
            GCD: '',
            po: '8.75',
            bing: ''
          },
          {
            acc:'6298',
            GCD: '1.25',
            po: '8.4375',
            bing: '2.4375'
          },
          {
            acc:'8140',
            GCD: '',
            po: '8.125',
            bing: ''
          },
          {
            acc:'8782',
            GCD: '1.1875',
            po: '',
            bing: ''
          },
          {
            acc:'10153',
            GCD: '',
            po: '7.8125',
            bing: '2.25'
          },
        ]
      }
    }
  }
</script>
