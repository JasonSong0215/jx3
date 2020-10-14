<template>
  <div class="home">
    <div class="log">
      <p>10.13 更新阵眼效果及部分实战增益、简易技能日志</p>
      <p>10.10 增加延迟选择以及黑鬼模式，实装征凶的模拟</p>
      <p>10.09 优化输出循环，留火卦，放灯/起卦前垫三星临/往者定</p>
      <p>10.05 更新属性收益</p>
      <p>10.04 更新加速算法，更新技能日志功能，DPS采用真实技能模拟，精确到帧。默认模拟时间为5分钟木桩环境</p>
      <p>9.22更新秘籍</p>
      <p>9.21修正火离次数异常的问题</p>
      <p>本计算器制作于2020-09-19 by电八亢龙-猫大仙 QQ:476675706</p>
      <p>衍天宗PVEQQ群：1151856552</p>
      <p>群内有输出循环手法等文件</p>
    </div>
    <div class="warning">
      <p>有可能存在的BUG</p>
      <p>往者定 作为九字诀不触发灵器</p>
      <p>兵主逆 在山艮BUFF消失的时候可能会有一跳少2K伤害</p>
    </div>
    <div class="warning">
      <p>
        10.09 更新内容 目前已知如下缺陷
      </p>
      <p>
        计算器本身是实际模拟，计算以及反映较慢。
      </p>
      <p>
        没有刻意让鬼遁覆盖杀星
      </p>
      <p>
        没有刻意保祝祷
      </p>
    </div>
    <div class="warning">
      <p>
        10.10技能系数记录，如有更精确的烦请反馈【技能，基础伤害，面板攻击加成系数】
      </p>
      <p>
        往者定：68,1.301
      </p>
      <p>
        兵主逆：578,1.197453
      </p>
      <p>
        三星临：116,1.0778
      </p>
      <p>
        天斗旋：833,2.274
      </p>
      <p>
        破：14.504,0
      </p>
      <p>
        杀星在尾：290,0.93715
      </p>
      <p>
        3灯鬼星开穴：519,3.29
      </p>

      <p>
        卦象·火离：97,1.0414
      </p>
      <p>
        焚如-卦象·火离：97,1.565
      </p>
      <p>
        灵器：65,0.5205
      </p>
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
  export default {
    name: 'log',
    data() {
      return {
      }
    },
  }
</script>
