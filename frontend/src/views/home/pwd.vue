<template>
  <div class="home">
    <div>
        <el-dialog
          title="登陆"
          :visible.sync="user"
          width="30%">
<!--          :before-close="handleClose"-->

          <el-form>
            <el-input v-model="form.user_name" style="width: 60%" placeholder="登录名"></el-input>
            <el-input v-model="form.password" style="width: 60%" type="password" placeholder="密码"></el-input>
          </el-form>

          <span slot="footer" class="dialog-footer">
            <el-button @click="user = false">取 消</el-button>
            <el-button type="primary" @click="onsubmit">确 定</el-button>
          </span>
        </el-dialog>
    </div>
    <div>
      <el-table
        :data="list"
        style="width: 100%"
      >
        <el-table-column
          prop="id"
          label="id"
          width="180"
          v-if="show"
        >
        </el-table-column>
        <el-table-column
          prop="user_name"
          label="用户名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="pwd"
          label="pwd"
          width="180"
          v-if="show"
        >
        </el-table-column>
        <el-table-column
          prop="owner"
          label="所有者"
          width="180">
        </el-table-column>
        <el-table-column
          prop="ex"
          label="备注"
          width="180">
        </el-table-column>
        <el-table-column
          label="操作">
          <template slot-scope="scope">
            <el-button
              @click.native.prevent="handleCopy(scope.$index, scope.row.user_name)"
              type="text"
              size="small">
              复制账号
            </el-button>
            <el-button
              @click.native.prevent="handleCopy(scope.$index, scope.row.pwd)"
              type="text"
              size="small">
              复制密码
            </el-button>
          </template>
        </el-table-column>



      </el-table>
    </div>
  </div>


</template>

<script>
  import { pwd } from '../../api/cal'
  export default {
    name: 'pwd',
    data(){
      return{
        copyData:null,
        user:true,
        list:[],
        form:{
          user_name:'',
          password:'',

        }
      }
    },
    methods:{
      handleCopy(index,row){
        console.log(index)
        console.log(row)
        this.copyData = row
        this.copy(this.copyData)
      },
      copy(data){
        let url = data;
        let oInput = document.createElement('input');
        oInput.value = url;
        document.body.appendChild(oInput);
        oInput.select(); // 选择对象;
        console.log(oInput.value)
        document.execCommand("Copy"); // 执行浏览器复制命令
        this.$message({
          message: '复制成功',
          type: 'success'
        });
        oInput.remove()
      },
      onsubmit(){
        pwd(this.form).then(response => {
          this.list = []
          this.list = response.data
          this.user = false
        })
      }
    }

  }
</script>

<style scoped>

</style>
