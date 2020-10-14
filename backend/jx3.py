from django.shortcuts import render
import pymysql
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
import json
import numpy
import copy
import random
from .Judge import Judge
from .Skill import Skill

class Damage:
    def __init__(self,res):
        self.res = res
        self.biangua_celue = {
            "山卦":{
                "变卦":False,
                "概率":0.5,
            },
            "水卦":{
                "变卦":True,
                "概率":0.5,
            },
            "火卦":{
                "变卦":True,
                "概率":0.5,
            }
        }
        if self.res["shan_ifbian"] == True:
            self.biangua_celue["山卦"]["变卦"] = False
            self.biangua_celue["山卦"]["概率"] = 0.5
        else:
            self.biangua_celue["山卦"]["变卦"] = True
            self.biangua_celue["山卦"]["概率"] = round(int(self.res["shan_bian_huo"])*0.01,2)
        if self.res["shui_ifbian"] == True:
            self.biangua_celue["水卦"]["变卦"] = False
            self.biangua_celue["水卦"]["概率"] = 0.5
        else:
            self.biangua_celue["水卦"]["变卦"] = True
            self.biangua_celue["水卦"]["概率"] = round(int(self.res["shui_bian_shan"])*0.01,2)
        if self.res["huo_ifbian"] == True:
            self.biangua_celue["火卦"]["变卦"] = False
            self.biangua_celue["火卦"]["概率"] = 0.5
        else:
            self.biangua_celue["火卦"]["变卦"] = True
            self.biangua_celue["火卦"]["概率"] = round(int(self.res["huo_bian_shan"])*0.01,2)
        if self.res["qixue_12"] == "2":
            self.biangua_celue["山卦"]["变卦"] = True
            self.biangua_celue["山卦"]["概率"] = 1
            self.biangua_celue["火卦"]["变卦"] = True
            self.biangua_celue["火卦"]["概率"] = 1
            self.biangua_celue["水卦"]["变卦"] = True
            self.biangua_celue["水卦"]["概率"] = 0.5


        self.skill_sim_log = []
        self.skill_log = []
        self.current_buff = []
        self.deng_gcd = 0
        self.xingyun = 0 #上限100
        if self.res["models_check"] == ["稳定模式(满星运起手只出火并必变山） -- 并提供当前属性收益"]:
            self.xingyun = 100
            self.biangua_celue["火卦"]["变卦"] = True
        elif self.res["models_check"] == ["黑鬼模式（0星运起手只出水必变山）"]:
            self.biangua_celue["水卦"]["变卦"] = True
        self.current = {
            "name":[""],
            "time":0,
        }
        self.target = {
            "火离":{
                "存在":False,
                "跳数":0,
                "GCD":Skill(self.res).huo[6],
                "cold_down":Skill(self.res).huo[6],
            },
            "杀星在尾1":{
                "存在":False,
                "跳数":0,
                "GCD":1,
                "cold_down":1,
            },
            "杀星在尾2":{
                "存在":False,
                "跳数":0,
                "GCD":1,
                "cold_down":1,
            },
            "兵主逆":{
                "存在":False,
                "跳数":0,
                "GCD":Skill(self.res).bing[6],
                "cold_down":Skill(self.res).bing[6],
            },

        }
        self.qi_delay = [-1]
        self.skills = {
                        "奇门飞宫":{
                            "CD":14,
                            "充能":2,
                            "剩余充能":2,
                            "消耗":0,
                            "cold_down":0,
                        },
                        "灵器":{
                            "CD":0,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":0,
                            "cold_down":0,
                        },
                        "天斗旋":{
                            "CD":4,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":-20,
                            "cold_down":0,
                        },
                        "兵主逆":{
                            "CD":5,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":-15,
                            "cold_down":0,
                        },
                        "三星临":{
                            "CD":0,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":-5,
                            "cold_down":0,
                        },
                        "往者定":{
                            "CD":20,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":0,
                            "cold_down":0,
                        },
                        "杀星在尾":{
                            "CD":45,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":0,
                            "cold_down":0,
                        },
                        "返闭惊魂":{
                            "CD":22,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":0,
                            "cold_down":0,
                        },
                        "鬼星开穴":{
                            "CD":10,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":60,
                            "cold_down":0,
                        },
                        "起卦":{
                            "CD":20,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":0,
                            "cold_down":0,
                        },
                        "变卦":{
                            "CD":20,
                            "充能":1,
                            "剩余充能":1,
                            "消耗":45,
                            "cold_down":0,
                        },
                        "祝由·火离":{
                            "CD":0,
                            "充能":0,
                            "剩余充能":0,
                            "消耗":0,
                            "cold_down":0,
                        },
        }
        # 奇穴亘天天斗旋充能
        if self.res["qixue_9"] == "5":
            self.skills["天斗旋"]["充能"] =3
            self.skills["天斗旋"]["剩余充能"] =3
        self.buffs = {
                        "魂灯1":{
                            "存在":False,
                            "time":0,
                        },
                        "魂灯2":{
                            "存在":False,
                            "time":0,
                        },
                        "魂灯3":{
                            "存在":False,
                            "time":0,
                        },
                        "魂阵":{
                            "存在":False,
                            "time":0,
                        },
                        "鬼遁":{
                            "存在":False,
                            "time":0,
                        },
                        "荧入白":{
                            "存在":False,
                            "time":0,
                        },
                        "山艮":{
                            "存在":False,
                            "time":0,
                        },
                        "水坎":{
                            "存在":False,
                            "time":0,
                        },
                        "火离":{
                            "存在":False,
                            "time":0,
                        },
                        "祝祷":{
                            "存在":False,
                            "time":0,
                        },

        }
    # 星运消耗计算
    # def cal_xingyun(self,skill):
    #     cal = self.skills[skill]["消耗"]
    #     self.xingyun -= cal
    #     if self.xingyun < 0:
    #         return False
    #     elif self.xingyun > 100:
    #         self.xingyun = 100
    #         return True
    #     else:
    #         return True
    # 技能释放日志
    def log(self,skill_name,damage,buff,time_stamp):
        self.skill_log.append(
                {
                    "name":skill_name,
                    "damage":int(damage[0]),
                    "buff":buff,
                    "time_stamp":time_stamp,
                }
        )
    def sim_log(self,skill_name,skill_type,time_stamp):
        self.skill_sim_log.append(
                {
                    "name":skill_name,
                    "type":skill_type,
                    "time_stamp":time_stamp,
                }
        )
    # 每帧开始的时候刷新BUFF
    def time_start(self,t):
        # 判定是否有加强魂阵在场，方便判断触发灵器
        if self.buffs["魂灯1"]["存在"] :
            if self.buffs["魂灯2"]["存在"] :
                if self.buffs["魂灯3"]["存在"] :
                    self.buffs["魂阵"]["存在"] = True
                    # self.buffs["魂阵"]["time"] = min(self.buffs["魂灯1"]["time"],self.buffs["魂灯2"]["time"],self.buffs["魂灯3"]["time"])
        # 判定是否触发荧入白
        if self.buffs["山艮"]["存在"]:
            if self.res["qixue_10"] == "1":
                self.buffs["荧入白"]["存在"] = True
        if self.buffs["水坎"]["存在"] :
            if self.res["qixue_10"] == "1":
                self.buffs["荧入白"]["存在"] = True
        if self.buffs["火离"]["存在"] :
            if self.res["qixue_10"] == "1":
                self.buffs["荧入白"]["存在"] = True
        # 判定是否触发祝祷
        if self.xingyun > 40:
            if self.res["qixue_7"] == "1":
                self.buffs["祝祷"]["存在"] = True
        # 将所有触发的buff添加进即时buff列表
        for key in self.buffs.keys():
            if self.buffs[key]["存在"] :
                self.current_buff.append(key)
        # 起卦延迟2s触发生效
        if self.qi_delay[0] == 0 :
            # 稳定模式
            if self.res["models_check"] == ["稳定模式(满星运起手只出火并必变山） -- 并提供当前属性收益"]:
                gua = "火离"
            elif self.res["models_check"] == ["黑鬼模式（0星运起手只出水必变山）"]:
                gua = "水坎"
            else:
                gua_list = ["火离","山艮","水坎"]
                gua = random.choice(gua_list)
            if gua == "火离":
                self.skills["祝由·火离"]["剩余充能"] = 1
            self.buffs[gua]["存在"] = True
            self.buffs[gua]["time"] = 19
            self.qi_delay[0] -= 0.0625
            self.log(gua,[0,],[],t)
            self.sim_log(gua,"卦象生成",t)
        else:
            self.qi_delay[0] -= 0.0625
    # 结算dot
    def dot_pass(self,t):
        buff_list = []
        buff = copy.copy(self.current_buff)
        if "荧入白" in buff and self.res["qixue_10"] == "1":
            buff_list.append("荧入白")
        if "祝祷" in buff and self.res["qixue_7"] == "1":
            buff_list.append("祝祷")
        if "鬼遁" in buff and self.res["qixue_6"] == "1":
            buff_list.append("鬼遁")
        for key,value in self.target.items():
            if self.target[key]["存在"] and self.target[key]["跳数"]>0:
                self.target[key]["cold_down"] -= 0.0625
                if self.target[key]["cold_down"] == 0:
                    if key == "火离":
                        damage = Judge(self.res,Skill(self.res).huo,buff_list).d()
                        self.log("火离",damage,buff_list,t)
                        self.target[key]["跳数"] -= 1
                        self.target[key]["cold_down"] = self.target[key]["GCD"]
                        if self.target[key]["跳数"] == 0 :
                            self.target[key]["存在"] = False
                            self.sim_log("祝由·火离","火离消失",t)
                    elif key == "杀星在尾1":
                        damage = Judge(self.res,Skill(self.res).sha,buff_list).d()
                        self.log("杀星在尾",damage,buff_list,t)
                        self.target[key]["跳数"] -= 1
                        self.target[key]["cold_down"] = self.target[key]["GCD"]
                        if self.target[key]["跳数"] == 0 :
                            self.target[key]["存在"] = False
                            self.sim_log("杀星在尾","杀星消失",t)
                    elif key == "杀星在尾2":
                        damage = Judge(self.res,Skill(self.res).sha,buff_list).d()
                        self.log("杀星在尾",damage,buff_list,t)
                        self.target[key]["跳数"] -= 1
                        self.target[key]["cold_down"] = self.target[key]["GCD"]
                        if self.target[key]["跳数"] == 0 :
                            self.target[key]["存在"] = False
                    elif key == "兵主逆":
                        damage = Judge(self.res,Skill(self.res).bing,buff).d()
                        self.log("兵主逆",damage,buff,t)
                        self.target[key]["跳数"] -= 1
                        self.target[key]["cold_down"] = self.target[key]["GCD"]
                        # 触发灵器
                        if "魂阵" in self.current_buff:
                            buff_1 = []
                            if "鬼遁" in buff:
                                buff_1.append("鬼遁")
                            if "祝祷" in buff:
                                buff_1.append("祝祷")
                            if "荧入白" in buff:
                                buff_1.append("荧入白")
                            damage_1 = Judge(self.res,Skill(self.res).ling,buff_1).d()
                            self.log("灵器",damage_1,buff_1,t)
                            self.xingyun -= self.skills["灵器"]["消耗"]
                        if self.target[key]["跳数"] == 0 :
                            self.target[key]["存在"] = False
    # 时间结算
    def time_pass(self,t):
        self.dot_pass(t)
        self.current_buff = [] # 清空即时buff列表
        # 转GCD
        self.current["time"] -= 0.0625
        if self.current["time"] == 0:
            self.current["name"] = [""]
        # 技能计时
        for key,value in self.skills.items():
            if self.skills[key]["充能"] > self.skills[key]["剩余充能"]:
                self.skills[key]["cold_down"] -= 0.0625
                if self.skills[key]["cold_down"] == 0:
                    self.skills[key]["剩余充能"] += 1
                    if self.skills[key]["充能"] > self.skills[key]["剩余充能"]:
                        self.skills[key]["cold_down"] = self.skills[key]["CD"]
        # buff计时
        for key,value in self.buffs.items():
            if self.buffs[key]["存在"] is True:
                self.buffs[key]["time"] -= 0.0625
                if self.buffs[key]["time"] <= 0 :
                    self.buffs[key]["存在"] = False
        # 放灯GCD
        if self.deng_gcd > 0 :
            self.deng_gcd -= 1
        # # 起卦延迟2s触发生效
        # if self.qi_delay[0] == 0 :
        #     gua_list = ["火离","山艮","水坎"]
        #     gua = random.choice(gua_list)
        #     if gua == "火离":
        #         self.skills["祝由·火离"]["剩余充能"] = 1
        #     self.buffs[gua]["存在"] = True
        #     self.buffs[gua]["time"] = 19
        #     self.qi_delay[0] -= 0.0625
        #     self.log(gua,[0,],[],t)
        # else:
        #     self.qi_delay[0] -= 0.0625
    # 返闭惊魂
    def fanbijinghun(self,t):
        if self.skills["返闭惊魂"]["剩余充能"] >0 and self.current["name"][0] != "天斗旋" and self.current["name"][0] != "兵主逆":
            if self.buffs["魂灯1"]["存在"] is False:
                self.buffs["魂灯1"]["存在"] = True
                self.buffs["魂灯1"]["time"] = 40
                self.skills["返闭惊魂"]["剩余充能"] -= 1
                if self.skills["返闭惊魂"]["充能"] - self.skills["返闭惊魂"]["剩余充能"] == 1:
                    self.skills["返闭惊魂"]["cold_down"] = self.skills["返闭惊魂"]["CD"]
                buff = copy.copy(self.current_buff)
                damage = [0,]
                self.log("返闭惊魂",damage,buff,t)
                self.sim_log("返闭惊魂","技能施放",t)
            else:
                if self.buffs["魂灯2"]["存在"] is False:
                    self.buffs["魂灯2"]["存在"] = True
                    self.buffs["魂灯2"]["time"] = 40
                    self.skills["返闭惊魂"]["剩余充能"] -= 1
                    if self.skills["返闭惊魂"]["充能"] - self.skills["返闭惊魂"]["剩余充能"] == 1:
                        self.skills["返闭惊魂"]["cold_down"] = self.skills["返闭惊魂"]["CD"]
                    buff = copy.copy(self.current_buff)
                    damage = [0,]
                    self.log("返闭惊魂",damage,buff,t)
                    self.sim_log("返闭惊魂","技能施放",t)
                else:
                    if self.buffs["魂灯3"]["存在"] is False:
                        self.buffs["魂灯3"]["存在"] = True
                        self.buffs["魂灯3"]["time"] = 40
                        self.skills["返闭惊魂"]["剩余充能"] -= 1
                        if self.skills["返闭惊魂"]["充能"] - self.skills["返闭惊魂"]["剩余充能"] == 1:
                            self.skills["返闭惊魂"]["cold_down"] = self.skills["返闭惊魂"]["CD"]
                        buff = copy.copy(self.current_buff)
                        damage = [0,]
                        self.log("返闭惊魂",damage,buff,t)
                        self.sim_log("返闭惊魂","技能施放",t)
    # 奇门飞宫
    def qimenfeigong(self,t):
        if self.skills["奇门飞宫"]["剩余充能"] >0 and self.deng_gcd == 0 and self.buffs["魂阵"]["存在"] == False and self.current["name"][0] != "天斗旋" and self.current["name"][0] != "兵主逆":
            if self.buffs["魂灯1"]["存在"] is False:
                self.buffs["魂灯1"]["存在"] = True
                self.buffs["魂灯1"]["time"] = 40
                self.skills["奇门飞宫"]["剩余充能"] -= 1
                if self.skills["奇门飞宫"]["充能"] - self.skills["奇门飞宫"]["剩余充能"] == 1:
                    self.skills["奇门飞宫"]["cold_down"] = self.skills["奇门飞宫"]["CD"]
                self.deng_gcd = 14
                buff = copy.copy(self.current_buff)
                damage = [0,]
                self.log("奇门飞宫",damage,buff,t)
                self.sim_log("奇门飞宫","技能施放",t)
            else:
                if self.buffs["魂灯2"]["存在"] is False:
                    self.buffs["魂灯2"]["存在"] = True
                    self.buffs["魂灯2"]["time"] = 40
                    self.skills["奇门飞宫"]["剩余充能"] -= 1
                    if self.skills["奇门飞宫"]["充能"] - self.skills["奇门飞宫"]["剩余充能"] == 1:
                        self.skills["奇门飞宫"]["cold_down"] = self.skills["奇门飞宫"]["CD"]
                    self.deng_gcd = 14
                    buff = copy.copy(self.current_buff)
                    damage = [0,]
                    self.log("奇门飞宫",damage,buff,t)
                    self.sim_log("奇门飞宫","技能施放",t)
                else:
                    if self.buffs["魂灯3"]["存在"] is False:
                        self.buffs["魂灯3"]["存在"] = True
                        self.buffs["魂灯3"]["time"] = 40
                        self.skills["奇门飞宫"]["剩余充能"] -= 1
                        if self.skills["奇门飞宫"]["充能"] - self.skills["奇门飞宫"]["剩余充能"] == 1:
                            self.skills["奇门飞宫"]["cold_down"] = self.skills["奇门飞宫"]["CD"]
                        self.deng_gcd = 14
                        self.current_buff.append("魂阵")
                        buff = copy.copy(self.current_buff)
                        damage = [0,]
                        self.log("奇门飞宫",damage,buff,t)
                        self.sim_log("奇门飞宫","技能施放",t)
    #鬼星开穴
    def guixingkaixue(self,t):
        if self.skills["鬼星开穴"]["剩余充能"] >0 and self.buffs["魂灯3"]["存在"] == True and self.deng_gcd == 0 and self.xingyun>=self.skills["鬼星开穴"]["消耗"] and self.current["name"][0] != "天斗旋" and self.current["name"][0] != "兵主逆":
            self.buffs["鬼遁"]["存在"] = True
            self.buffs["鬼遁"]["time"] = 30
            self.buffs["魂灯1"]["存在"] = False
            self.buffs["魂灯1"]["time"] = 0
            self.buffs["魂灯2"]["存在"] = False
            self.buffs["魂灯2"]["time"] = 0
            self.buffs["魂灯3"]["存在"] = False
            self.buffs["魂灯3"]["time"] = 0
            self.buffs["魂阵"]["存在"] = False
            self.buffs["魂阵"]["time"] = 0
            self.current_buff.remove("魂灯1")
            self.current_buff.remove("魂灯2")
            self.current_buff.remove("魂灯3")
            self.current_buff.remove("魂阵")
            if "鬼遁" not in self.current_buff:
                self.current_buff.append("鬼遁")
            self.skills["鬼星开穴"]["剩余充能"] -= 1
            # 如果炸火卦，目标带火离DOT
            if "火离" in self.current_buff:
                if self.target["火离"]["存在"]:
                    self.target["火离"]["跳数"] = 9
                    self.sim_log("祝由·火离","刷新火离跳数",t)
                else:
                    self.target["火离"]["存在"] = True
                    self.target["火离"]["cold_down"] = Skill(self.res).huo[6] #这边模拟的不准确,忘记刷新DOT时间的机制了
                    self.target["火离"]["跳数"] = 9
            # 用完后进CD
            if self.skills["鬼星开穴"]["充能"] - self.skills["鬼星开穴"]["剩余充能"] == 1:
                self.skills["鬼星开穴"]["cold_down"] = self.skills["鬼星开穴"]["CD"]
            self.deng_gcd = 14
            buff = copy.copy(self.current_buff)
            damage = Judge(self.res,Skill(self.res).kai,buff).d()
            self.log("鬼星开穴",damage,buff,t)
            self.sim_log("鬼星开穴","技能施放",t)
            self.xingyun -= self.skills["鬼星开穴"]["消耗"]
    # 起卦
    def qigua(self,t):
        if self.skills["起卦"]["剩余充能"] >0 and self.current["name"][0] != "天斗旋" and self.current["name"][0] != "兵主逆":
            self.qi_delay = [2]
            self.skills["起卦"]["剩余充能"] -= 1
            self.skills["起卦"]["cold_down"] = self.skills["起卦"]["CD"]
            buff = copy.copy(self.current_buff)
            damage = [0,]
            self.log("起卦",damage,buff,t)
            self.sim_log("起卦","起卦",t)
            self.xingyun -= self.skills["起卦"]["消耗"]
    #祝由·火离
    def huoli(self,t):
        if self.skills["祝由·火离"]["剩余充能"] == 1 and self.current["name"][0] != "天斗旋" and self.current["name"][0] != "兵主逆":
            self.skills["祝由·火离"]["剩余充能"] = 0
            if self.target["火离"]["存在"]:
                self.target["火离"]["跳数"] = 9 #这边模拟的不准确,忘记刷新DOT时间的机制了
            else:
                self.target["火离"]["存在"] = True
                self.target["火离"]["cold_down"] = Skill(self.res).huo[6]
                self.target["火离"]["跳数"] = 9
            buff = copy.copy(self.current_buff)
            damage = [0,]
            self.log("火离施放",damage,buff,t)
            self.sim_log("祝由·火离","技能施放",t)
            self.xingyun -= self.skills["祝由·火离"]["消耗"]
    # 变卦
    def biangua(self,t):
        if self.skills["变卦"]["剩余充能"] >0 and self.current["name"][0] != "天斗旋" and self.current["name"][0] != "兵主逆" and self.xingyun>=self.skills["变卦"]["消耗"]:
            if "山艮" in self.current_buff and self.biangua_celue["山卦"]["变卦"]:
                self.skills["变卦"]["剩余充能"] -= 1
                self.skills["变卦"]["cold_down"] = self.skills["变卦"]["CD"]
                self.xingyun -= self.skills["变卦"]["消耗"]
                k = random.random()
                m = self.biangua_celue["山卦"]["概率"]  # 山变火的概率

                if k < m:
                    # 变火卦
                    self.skills["祝由·火离"]["剩余充能"] = 1
                    self.buffs["火离"]["存在"] = True
                    self.buffs["火离"]["time"] = 19
                    self.current_buff.remove("山艮")
                    self.current_buff.append("火离")
                    self.buffs["山艮"]["存在"] = False
                    self.buffs["山艮"]["time"] = 0
                    self.log("变卦·山变火",[0,],[],t)
                    self.sim_log("变卦·山变火","技能施放",t)
                else:
                    # 变水卦
                    self.buffs["水坎"]["存在"] = True
                    self.buffs["水坎"]["time"] = 19
                    self.current_buff.remove("山艮")
                    self.current_buff.append("水坎")
                    self.buffs["山艮"]["存在"] = False
                    self.buffs["山艮"]["time"] = 0
                    self.log("变卦·山变水",[0,],[],t)
                    self.sim_log("变卦·山变水","技能施放",t)
                return
            if "水坎" in self.current_buff and self.biangua_celue["水卦"]["变卦"]:
                self.skills["变卦"]["剩余充能"] -= 1
                self.skills["变卦"]["cold_down"] = self.skills["变卦"]["CD"]
                self.xingyun -= self.skills["变卦"]["消耗"]
                k = random.random()
                if self.res["models_check"] == ["黑鬼模式（0星运起手只出水必变山）"]:
                    m = 1
                else:
                    m = self.biangua_celue["水卦"]["概率"]  # 水变山的概率
                if k < m:
                    # 变山卦
                    self.buffs["山艮"]["存在"] = True
                    self.buffs["山艮"]["time"] = 19
                    self.current_buff.remove("水坎")
                    self.current_buff.append("山艮")
                    self.buffs["水坎"]["存在"] = False
                    self.buffs["水坎"]["time"] = 0
                    self.log("变卦·水变山",[0,],[],t)
                    self.sim_log("变卦·水变山","技能施放",t)
                else:
                    # 变火卦
                    self.skills["祝由·火离"]["剩余充能"] = 1
                    self.buffs["火离"]["存在"] = True
                    self.buffs["火离"]["time"] = 19
                    self.current_buff.remove("水坎")
                    self.current_buff.append("火离")
                    self.buffs["水坎"]["存在"] = False
                    self.buffs["水坎"]["time"] = 0
                    self.log("变卦·水变火",[0,],[],t)
                    self.sim_log("变卦·水变火","技能施放",t)
                return

            if "火离" in self.current_buff and self.biangua_celue["火卦"]["变卦"]:
                self.skills["变卦"]["剩余充能"] -= 1
                self.skills["变卦"]["cold_down"] = self.skills["变卦"]["CD"]
                self.xingyun -= self.skills["变卦"]["消耗"]
                k = random.random()
                if self.res["models_check"] == ["稳定模式(满星运起手只出火并必变山） -- 并提供当前属性收益"]:
                    m = 1
                else:
                    m = self.biangua_celue["火卦"]["概率"]  # 火变山的概率
                if k < m:
                    # 变山卦
                    self.buffs["山艮"]["存在"] = True
                    self.buffs["山艮"]["time"] = 19
                    self.current_buff.remove("火离")
                    self.current_buff.append("山艮")
                    self.buffs["火离"]["存在"] = False
                    self.buffs["火离"]["time"] = 0
                    self.log("变卦·火变山",[0,],[],t)
                    self.sim_log("变卦·火变山","技能施放",t)
                else:
                    # 变水卦
                    self.buffs["水坎"]["存在"] = True
                    self.buffs["水坎"]["time"] = 19
                    self.current_buff.remove("火离")
                    self.current_buff.append("水坎")
                    self.buffs["火离"]["存在"] = False
                    self.buffs["火离"]["time"] = 0
                    self.log("变卦·火变水",[0,],[],t)
                    self.sim_log("变卦·火变水","技能施放",t)
                return
    # 往者定
    def wang(self,t):
        if self.current["time"] == 0 and self.skills["往者定"]["剩余充能"] >= 1:
            self.skills["往者定"]["剩余充能"] -= 1
            self.skills["往者定"]["cold_down"] = self.skills["往者定"]["CD"]
            self.current["name"] = ["往者定"]
            self.current["time"] = Skill(self.res).ding[6]
            buff = copy.copy(self.current_buff)
            damage = Judge(self.res,Skill(self.res).ding,buff).d()
            self.log("往者定",damage,buff,t)
            self.sim_log("往者定","技能施放",t)
            self.xingyun -= self.skills["往者定"]["消耗"]
            # 触发灵器 #往者定还是不触发灵器
            # if "魂阵" in self.current_buff:
            #     buff_1 = []
            #     if "鬼遁" in buff:
            #         buff_1.append("鬼遁")
            #     if "祝祷" in buff:
            #         buff_1.append("祝祷")
            #     if "荧入白" in buff:
            #         buff_1.append("荧入白")
            #     damage_1 = Judge(self.res,Skill(self.res).ling,buff_1).d()
            #     self.log("灵器",damage_1,buff_1,t)
            #     self.xingyun -= self.skills["灵器"]["消耗"]
    # 兵主逆
    def bing(self,t):
        if self.current["time"] == 0 and self.skills["兵主逆"]["剩余充能"] == 1:
            self.skills["兵主逆"]["剩余充能"] -= 1
            self.skills["兵主逆"]["cold_down"] = self.skills["兵主逆"]["CD"]
            self.current["name"] = ["兵主逆"]
            self.current["time"] = Skill(self.res).bing[6]*3+(self.res["ping"]-1)*0.0625
            self.target["兵主逆"]["存在"] = True
            self.target["兵主逆"]["跳数"] = 3
            buff = copy.copy(self.current_buff)
            # damage = Judge(self.res,Skill(self.res).bing,buff).d()
            damage = [0,]
            self.log("兵主逆施放",damage,buff,t)
            self.sim_log("兵主逆","技能施放",t)
            self.xingyun -= self.skills["兵主逆"]["消耗"]
    # 天斗旋
    def dou(self,t):
        if self.current["time"] == 0 and self.skills["天斗旋"]["剩余充能"] >= 1:
            self.skills["天斗旋"]["剩余充能"] -= 1
            self.skills["天斗旋"]["cold_down"] = self.skills["天斗旋"]["CD"]
            self.current["name"] = ["天斗旋"]
            self.current["time"] = Skill(self.res).dou[6]
            buff = copy.copy(self.current_buff)
            damage = Judge(self.res,Skill(self.res).dou,buff).d()
            self.log("天斗旋",damage,buff,t)
            self.sim_log("天斗旋","技能施放",t)
            self.xingyun -= self.skills["天斗旋"]["消耗"]
            # 触发灵器
            if "魂阵" in self.current_buff:
                buff_1 = []
                if "鬼遁" in buff:
                    buff_1.append("鬼遁")
                if "祝祷" in buff:
                    buff_1.append("祝祷")
                if "荧入白" in buff:
                    buff_1.append("荧入白")
                damage_1 = Judge(self.res,Skill(self.res).ling,buff_1).d()
                self.log("灵器",damage_1,buff_1,t)
                self.xingyun -= self.skills["灵器"]["消耗"]
    # 三星临
    def lin(self,t):
        if self.current["time"] == 0 and self.skills["三星临"]["剩余充能"] >= 1:
            self.skills["三星临"]["cold_down"] = self.skills["三星临"]["CD"]
            self.current["name"] = ["三星临"]
            self.current["time"] = Skill(self.res).lin[6]
            buff = copy.copy(self.current_buff)
            damage = Judge(self.res,Skill(self.res).lin,buff).d()
            self.log("三星临",damage,buff,t)
            self.sim_log("三星临","技能施放",t)
            self.xingyun -= self.skills["三星临"]["消耗"]
            # 触发灵器
            if "魂阵" in self.current_buff:
                buff_1 = []
                if "鬼遁" in buff:
                    buff_1.append("鬼遁")
                if "祝祷" in buff:
                    buff_1.append("祝祷")
                if "荧入白" in buff:
                    buff_1.append("荧入白")
                damage_1 = Judge(self.res,Skill(self.res).ling,buff_1).d()
                self.log("灵器",damage_1,buff_1,t)
                self.xingyun -= self.skills["灵器"]["消耗"]
    # 杀星在尾
    def sha(self,t):
        if self.current["time"] == 0 and self.skills["杀星在尾"]["剩余充能"] >= 1:
            self.skills["杀星在尾"]["剩余充能"] -= 1
            self.skills["杀星在尾"]["cold_down"] = self.skills["杀星在尾"]["CD"]
            self.current["name"] = ["杀星在尾"]
            self.current["time"] = Skill(self.res).sha[6]
            self.target["杀星在尾1"]["存在"] = True
            self.target["杀星在尾1"]["跳数"] = 12
            self.target["杀星在尾2"]["存在"] = True
            self.target["杀星在尾2"]["跳数"] = 12
            buff = copy.copy(self.current_buff)
            # damage = Judge(self.res,Skill(self.res).bing,buff).d()
            damage = [0,]
            self.log("杀星在尾施放",damage,buff,t)
            self.sim_log("杀星在尾","技能施放",t)
            self.xingyun -= self.skills["杀星在尾"]["消耗"]
    # 开始模拟
    def start(self):
        # 录入正式循环
        total_time = 300
        for t in numpy.arange(0,total_time,0.0625):
            # print(self.qi_delay,self.current_buff,self.skills["祝由·火离"])
            self.time_start(t)
            # 炸灯
            if self.buffs["魂灯1"]["time"] <10 and self.xingyun >= 60:
                if self.target["杀星在尾1"]["存在"] is False:
                    # 可以炸灯 但是自己是火卦，这个时候不变卦，等火DOT多跳几下再爆灯刷新
                    if self.buffs["火离"]["存在"]:
                        if self.current["time"]==0 and self.buffs["魂灯1"]["time"] < 3 and self.skills["兵主逆"]["剩余充能"] == 1:
                            if self.skills["天斗旋"]["剩余充能"] == 1:
                                if self.buffs["魂灯1"]["time"] < 1.5:
                                    self.guixingkaixue(t)
                                else:
                                    self.dou(t)
                                    self.lin(t)
                            else:
                                self.lin(t)
                                self.guixingkaixue(t)
                        elif self.current["time"]==0 and self.buffs["魂灯1"]["time"] >= 3 and self.skills["兵主逆"]["剩余充能"] == 1:
                            self.bing(t)
                        else:
                            if self.buffs["魂灯1"]["time"] < 1.5:
                                self.guixingkaixue(t)
                            else:
                                self.dou(t)
                                self.lin(t)
                    else:
                        # print(t)
                        # print(self.current_buff)
                        # print(self.buffs)
                        self.guixingkaixue(t)

            # # 炸灯
            # if self.buffs["魂灯3"]["time"] <10 and self.xingyun >= 60:
            #     if self.target["杀星在尾1"]["存在"] is False:
            #             self.guixingkaixue(t)

            # 放灯
            if "魂阵" not in self.current_buff:
                self.fanbijinghun(t)
                self.qimenfeigong(t)
            # 起卦
            if self.buffs["山艮"]["存在"] is False and self.buffs["水坎"]["存在"] is False and self.buffs["火离"]["存在"] is False:
                self.qigua(t)
            if self.buffs["山艮"]["存在"] and self.buffs["山艮"]["time"] < 2 :
                self.qigua(t)
            if self.buffs["水坎"]["存在"] and self.buffs["水坎"]["time"] < 2 :
                self.qigua(t)
            if self.buffs["火离"]["存在"] and self.buffs["火离"]["time"] < 2 :
                self.qigua(t)
            # 杀星
            if self.res["qixue_12"] == "4":
                if self.buffs["魂灯2"]["存在"] and self.buffs["魂灯3"]["存在"] is False:
                    self.sha(t)
                    self.qimenfeigong(t)
                else:
                    if self.buffs["魂灯1"]["time"]> 12 and self.buffs["魂灯1"]["存在"]:
                        self.sha(t)
            # 火离
            # if self.target["火离"]["存在"]:
            #    if self.current["time"]==0 and self.buffs["火离"]["time"] < 3 and self.skills["兵主逆"]["剩余充能"] == 1:
            #                 if self.skills["天斗旋"]["剩余充能"] == 1:
            #                     if self.buffs["火离"]["time"] < 1.5:
            #                         self.huoli(t)
            #                     self.dou(t)
            #                     self.lin(t)
            #                 else:
            #                     self.lin(t)
            #                     self.huoli(t)
            # else:
            self.huoli(t)
            # 变卦
            if self.buffs["火离"]["存在"] and self.buffs["火离"]["time"] > self.buffs["魂灯3"]["time"]:
                pass
            else:
                self.biangua(t)
            self.dou(t)
            # 兵主逆
            if self.buffs["魂阵"]["存在"]:
                self.bing(t)
            # 看情况在放灯的时候垫技能
            if self.buffs["魂灯3"]["存在"] is False and self.buffs["魂灯2"]["存在"]:
                self.wang(t)
            self.lin(t)
            self.time_pass(t)


        # 添加破招伤害
        po_dou = 0
        po_stamp = 0.0
        po_list = []
        for i in self.skill_log:
            if i["damage"] !="0":
                if i["time_stamp"] - po_stamp >= Skill(self.res).po[6]*5:
                    po_dou += 5
                    po_stamp = i["time_stamp"]
                    if po_dou == 5:
                        po_dou = 0
                        buff = copy.copy(i["buff"])
                        buff_list = []
                        if "荧入白" in buff and self.res["qixue_10"] == "1":
                            buff_list.append("荧入白")
                        if "祝祷" in buff and self.res["qixue_7"] == "1":
                            buff_list.append("祝祷")
                        if "鬼遁" in buff and self.res["qixue_6"] == "1":
                            buff_list.append("鬼遁")
                        damage = Judge(self.res,Skill(self.res).po,buff_list).d()
                        po_list.append(
                            {
                                "name":"破",
                                "damage":int(damage[0]),
                                "buff":buff_list,
                                "time_stamp":i["time_stamp"],
                            }
                        )

        for i in po_list:
            self.skill_log.append(i)
        dam = 0
        dam_dic = {
            "往者定": 0,
            "天斗旋": 0,
            "灵器": 0,
            "破": 0,
            "杀星在尾": 0,
            "兵主逆": 0,
            "三星临": 0,
            "鬼星开穴": 0,
            "火离":0,
        }
        for i in self.skill_log:
            if i["name"] in dam_dic:
                dam += i["damage"]
                dam_dic[i["name"]] += i["damage"]
        dps = int(dam/total_time)
        damage_ding = str(round(100*dam_dic["往者定"]/dam,2))+"%"
        damage_dou = str(round(100*dam_dic["天斗旋"]/dam,2))+"%"
        damage_ling = str(round(100*dam_dic["灵器"]/dam,2))+"%"
        damage_po = str(round(100*dam_dic["破"]/dam,2))+"%"
        damage_sha = str(round(100*dam_dic["杀星在尾"]/dam,2))+"%"
        damage_bing = str(round(100*dam_dic["兵主逆"]/dam,2))+"%"
        damage_lin = str(round(100*dam_dic["三星临"]/dam,2))+"%"
        damage_kai = str(round(100*dam_dic["鬼星开穴"]/dam,2))+"%"
        damage_huo = str(round(100*dam_dic["火离"]/dam,2))+"%"
        msg = {
                "data": {"dps": dps,
                         "往者定":damage_ding,
                         "天斗旋":damage_dou,
                         "灵器":damage_ling,
                         "破":damage_po,
                         "杀星在尾":damage_sha,
                         "兵主逆":damage_bing,
                         "三星临":damage_lin,
                         "鬼星开穴":damage_kai,
                         "卦象·火离":damage_huo,
                         "skill_log":self.skill_log,
                         "skill_sim_log":self.skill_sim_log,
                        },
                "code": 20000,
            }

        return msg




def cal(request):
    res = json.loads(request.body)
    msg = Damage(res).start()
    if res["models_check"] == ["稳定模式(满星运起手只出火并必变山） -- 并提供当前属性收益"]:
        res_yuanqi = copy.copy(res)
        res_yuanqi["yuanqi"] = str (int(res_yuanqi["yuanqi"]) + 73 )
        res_gongji = copy.copy(res)
        res_gongji["jichugongji"] = str (int(res_gongji["jichugongji"]) + 175 )
        res_wushuang = copy.copy(res)
        res_wushuang["wushuang"] = str (float(res_wushuang["wushuang"]) + 325/344.5875 )
        res_pofang = copy.copy(res)
        res_pofang["pofang"] = str (float(res_pofang["pofang"]) + 325/357.375 )
        res_huixin = copy.copy(res)
        res_huixin["huixin"] = str (float(res_huixin["huixin"]) + 325/357.375 )
        res_huixiao = copy.copy(res)
        res_huixiao["huixiao"] = str (float(res_huixiao["huixiao"]) + 325/125.0625 )
        res_pozhao = copy.copy(res)
        res_pozhao["pozhao"] = str (int(res_pozhao["pozhao"]) + 325 )
        dps_ori = msg["data"]["dps"]
        dps_yuanqi = Damage(res_yuanqi).start()["data"]["dps"] - dps_ori
        dps_gongji = Damage(res_gongji).start()["data"]["dps"] - dps_ori
        dps_wushuang = Damage(res_wushuang).start()["data"]["dps"] - dps_ori
        dps_pofang = Damage(res_pofang).start()["data"]["dps"] - dps_ori
        dps_huixin = Damage(res_huixin).start()["data"]["dps"] - dps_ori
        dps_huixiao = Damage(res_huixiao).start()["data"]["dps"] - dps_ori
        dps_pozhao = Damage(res_pozhao).start()["data"]["dps"] - dps_ori
        msg["data"]["dps_yuanqi"] = dps_yuanqi
        msg["data"]["dps_gongji"] = dps_gongji
        msg["data"]["dps_wushuang"] = dps_wushuang
        msg["data"]["dps_pofang"] = dps_pofang
        msg["data"]["dps_huixin"] = dps_huixin
        msg["data"]["dps_huixiao"] = dps_huixiao
        msg["data"]["dps_pozhao"] = dps_pozhao
    # gj = []
    # x = range(0,50)
    # dps_oril = msg["data"]["dps"]
    #
    # for k in range(0,50):
    #     res_gj = copy.copy(res)
    #     res_gj["jichugongji"] = str(int(res_gj["jichugongji"]) + k*175)
    #     dps_gj = Damage(res_gj).start()["data"]["dps"] - dps_oril
    #     gj.append(dps_gj)
    # ws = []
    # for k in range(0,50):
    #     res_ws = copy.copy(res)
    #     res_ws["jichugongji"] = str (float(res_ws["wushuang"]) + 325/344.5875 )
    #     dps_ws = Damage(res_gj).start()["data"]["dps"] - dps_oril
    #     ws.append(dps_ws)
    #
    #
    # pyplot.figure(figsize=(20, 8), dpi=80)
    # pyplot.plot(x, gj, label='攻击', )
    # pyplot.plot(x, ws, label='无双', )
    # pyplot.show()
    # print(gj)

    return JsonResponse(msg, safe=False)





def auth(request):
    res = json.loads(request.body)
    result = [
        ["技能","命中伤害","会心伤害"],
        ["三星临+奇穴秘籍",int(Judge(res,Skill(res).lin,[]).t()[0]),int(Judge(res,Skill(res).lin,[]).t()[1])],
        ["三星临+奇穴秘籍+祝祷",int(Judge(res,Skill(res).lin,["祝祷"]).t()[0]),int(Judge(res,Skill(res).lin,["祝祷"]).t()[1])],
        ["三星临+奇穴秘籍+荧入白",int(Judge(res,Skill(res).lin,["荧入白"]).t()[0]),int(Judge(res,Skill(res).lin,["荧入白"]).t()[1])],
        ["三星临+奇穴秘籍+重山",int(Judge(res,Skill(res).lin,["重山"]).t()[0]),int(Judge(res,Skill(res).lin,["重山"]).t()[1])],
        ["三星临+奇穴秘籍+鬼遁",int(Judge(res,Skill(res).lin,["鬼遁"]).t()[0]),int(Judge(res,Skill(res).lin,["鬼遁"]).t()[1])],
        ["三星临+奇穴秘籍+祝祷重山",int(Judge(res,Skill(res).lin,["祝祷","重山"]).t()[0]),int(Judge(res,Skill(res).lin,["祝祷","重山"]).t()[1])],
        ["三星临+奇穴秘籍+祝祷荧入白",int(Judge(res,Skill(res).lin,["祝祷","荧入白"]).t()[0]),int(Judge(res,Skill(res).lin,["祝祷","荧入白"]).t()[1])],
        ["三星临+奇穴秘籍+祝祷鬼遁",int(Judge(res,Skill(res).lin,["祝祷","鬼遁"]).t()[0]),int(Judge(res,Skill(res).lin,["祝祷","鬼遁"]).t()[1])],
        ["三星临+奇穴秘籍+荧入白重山",int(Judge(res,Skill(res).lin,["荧入白","重山"]).t()[0]),int(Judge(res,Skill(res).lin,["荧入白","重山"]).t()[1])],
        ["三星临+奇穴秘籍+荧入白鬼遁",int(Judge(res,Skill(res).lin,["荧入白","鬼遁"]).t()[0]),int(Judge(res,Skill(res).lin,["荧入白","鬼遁"]).t()[1])],
        ["三星临+奇穴秘籍+重山鬼遁",int(Judge(res,Skill(res).lin,["重山","鬼遁"]).t()[0]),int(Judge(res,Skill(res).lin,["重山","鬼遁"]).t()[1])],
        ["三星临+奇穴秘籍+鬼遁祝祷荧入白",int(Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白"]).t()[0]),int(Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白"]).t()[1])],
        ["三星临+奇穴秘籍+重山祝祷荧入白",int(Judge(res,Skill(res).lin,["重山","祝祷","荧入白"]).t()[0]),int(Judge(res,Skill(res).lin,["重山","祝祷","荧入白"]).t()[1])],
        ["三星临+奇穴秘籍+鬼遁重山祝祷荧入白",int(Judge(res,Skill(res).lin,["鬼遁","重山","祝祷","荧入白"]).t()[0]),int(Judge(res,Skill(res).lin,["鬼遁","重山","祝祷","荧入白"]).t()[1])],
        ["兵主逆+奇穴秘籍",int(Judge(res,Skill(res).bing,[]).t()[0]),int(Judge(res,Skill(res).bing,[]).t()[1])],
        ["天斗旋+奇穴秘籍",int(Judge(res,Skill(res).dou,[]).t()[0]),int(Judge(res,Skill(res).dou,[]).t()[1])],
        ["往者定",int(Judge(res,Skill(res).ding,[]).t()[0]),int(Judge(res,Skill(res).ding,[]).t()[1])],
        ["灵器",int(Judge(res,Skill(res).ling,[]).t()[0]),int(Judge(res,Skill(res).ling,[]).t()[1])],
        ["破",int(Judge(res,Skill(res).po,[]).t()[0]),int(Judge(res,Skill(res).po,[]).t()[1])],
        ["杀星在尾",int(Judge(res,Skill(res).sha,[]).t()[0]),int(Judge(res,Skill(res).sha,[]).t()[1])],
        ["鬼星开穴+奇穴秘籍",int(Judge(res,Skill(res).kai,[]).t()[0]),int(Judge(res,Skill(res).kai,[]).t()[1])],
        ["卦象·火离",int(Judge(res,Skill(res).huo,[]).t()[0]),int(Judge(res,Skill(res).huo,[]).t()[1])],
    ]


    msg = {
                "data": result,
                "code": 20000,
            }
    return JsonResponse(msg, safe=False)