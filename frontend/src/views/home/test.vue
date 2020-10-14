<template>
  <div class="home">
    <div class="log">
      <p>tips:</p>
      <p>某些加成不会加成一些技能，请谨慎选择加成buff</p>
      <p>兵、杀星、火离默认都为1跳伤害，如需模拟完整技能请手动录入所有跳数</p>
      <p>默认114级木桩不可选择其他目标</p>
    </div>
    <el-form :rules="rules" ref="skills" label-width="100px" class="demo-dynamic">
      <el-form-item label="角色属性">
        <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
          点击输入
        </el-button>
      </el-form-item>
      <el-form-item label="秘籍">
        <el-button @click="miji = true" type="primary" style="margin-left: 16px;">
          点击选择
        </el-button>
      </el-form-item>
      <el-drawer
        title="人物属性"
        :visible.sync="drawer"
        :with-header="false">
        <br>
        <table cellpadding="17">
          <!--          <table>-->
          <tr>
            <td><el-tag >基础攻击</el-tag></td>
            <td><el-input v-model="form.jichugongji" style="width: 80px;left: 30%"></el-input></td>
          </tr>
          <tr>
            <td><el-tag >元气</el-tag></td>
            <td><el-input v-model="form.yuanqi" style="width: 80px;left: 30%"></el-input></td>
          </tr>
          <tr>
            <td><el-tag >加速</el-tag></td>
            <td><el-input v-model="form.jiasu" style="width: 80px;left: 30%"></el-input></td>
          </tr>
          <tr>
            <td><el-tag >会心</el-tag></td>
            <td><el-input v-model="form.huixin" style="width: 80px;left: 30%"></el-input></td>
            <td><span>%</span></td>
          </tr>
          <tr>
            <td><el-tag >会效</el-tag></td>
            <td><el-input v-model="form.huixiao" style="width: 80px;left: 30%"></el-input></td>
            <td><span>%</span></td>
          </tr>
          <tr>
            <td><el-tag >破防</el-tag></td>
            <td><el-input v-model="form.pofang" style="width: 80px;left: 30%"></el-input></td>
            <td><span>%</span></td>
          </tr>
          <tr>
            <td><el-tag >无双</el-tag></td>
            <td><el-input v-model="form.wushuang" style="width: 80px;left: 30%"></el-input></td>
            <td><span>%</span></td>
          </tr>
          <tr>
            <td><el-tag >破招</el-tag></td>
            <td><el-input v-model="form.pozhao" style="width: 80px;left: 30%"></el-input></td>
          </tr>
        </table>
        <el-switch
          style="display: block"
          v-model="form.shenyuan_isinclude"
          active-color="#13ce66"
          inactive-color="#ff4949"
          inactive-text="未包含"
          active-text="已包含神元加成的属性"
        >
        </el-switch>
      </el-drawer>
      <el-drawer
        title="秘籍"
        :visible.sync="miji"
        :with-header="false">
        <br>
        <table>
          <tr>
            <div>
              <el-tag>三星临</el-tag><br>
              <el-checkbox-group v-model="form.miji_lin"  :max="4">
                <el-checkbox-button v-for="item in miji_lin" :label="item" :key="item">{{item}}</el-checkbox-button>
              </el-checkbox-group>
            </div>
          </tr>
          <tr>
            <div>
              <el-tag>兵主逆</el-tag><br>
              <el-checkbox-group v-model="form.miji_bing"  :max="4">
                <el-checkbox-button v-for="item in miji_bing" :label="item" :key="item">{{item}}</el-checkbox-button>
              </el-checkbox-group>
            </div>
          </tr>
          <tr>
            <div>
              <el-tag>天斗旋(必须点减调息时间秘籍)</el-tag><br>
              <el-checkbox-group v-model="form.miji_dou"  :max="3">
                <el-checkbox-button v-for="item in miji_dou" :label="item" :key="item">{{item}}</el-checkbox-button>
              </el-checkbox-group>
            </div>
          </tr>
          <tr>
            <div>
              <el-tag>起卦</el-tag><br>
              <el-checkbox-group v-model="form.miji_qi"  :max="4">
                <el-checkbox-button v-for="item in miji_qi" :label="item" :key="item">{{item}}</el-checkbox-button>
              </el-checkbox-group>
            </div>
          </tr>
          <tr>
            <div>
              <el-tag>变卦</el-tag><br>
              <el-checkbox-group v-model="form.miji_bian"  :max="4">
                <el-checkbox-button v-for="item in miji_bian" :label="item" :key="item">{{item}}</el-checkbox-button>
              </el-checkbox-group>
            </div>
          </tr>
          <tr>
            <div>
              <el-tag>鬼星开穴</el-tag><br>
              <el-checkbox-group v-model="form.miji_kai"  :max="4">
                <el-checkbox-button v-for="item in miji_kai" :label="item" :key="item">{{item}}</el-checkbox-button>
              </el-checkbox-group>
            </div>
          </tr>

        </table>
      </el-drawer>

      <el-form-item label="用时（秒）" >
        <el-input type='number' style="width: 100px" v-model="form.totaltime"></el-input>
      </el-form-item>
      <el-form-item
        v-for="(skills, index) in form.skills"
        :label="'技能' + index"
        :key="skills.key"
        :prop="'skills.' + index + '.value'"
      >

        <el-select v-model="skills.value" placeholder="请选择技能">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
        <el-select v-model="skills.buff" multiple placeholder="请选择buff">
          <el-option
            v-for="item in buff_list"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
        <el-button @click.prevent="removeskills(skills)">删除</el-button>
      </el-form-item>
      <el-form-item>

        <el-button @click="addskills">新增技能</el-button>
      </el-form-item>

    </el-form>
    <el-button type="success"  round @click="onSubmit()" style="margin-left: 16px;" :disabled="isDisabled" :loading="isDisabled">计算</el-button>
    <el-button @click="skill_logs = true" round type="primary" style="margin-left: 16px;">
      技能日志
    </el-button>DPS:{{dps}}
    <el-drawer
      title="技能日志"
      :visible.sync="skill_logs"
      :with-header="false">
      <div>
        <el-table
          :data="skill_log"
          style="width: 100%"
          height="700">
          <el-table-column
            fixed
            prop="name"
            label="技能名称"
            width="150">
          </el-table-column>
          <el-table-column
            fixed
            prop="damage"
            label="伤害预期"
            width="150">
          </el-table-column>
        </el-table>
      </div>
    </el-drawer>


  </div>
</template>
<style>
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
  font-size: 10px;
}
.demo-table-expand .el-form-item{
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
  font-size: 10px;
}
.log {
  padding: 8px 16px;
  background-color: #fff6f7;
  border-radius: 4px;
  border-left: 5px solid #1482f0;
  margin: 20px 0;
}
</style>
<script>
// import { mapGetters } from 'vuex'
import { cal } from '@/api/cal'
import { authdps } from '../../api/cal'
import { test_dps } from '../../api/cal'


export default {
  name: 'test',
  data() {
    return {
      rules:{
        totaltime: { type: 'number', required: true, message: '请输入总用时长', trigger: 'blur' }
      },
      options: [{
        value: 'bing',
        label: '兵主逆',
        buff:[],
      }, {
        value: 'dou',
        label: '天斗旋',
        buff:[],
      }, {
        value: 'lin',
        label: '三星临',
        buff:[],
      }, {
        value: 'kai',
        label: '鬼星开穴',
        buff:[],
      }, {
        value: 'ding',
        label: '往者定',
        buff:[],
      },
      {
        value: 'sha',
        label: '杀星在尾',
        buff:[],
      },
      {
        value: 'huo',
        label: '火离',
        buff:[],
      },
      {
        value: 'ling',
        label: '灵器',
        buff:[],
      },
      ],
      buff_list: [
        {
          value: '鬼遁',
          label: '鬼遁（攻击+15%）',
        },
        {
          value: '祝祷',
          label: '祝祷（伤害+10%）',
        },
        {
          value: '荧入白',
          label: '荧入白（无视50%防御）',
        },
        {
          value: '重山',
          label: '重山 (九字诀*1.15)',
        },
        {
          value: '望旗',
          label: '望旗（兵+10%）',
        },
        {
          value: '相蚀',
          label: '相蚀（临+30%）',
        },
        {
          value: '明心',
          label: '明心（临双会）',
        },
        {
          value: '正夏',
          label: '正夏（临+10%）',
        },
      ],

        value: '',
      isDisabled:false,
      dpsData: [],
      itemkey: '',
      dps:0,
      colors: [
        {color: '#f56c6c', percentage: 20},
        {color: '#e6a23c', percentage: 40},
        {color: '#5cb87a', percentage: 60},
        {color: '#1989fa', percentage: 80},
        {color: '#6f7ad3', percentage: 100}
      ],
      miji_lin:["伤害+5%","伤害+4%","伤害+3%","会心+4%","会心+3%","会心+2%","效果：瞬发斗"],
      miji_bing:["伤害+5%","伤害+4%","伤害+3%","会心+4%","会心+3%",],
      miji_dou:["伤害+5%","伤害+4%","伤害+3%","会心+4%","会心+3%","会心+2%"],
      miji_qi:["调息时间-3s","调息时间-2s"],
      miji_bian:["调息时间-2s","调息时间-2s","调息时间-1s","星运消耗-5"],
      miji_kai:["伤害+5%","伤害+4%","会心+4%","会心+3%",],
      drawer: false,
      miji:false,
      guaxiang:false,
      res:false,
      auth:false,
      skill_logs:false,
      form: {
        totaltime:'',
        skills:[{
          value:'',
          buff:[],
        }],
        shenyuan_isinclude:true,
        miji_lin:["伤害+5%","伤害+4%","伤害+3%","会心+4%"],
        miji_bing:["伤害+5%","伤害+4%","伤害+3%","会心+4%"],
        miji_dou:["伤害+5%","伤害+4%","会心+4%"],
        miji_qi:["调息时间-3s","调息时间-2s"],
        miji_bian:["调息时间-2s","调息时间-2s","调息时间-1s","星运消耗-5"],
        miji_kai:["伤害+5%","伤害+4%","会心+4%","会心+3%",],
        jichugongji: '10166',
        yuanqi: '3301',
        jiasu:'325',
        huixin: '16.62',
        huixiao: '175.99',
        pofang: '24.78',
        wushuang: '14.35',
        pozhao: '10184',
        zhenyan:'1',
        buff: [],
        med: [],
        target:'4',
      }
    }
  },
  methods: {
    onSubmit() {
      this.isDisabled = true
      setTimeout(() => {
        this.isDisabled = false

      },3000)
      test_dps(this.form).then(response => {
        this.skill_log = []
        this.skill_log = response.data.skill_log
        this.dps = response.data.dps
        this.itemkey = Math.random()
        ;
      })
    },
    auth_dps() {
      authdps(this.form).then(response => {
        this.authData = []
        this.authData = response.data
        console.log(response.data)
      })
    },



    addskills() {
      this.form.skills.push({
        value: '',
        key: Date.now(),
        buff:[],
      });
      console.log(this.form.skills)
    },
    removeskills(item) {
      var index = this.form.skills.indexOf(item)
      if (index !== -1) {
        this.form.skills.splice(index, 1)
      }
    },
  }
}
</script>
