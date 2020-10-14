<template>
  <div class="home">
    <div>
      <el-form ref="form" :model="form" label-width="80px">
        <br>
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
        <el-form-item label="奇穴" >
          <el-select v-model="form.qixue_1" style="width: 80px">
            <el-option label="正夏" value="1" onselect="qixue_1" style="color: indigo"></el-option>
            <el-option label="明心" value="2" onselect="qixue_1" style="color: indigo"></el-option>
            <el-option label="天网" value="3" onselect="qixue_1" disabled></el-option>
          </el-select>
          <el-select v-model="form.qixue_2" style="width: 80px">
            <el-option label="望旗" value="1" onselect="qixue_2" style="color: indigo"></el-option>
            <el-option label="关锁" value="2" onselect="qixue_2"></el-option>
            <el-option label="水盈" value="3" onselect="qixue_2"></el-option>
          </el-select>
          <el-select v-model="form.qixue_3" style="width: 80px">
            <el-option label="相蚀" value="1" onselect="qixue_3" style="color: indigo"></el-option>
            <el-option label="山瘴" value="2" onselect="qixue_3" ></el-option>
            <el-option label="连蜷" value="3" onselect="qixue_3" disabled></el-option>
            <el-option label="司命" value="4" onselect="qixue_3" disabled></el-option>
          </el-select>
          <el-select v-model="form.qixue_4" style="width: 80px">
            <el-option label="重山" value="1" onselect="qixue_4" style="color: indigo"></el-option>
            <el-option label="水洊" value="2" onselect="qixue_4" ></el-option>
            <el-option label="龙回首" value="3" onselect="qixue_4"></el-option>
            <el-option label="神皆寂" value="4" onselect="qixue_4"></el-option>
          </el-select>
          <el-select v-model="form.qixue_5" style="width: 80px">
          <el-option label="顺祝" value="1" onselect="qixue_5" style="color: indigo"></el-option>
          <el-option label="罔替" value="2" onselect="qixue_5"  disabled></el-option>
          <el-option label="地遁" value="3" onselect="qixue_5"  disabled></el-option>
          <el-option label="星合" value="4" onselect="qixue_5"  disabled></el-option>
        </el-select>
          <el-select v-model="form.qixue_6" style="width: 80px">
          <el-option label="鬼遁" value="1" onselect="qixue_6" style="color: indigo"></el-option>
          <el-option label="神遁" value="2" onselect="qixue_6"></el-option>
          <el-option label="风遁" value="3" onselect="qixue_6"></el-option>
          <el-option label="天医" value="4" onselect="qixue_6"></el-option>
        </el-select>
          <el-select v-model="form.qixue_7" style="width: 80px">
            <el-option label="祝祷" value="1" onselect="qixue_7" style="color: indigo"></el-option>
            <el-option label="虎遁" value="2" onselect="qixue_7"></el-option>
            <el-option label="延年" value="3" onselect="qixue_7"></el-option>
            <el-option label="移魂" value="4" onselect="qixue_7"></el-option>
          </el-select>
          <el-select v-model="form.qixue_8" style="width: 80px">
            <el-option label="神元" value="1" onselect="qixue_8" style="color: indigo"></el-option>
            <el-option label="覆舟" value="2" onselect="qixue_8"></el-option>
            <el-option label="神俱" value="3" onselect="qixue_8"></el-option>
            <el-option label="虎猖狂" value="4" onselect="qixue_8"></el-option>
            <el-option label="知微" value="5" onselect="qixue_8"></el-option>
          </el-select>
          <el-select v-model="form.qixue_9" style="width: 80px">
            <el-option label="枭神" value="1" onselect="qixue_9"></el-option>
            <el-option label="比扶" value="2" onselect="qixue_9" disabled></el-option>
            <el-option label="器盈" value="3" onselect="qixue_9"></el-option>
            <el-option label="休囚" value="4" onselect="qixue_9"></el-option>
            <el-option label="亘天" value="5" onselect="qixue_9" style="color: indigo"></el-option>
          </el-select>
          <el-select v-model="form.qixue_10" style="width: 90px">
            <el-option label="荧入白" value="1" onselect="qixue_10" style="color: indigo"></el-option>
            <el-option label="伏位" value="2" onselect="qixue_10"></el-option>
            <el-option label="天钺" value="3" onselect="qixue_10"></el-option>
            <el-option label="龙马出河" value="4" onselect="qixue_10"></el-option>
            <el-option label="华盖" value="5" onselect="qixue_10"></el-option>
          </el-select>
          <el-select v-model="form.qixue_11" style="width: 80px">
            <el-option label="擎羊" value="1" onselect="qixue_11" disabled></el-option>
            <el-option label="灵器" value="2" onselect="qixue_11" style="color: indigo"></el-option>
            <el-option label="焚如" value="3" onselect="qixue_11" style="color: indigo"></el-option>
            <el-option label="直符" value="4" onselect="qixue_11" disabled></el-option>
            <el-option label="连断" value="5" onselect="qixue_11" disabled></el-option>
          </el-select>
          <el-select v-model="form.qixue_12" style="width: 110px">
            <el-option label="增卜" value="1" onselect="qixue_12" ></el-option>
            <el-option label="征凶" value="2" onselect="qixue_12" style="color: indigo"></el-option>
            <el-option label="洞彻九宫" value="3" onselect="qixue_12" disabled></el-option>
            <el-option label="杀星在尾" value="4" onselect="qixue_12" style="color: indigo"></el-option>
            <el-option label="连极阵" value="5" onselect="qixue_12" disabled></el-option>
          </el-select>
          <br><label>奇穴紫色选项为计算器已实装奇穴，同层选择其他奇穴可取消其效果，不影响技能循环</label>
        </el-form-item>
        <el-form-item label="阵眼" >
          <el-select v-model="form.zhenyan" style="width: 120px">
            <el-option label="无阵眼" value="1" onselect="zhenyan" ></el-option>
            <el-option label="花间阵" value="2" onselect="zhenyan" ></el-option>
            <el-option label="气纯阵" value="3" onselect="zhenyan" ></el-option>
            <el-option label="大师阵" value="4" onselect="zhenyan" ></el-option>
            <el-option label="田螺阵" value="5" onselect="zhenyan" ></el-option>
            <el-option label="毒经阵" value="6" onselect="zhenyan" ></el-option>
            <el-option label="衍天阵-自己" value="7" onselect="zhenyan" ></el-option>
            <el-option label="衍天阵-同门" value="8" onselect="zhenyan" ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="增益" >
          <el-checkbox-group v-model="form.buff">
            <el-checkbox label="套装+技能伤害" name="buff" disabled></el-checkbox>
            <el-checkbox label="套装+攻击" name="buff" disabled></el-checkbox>
            <el-checkbox label="袖气" name="buff" disabled></el-checkbox>
            <el-checkbox label="破苍穹" name="buff" ></el-checkbox>
            <el-checkbox label="梅花盾" name="buff"></el-checkbox>
<!--            <el-checkbox label="金刚怒目" name="buff" disabled></el-checkbox>-->
            <el-checkbox label="清涓" name="buff" ></el-checkbox>
            <el-checkbox label="分澜" name="buff" ></el-checkbox>
            <el-checkbox label="戒火斩" name="buff" disabled></el-checkbox>
            <el-checkbox label="疏狂" name="buff" disabled></el-checkbox>
            <el-checkbox label="朝圣言" name="buff" disabled></el-checkbox>
<!--            <el-checkbox label="寒啸千军" name="buff" disabled></el-checkbox>-->
            <el-checkbox label="弘法" name="buff" ></el-checkbox>

          </el-checkbox-group>
        </el-form-item>
        <el-form-item label="小吃小药" >
          <el-checkbox-group v-model="form.med">
            <el-checkbox label="增食" name="med" disabled></el-checkbox>
            <el-checkbox label="增药" name="med" disabled></el-checkbox>
            <el-checkbox label="辅食" name="med" disabled></el-checkbox>
            <el-checkbox label="辅药" name="med" disabled></el-checkbox>
            <el-checkbox label="桌子" name="med" disabled></el-checkbox>
            <el-checkbox label="蒸鱼" name="med" disabled></el-checkbox>
            <el-checkbox label="水煮鱼" name="med" disabled></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item label="目标" >
          <el-select v-model="form.target" style="width: 120px">
<!--            <el-option label="110级" value="1" onselect="target" disabled></el-option>-->
            <el-option label="111级" value="2" onselect="target"></el-option>
            <el-option label="112级" value="3" onselect="target"></el-option>
            <el-option label="113级" value="4" onselect="target"></el-option>
            <el-option label="114级" value="5" onselect="target"></el-option>
          </el-select>
          <el-radio-group v-model="form.ping" style="margin-left: 20%">
            <el-radio :label="1">0延迟</el-radio>
            <el-radio :label="2">正常玩家(0-60ms)</el-radio>
            <el-radio :label="3">中PING战士(60-120ms)</el-radio>
            <el-radio :label="4">高PING战士(120+ms)</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="变卦策略">
          <el-button @click="guaxiang = true" type="primary" style="margin-left: 16px;">
            点击修改
          </el-button>
        </el-form-item>
        <el-form-item label="计算模式">
          <el-checkbox-group :max="1" v-model="form.models_check">
            <el-checkbox v-for="model in form.models" :label="model" :key="model">{{model}}</el-checkbox>
          </el-checkbox-group>
        </el-form-item>

        <el-drawer
          title="卦象"
          :visible.sync="guaxiang"
          :with-header="false">
          <div>
            <el-form-item label="山卦">
              <el-switch
                v-model="form.shan_ifbian"
                :onclick="this.shan_bian"
                active-color="#ff4949"
                active-text="不变卦"
                inactive-color="#13ce66"
                inactive-text="变卦"
              >
              </el-switch>
              <div class="block">
                <span class="demonstration" >变火概率</span>
                <el-slider v-model="form.shan_bian_huo"  v-bind:disabled="form.shan_ifbian" show-input></el-slider>
              </div>
            </el-form-item>
            <el-form-item label="水卦">
              <el-switch
                v-model="form.shui_ifbian"
                :onclick="this.shui_bian"
                active-color="#ff4949"
                active-text="不变卦"
                inactive-color="#13ce66"
                inactive-text="变卦"
              >
              </el-switch>
              <div class="block">
                <span class="demonstration" >变山概率</span>
                <el-slider v-model="form.shui_bian_shan" v-bind:disabled="form.shui_ifbian" show-input></el-slider>
              </div>
            </el-form-item>
            <el-form-item label="火卦">
              <el-switch
                v-model="form.huo_ifbian"
                :onclick="this.huo_bian"
                active-color="#ff4949"
                active-text="不变卦"
                inactive-color="#13ce66"
                inactive-text="变卦"
              >
              </el-switch>
              <div class="block">
                <span class="demonstration" >变山概率</span>
                <el-slider v-model="form.huo_bian_shan" v-bind:disabled="form.huo_ifbian" show-input></el-slider>
              </div>
            </el-form-item>
          </div>

        </el-drawer>


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

        <el-button type="success"  round @click="onSubmit()" style="margin-left: 16px;" :disabled="isDisabled" :loading="isDisabled">计算</el-button>
        <el-button @click="res = true" round type="primary" style="margin-left: 16px;">
          查看详细
        </el-button> DPS:{{dps}}
        <br>
        <br>
        <br>
        <el-button @click="auth = true" round type="primary" style="margin-left: 16px;">
          测试伤害
        </el-button>
        <el-button @click="skill_logs = true" round type="primary" style="margin-left: 16px;">
          技能日志
        </el-button>
        <el-button @click="skill_sim_logs = true" round type="primary" style="margin-left: 16px;">
          技能简易日志
        </el-button>
      </el-form>


      <el-drawer
        title="DPS统计"
        :visible.sync="res"
        :with-header="false">
        <el-table
          :data="dpsData"
          :key="itemkey"
          style="width: 100%"
          height="80%"
        >
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="dps">
                  <span>{{ props.row.dps }}</span>
                </el-form-item>
                <el-form-item label="兵主逆">
                  <span>{{ props.row.兵主逆 }}</span>
                </el-form-item>
                <el-form-item label="杀星在尾">
                  <span>{{ props.row.杀星在尾 }}</span>
                </el-form-item>
                <el-form-item label="天斗旋">
                  <span>{{ props.row.天斗旋 }}</span>
                </el-form-item>
                <el-form-item label="破">
                  <span>{{ props.row.破 }}</span>
                </el-form-item>
                <el-form-item label="灵器">
                  <span>{{ props.row.灵器 }}</span>
                </el-form-item>
                <el-form-item label="三星临">
                  <span>{{ props.row.三星临 }}</span>
                </el-form-item>
                <el-form-item label="往者定">
                  <span>{{ props.row.往者定 }}</span>
                </el-form-item>
                <el-form-item label="鬼星开穴">
                  <span>{{ props.row.鬼星开穴 }}</span>
                </el-form-item>
                <el-form-item label="卦象·火离">
                  <span>{{ props.row.卦象·火离 }}</span>
                </el-form-item>

                <el-form-item label="73元气提升" style="width: 300px" size="mini">
                  <span>{{ props.row.dps_yuanqi }}</span>
                </el-form-item>
                <el-form-item label="175攻击提升" style="width: 300px" size="mini">
                  <span>{{ props.row.dps_gongji }}</span>
                </el-form-item>
                <el-form-item label="325无双提升" style="width: 100%" size="mini">
                  <span>{{ props.row.dps_wushuang }}</span>
                </el-form-item>
                <el-form-item label="325破防提升" style="width: 100%" size="mini">
                  <span>{{ props.row.dps_pofang }}</span>
                </el-form-item>
                <el-form-item label="325会心提升" style="width: 100%" size="mini">
                  <span>{{ props.row.dps_huixin }}</span>
                </el-form-item>
                <el-form-item label="325会效提升" style="width: 100%" size="mini">
                  <span>{{ props.row.dps_huixiao }}</span>
                </el-form-item>
                <el-form-item label="325破招提升" style="width: 100%" size="mini">
                  <span>{{ props.row.dps_pozhao }}</span>
                </el-form-item>
              </el-form>
            </template>

          </el-table-column>
          <el-table-column
            label="dps"
            prop="dps">
          </el-table-column>

        </el-table>
      </el-drawer>
      <el-drawer
        title="测试伤害"
        :visible.sync="auth"
        :with-header="false">
        <table>
          <tr v-for="key in authData">
            <td>{{key[0]}}</td>
            <td>{{key[1]}}</td>
            <td>{{key[2]}}</td>

          </tr>
        </table>
        <el-button type="primary" @click="auth_dps" style="margin-left: 16px;">测试伤害</el-button><br>
        <label>测试时请注意相蚀（点了相蚀打完3跳兵再打临）和正夏明心奇穴</label>
      </el-drawer>
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
              prop="time_stamp"
              label="时间戳"
              width="150">
            </el-table-column>
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
      <el-drawer
        title="技能简易日志"
        :visible.sync="skill_sim_logs"
        :with-header="false">
        <div>
          <el-table
            :data="skill_sim_log"
            style="width: 100%"
            height="700">
            <el-table-column
              fixed
              prop="time_stamp"
              label="时间戳"
              width="150">
            </el-table-column>
            <el-table-column
              fixed
              prop="name"
              label="技能名称"
              width="150">
            </el-table-column>
            <el-table-column
              fixed
              prop="type"
              label="施放类型"
              width="150">
            </el-table-column>
          </el-table>
        </div>
      </el-drawer>

    </div>

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
</style>
<script>
  // import { mapGetters } from 'vuex'
  import { cal } from '@/api/cal'
  import { authdps } from '../../api/cal'


  export default {
    name: 'home',
    data() {
      return {
        isDisabled:false,
        dpsData: [],
        skill_log:[],
        skill_sim_log:[],
        authData: [],
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
        skill_sim_logs:false,
        form: {
          ping:2,
          models_check:["稳定模式(满星运起手只出火并必变山） -- 并提供当前属性收益"],
          models:["稳定模式(满星运起手只出火并必变山） -- 并提供当前属性收益","黑鬼模式（0星运起手只出水必变山）"],
          shan_ifbian:true,
          shui_ifbian:false,
          huo_ifbian:false,
          shan_bian_huo:50,
          shui_bian_shan:50,
          huo_bian_shan:50,
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
          qixue_1:'2',
          qixue_2:'1',
          qixue_3:'1',
          qixue_4:'1',
          qixue_5:'1',
          qixue_6:'1',
          qixue_7:'1',
          qixue_8:'1',
          qixue_9:'1',
          qixue_10:'1',
          qixue_11:'2',
          qixue_12:'4',
          zhenyan:'1',
          buff: [],
          med: [],
          target:'4',
        }
      }
    },
    methods: {
      shan_bian(){
        this.form.shan_ifbian = this.form.shan_ifbian !== true;
        this.shan_text_bian()
      },
      shui_bian(){
        this.form.shan_ifbian = this.form.shan_ifbian !== true;
      },
      huo_bian(){
        this.form.shan_ifbian = this.form.shan_ifbian !== true;
      },
      onSubmit() {
        this.isDisabled = true
        setTimeout(() => {
          this.isDisabled = false

        },3000)
        cal(this.form).then(response => {
          this.skill_log = []
          this.skill_log = response.data.skill_log
          this.skill_sim_log = []
          this.skill_sim_log = response.data.skill_sim_log
          this.dps = response.data.dps
          this.dpsData.push(response.data)
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
      ouhuang_heigui(){
        if (this.form.wendingmoshi === false){this.form.heiguimoshi = false}
        if (this.form.heiguimoshi === false){this.form.wendingmoshi = false}
      },
      qixue_1(value){
        this.data.qixue_1 = value
      },
      qixue_2(value){
        this.data.qixue_2 = value
      },
      qixue_3(value){
        this.data.qixue_3 = value
      },
      qixue_4(value){
        this.data.qixue_4 = value
      },
      qixue_5(value){
        this.data.qixue_5 = value
      },
      qixue_6(value){
        this.data.qixue_6 = value
      },
      qixue_7(value){
        this.data.qixue_7 = value
      },
      qixue_8(value){
        this.data.qixue_8 = value
      },
      qixue_9(value){
        this.data.qixue_9 = value
      },
      qixue_10(value){
        this.data.qixue_10 = value
      },
      qixue_11(value){
        this.data.qixue_11 = value
      },
      qixue_12(value){
        this.data.qixue_12 = value
      },
      zhenyan(value){
        this.data.zhenyan = value
      },
      target(value){
        this.data.target = value
      },
    }
  }
</script>
