from django.shortcuts import render
import pymysql
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
import json
import requests
from .Skill import Skill
from .Judge import Judge
# Create your views here.
dic = {
    "huixin":35737.5,
    "huixiao":12506.25,
    "wushuang":34458.75,
    "fangyu":19091.25,
    "pofang":35737.5,# 奉天证道
    # "pofang":15344.2,# 世外蓬莱
    "jiashu":43856.25,
    "xinfa_gongji":1.7998, #心法元气提供的额外内功攻击
    }
def_dic = {
        "111":[5034,20134.905], # 奉天证道
        # "111":[1924,7698.34], #世外蓬莱
        "112":[7060,21178.560],
        "113":[11966,22222.215],
        "114":[12528,23265.870],
        }
acc_dic_1 = {
    "1":[0,0],
    "0.9375":[43,0.09765625],
    "0.875":[2956,6.73828125],
    "0.8125":[6298,14.35546875],
    "0.75":[10153,23.14453125],
}
acc_dic_15 = {
    "1.5":[0,0],
    "1.4375":[43,0.09765625],
    "1.375":[1928,4.39453125],
    "1.3125":[4027,9.1796875],
    "1.25":[6298,14.35546875],
    "1.1875":[8782,20.01953125],
}


# class Judge:
#     def __init__(self,res,skill,buff):
#         self.skill_name = skill[6]
#         self.weapon = 0 # 武伤，衍天没有所以直接0
#         self.skill_basic_damage = skill[0] # 技能基础伤害
#         self.skill_damage_per = skill[1] # 技能伤害系数
#         self.skill_weapon_damage = skill[2] # 技能武器伤害系数
#         self.jichugongji = int(res["jichugongji"]) # 人物初始基础攻击
#         self.huixin = float(res["huixin"])*0.01 + skill[4] # 人物基础会心+技能奇穴会心
#         self.huixiao = float(res["huixiao"])*0.01 + skill[5] # 人物基础会效+技能奇穴会效
#         self.jiasu = int(res["jiasu"])
#         self.wushuang = float(res["wushuang"])
#         self.yuanqi = int(res["yuanqi"])
#         self.pofang = float(res["pofang"])
#         self.pozhao = int(res["pozhao"])
#         self.limit_reduce_defence = 0 #固定减防御
#         self.reduce_defence = 0
#         self.target = res["target"] # 目标等级 1-110级，2-111级，3-112级，4-113级，5-114级
# 
#         # 战斗BUFF+阵眼+小吃小药 带来的额外收益
#         self.ex_gongji = 0
#         self.ex_pofang = 0
#         self.ex_huixin = 0
#         self.ex_huixiao = 0
# 
#         #处理整体技能增伤
#         self.zengshang = 1
#         self.zengshang += skill[3]
# 
#         if "祝祷" in buff:
#             if res["qixue_7"] == "1":
#                 self.zengshang += 0.1
#         if "重山" in buff:
#             if res["qixue_4"] == "1":
#                 self.zengshang = self.zengshang *1.15
# 
# 
# 
#         # 这里处理填数值时选择了神元奇穴但是面板没实际加成上的情况
#         if res["shenyuan_isinclude"] is False:
#             self.huixin += self.yuanqi*0.1*0.42/dic["huixin"]
#             self.pofang += self.yuanqi*0.1*0.3/dic["pofang"]
#             self.jichugongji += int(self.yuanqi*0.1*0.18)
#             self.yuanqi = int(self.yuanqi*1.1)
#         if "梅花盾" in res["buff"]:
#             self.reduce_defence += 0.15 #无视百分比防御
#         if  res["zhenyan"] == "5":
#             self.reduce_defence += 0.05 #无视百分比防御
#         if "荧入白" in buff:
#             if  res["qixue_10"] == "1":
#                 self.reduce_defence += 0.5 #无视百分比防御
#         if "鬼遁" in buff: # 判断buff是否存在
#             if res["qixue_6"] == "1": # 判断是否点奇穴
#                 self.ex_gongji += self.jichugongji*0.15
# 
# 
# 
#         self.fin_gongji = self.jichugongji+int(dic["xinfa_gongji"]*self.yuanqi)+int(self.ex_gongji)  # 这边要加上元气的额外攻击和BUFF提供的攻击
#         self.fin_pofang = self.pofang+self.ex_pofang
#         self.fin_yuanqi = self.yuanqi
#         self.fin_huixin = self.huixin+self.ex_huixin
#         self.fin_huixiao = self.huixiao+self.ex_huixiao
#         self.fin_jiasu = self.jiasu
#         self.fin_wushuang = self.wushuang
# 
# 
#     #防御减伤计算,limit_reduce_defence是固定减防御，reduce_defence是无视百分比防御
#     def guo_defence(self,limit_reduce_defence,reduce_defence):
#         tar_defence_level_111 = (def_dic["111"][0]-limit_reduce_defence)*(1-reduce_defence)
#         tar_defence_level_112 = (def_dic["112"][0]-limit_reduce_defence)*(1-reduce_defence)
#         tar_defence_level_113 = (def_dic["113"][0]-limit_reduce_defence)*(1-reduce_defence)
#         tar_defence_level_114 = (def_dic["114"][0]-limit_reduce_defence)*(1-reduce_defence)
#         def_111 = int(tar_defence_level_111*1024/(tar_defence_level_111+def_dic["111"][1]))
#         def_112 = int(tar_defence_level_112*1024/(tar_defence_level_112+def_dic["112"][1]))
#         def_113 = int(tar_defence_level_113*1024/(tar_defence_level_113+def_dic["113"][1]))
#         def_114 = int(tar_defence_level_114*1024/(tar_defence_level_114+def_dic["114"][1]))
#         res = [def_111,def_112,def_113,def_114]
#         return res
#     #计算郭氏破防值
#     def guo_pofang(self,fin_pofang):
#         pofang_value = int(fin_pofang*0.01*dic["pofang"])
#         guo_pf = int(pofang_value*1024/dic["pofang"])
#         return guo_pf
#     # 原始伤害
#     def damage_ori(self):
#         damage_ori = int(self.skill_basic_damage) + int(float(self.fin_gongji)*self.skill_damage_per)+int(self.weapon*self.skill_weapon_damage)
#         return damage_ori
#     # 计算伤害
#     def d(self):
#         guo_pf = self.guo_pofang(self.fin_pofang)
#         guo_fy = self.guo_defence(self.limit_reduce_defence,self.reduce_defence)[int(self.target)-2]
#         Y = 1024+guo_pf-int((1024+guo_pf)*guo_fy/1024)
#         damage_basic = int(self.damage_ori()*Y/1024) # 基准伤害(破防伤害)
#         # print("最终无双",1+self.fin_wushuang*0.01)
#         damage_basic_wushuang = damage_basic*(1+self.fin_wushuang*0.01) #无双加成后的伤害
#         # 计算会心伤害
#         # 郭氏会效值
#         guo_huixiao = int((self.huixiao-1.75)*1024)
#         # print("郭氏会效值",guo_huixiao)
#         damage_basic_wushuang_huixin = int(damage_basic_wushuang*1.75)+int(damage_basic_wushuang * guo_huixiao/1024)
#         damage_final = ((1-self.huixin)*damage_basic_wushuang+self.huixin*damage_basic_wushuang_huixin)*self.zengshang
#         # print("普通命中",damage_basic_wushuang*self.zengshang,self.zengshang)
#         # print(damage_basic_wushuang_huixin)
#         # print("伤害预期",damage_final)
#         return damage_final,self.skill_name
#     def print_obj(obj):
#         print(obj.__dict__)







# class Skill:
#     def __init__(self,res):
#         #技能基础伤害，技能系数，武伤系数，伤害秘籍+套装伤害+奇穴增伤，会心秘籍+会心奇穴，会效奇穴]
#         self.ding = [36,1.3023,0,0,0,0,"往者定"]
#         self.bing = [65,1.19289544,0,0,0,0,"兵主逆"]
#         self.lin = [36,1.0731,0,0,0,0,"三星临"]
#         self.dou = [36,2.386,0,0,0,0,"天斗旋"]
#         self.po = [16.116,0,0,0,0,0,"破"]
#         self.sha = [290,0.9377,0,0,0,0,"杀星在尾"]
#         self.ling = [65,0.5209,0,0,0,0,"灵器"]
#         self.huo = [109,1.075,0,0,0,0,"卦象·火离"]#未测试
#         self.kai = [36,1.823,0,0,0,0,"鬼星开穴"]
#         self.pozhao = res["pozhao"]
#         self.po[0] = self.po[0] * int(self.pozhao)
#         if res["qixue_1"] == "1": # 正夏
#             self.lin[3] += 0.1
#         if res["qixue_1"] == "2": # 明心
#             self.lin[4] += 0.1
#             self.lin[5] += 0.1
#         if res["qixue_2"] == "1":# 望旗BUFF
#             self.bing[3] += 0.1
#         if res["qixue_3"] == "1":# 相蚀BUFF
#             self.lin[3] += 0.3
#         if "伤害+5%" in res["miji_lin"]:
#             self.lin[3] += 0.05
#         if "伤害+4%" in res["miji_lin"]:
#             self.lin[3] += 0.04
#         if "伤害+3%" in res["miji_lin"]:
#             self.lin[3] += 0.03
#         if "会心+4%" in res["miji_lin"]:
#             self.lin[4] += 0.04
#         if "会心+3%" in res["miji_lin"]:
#             self.lin[4] += 0.03
#         if "会心+2%" in res["miji_lin"]:
#             self.lin[4] += 0.02
#
#
#         if "伤害+5%" in res["miji_bing"]:
#             self.bing[3] += 0.05
#         if "伤害+4%" in res["miji_bing"]:
#             self.bing[3] += 0.04
#         if "伤害+3%" in res["miji_bing"]:
#             self.bing[3] += 0.03
#         if "会心+4%" in res["miji_bing"]:
#             self.bing[4] += 0.04
#         if "会心+3%" in res["miji_bing"]:
#             self.bing[4] += 0.03
#
#         if "伤害+5%" in res["miji_dou"]:
#             self.dou[3] += 0.05
#         if "伤害+4%" in res["miji_dou"]:
#             self.dou[3] += 0.04
#         if "伤害+3%" in res["miji_dou"]:
#             self.dou[3] += 0.03
#         if "会心+4%" in res["miji_dou"]:
#             self.dou[4] += 0.04
#         if "会心+3%" in res["miji_dou"]:
#             self.dou[4] += 0.03
#         if "会心+2%" in res["miji_dou"]:
#             self.dou[4] += 0.02
#
#         if "伤害+5%" in res["miji_kai"]:
#             self.kai[3] += 0.05
#         if "伤害+4%" in res["miji_kai"]:
#             self.kai[3] += 0.04
#         if "会心+4%" in res["miji_kai"]:
#             self.kai[4] += 0.04
#         if "会心+3%" in res["miji_kai"]:
#             self.kai[4] += 0.03


def cal(request):
    res = json.loads(request.body)

    # 注意 重山BUFF只加成九字诀
    # buff = ["鬼遁","荧入白","祝祷","重山"]
    shan_damage = [
        (Judge(res,Skill(res).ding,["鬼遁","祝祷"]).d()[0]*4,"往者定"),
        (Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白",]).d()[0]*2,"天斗旋"),
        (Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白","重山"]).d()[0]*8,"天斗旋"),
        (Judge(res,Skill(res).dou,["祝祷","荧入白","重山"]).d()[0]*4,"天斗旋"),
        (Judge(res,Skill(res).huo,["鬼遁","祝祷","荧入白",]).d()[0]*118/3,"卦象·火离"),
        (Judge(res,Skill(res).huo,["祝祷","荧入白",]).d()[0]*18/3,"卦象·火离"),
        (Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d()[0]*32,"灵器"),
        (Judge(res,Skill(res).ling,["祝祷","荧入白"]).d()[0]*26,"灵器"),
        (Judge(res,Skill(res).po,["鬼遁","祝祷","荧入白"]).d()[0]*4,"破"),
        (Judge(res,Skill(res).po,["祝祷","荧入白"]).d()[0]*3,"破"),
        (Judge(res,Skill(res).po,["鬼遁","祝祷"]).d()[0]*2,"破"),
        (Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d()[0]*48,"杀星在尾"),
        (Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d()[0]*18,"兵主逆"),
        (Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d()[0]*18,"兵主逆"),
        (Judge(res,Skill(res).bing,["鬼遁","祝祷"]).d()[0]*6,"兵主逆"),
        (Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白","重山"]).d()[0]*8,"三星临"),
        (Judge(res,Skill(res).lin,["祝祷","荧入白","重山"]).d()[0]*4,"三星临"),
        (Judge(res,Skill(res).kai,["祝祷","荧入白"]).d()[0]*2,"鬼星开穴"),
    ]
    shui_damage = [
        (Judge(res,Skill(res).ding,["鬼遁","祝祷"]).d()[0]*4,"往者定"),
        (Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白",]).d()[0]*2,"天斗旋"),
        (Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白"]).d()[0]*8,"天斗旋"),
        (Judge(res,Skill(res).huo,["鬼遁","祝祷","荧入白",]).d()[0]*9,"卦象·火离"),
        (Judge(res,Skill(res).huo,["祝祷","荧入白",]).d()[0]*9,"卦象·火离"),
        (Judge(res,Skill(res).dou,["祝祷","荧入白"]).d()[0]*4,"天斗旋"),
        (Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d()[0]*32,"灵器"),
        (Judge(res,Skill(res).ling,["祝祷","荧入白"]).d()[0]*26,"灵器"),
        (Judge(res,Skill(res).po,["鬼遁","祝祷","荧入白"]).d()[0]*4,"破"),
        (Judge(res,Skill(res).po,["祝祷","荧入白"]).d()[0]*3,"破"),
        (Judge(res,Skill(res).po,["鬼遁","祝祷"]).d()[0]*2,"破"),
        (Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d()[0]*48,"杀星在尾"),
        (Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白"]).d()[0]*18,"兵主逆"),
        (Judge(res,Skill(res).bing,["祝祷","荧入白"]).d()[0]*18,"兵主逆"),
        (Judge(res,Skill(res).bing,["鬼遁","祝祷"]).d()[0]*6,"兵主逆"),
        (Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白"]).d()[0]*8,"三星临"),
        (Judge(res,Skill(res).lin,["祝祷","荧入白"]).d()[0]*4,"三星临"),
        (Judge(res,Skill(res).kai,["祝祷","荧入白"]).d()[0]*2,"鬼星开穴"),
    ]
    huo_damage = [
        (Judge(res,Skill(res).ding,["鬼遁","祝祷"]).d()[0]*4,"往者定"),
        (Judge(res,Skill(res).huo,["鬼遁","祝祷","荧入白",]).d()[0]*18,"卦象·火离"),
        (Judge(res,Skill(res).huo,["祝祷","荧入白",]).d()[0]*18,"卦象·火离"),
        (Judge(res,Skill(res).huo,["鬼遁","祝祷","荧入白",]).d()[0]*18,"卦象·火离"),
        (Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白",]).d()[0]*2,"天斗旋"),
        (Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白"]).d()[0]*8,"天斗旋"),
        (Judge(res,Skill(res).dou,["祝祷","荧入白"]).d()[0]*4,"天斗旋"),
        (Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d()[0]*32,"灵器"),
        (Judge(res,Skill(res).ling,["祝祷","荧入白"]).d()[0]*26,"灵器"),
        (Judge(res,Skill(res).po,["鬼遁","祝祷","荧入白"]).d()[0]*4,"破"),
        (Judge(res,Skill(res).po,["祝祷","荧入白"]).d()[0]*3,"破"),
        (Judge(res,Skill(res).po,["鬼遁","祝祷"]).d()[0]*2,"破"),
        (Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d()[0]*48,"杀星在尾"),
        (Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白"]).d()[0]*18,"兵主逆"),
        (Judge(res,Skill(res).bing,["祝祷","荧入白"]).d()[0]*18,"兵主逆"),
        (Judge(res,Skill(res).bing,["鬼遁","祝祷"]).d()[0]*6,"兵主逆"),
        (Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白"]).d()[0]*8,"三星临"),
        (Judge(res,Skill(res).lin,["祝祷","荧入白"]).d()[0]*4,"三星临"),
        (Judge(res,Skill(res).kai,["祝祷","荧入白"]).d()[0]*2,"鬼星开穴"),
    ]
    acc = int(res["jiasu"])
    if acc > 43:
        shan_damage.append((Judge(res,Skill(res).dou,["祝祷","荧入白","鬼遁"]).d()[0]*2,"天斗旋"))
        shui_damage.append((Judge(res,Skill(res).dou,["祝祷","荧入白","鬼遁"]).d()[0]*2,"天斗旋"))
        huo_damage.append((Judge(res,Skill(res).dou,["祝祷","荧入白","鬼遁"]).d()[0]*2,"天斗旋"))
        if acc >1928:
            shan_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
            shui_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
            huo_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
            if acc > 2956:
                shan_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                shui_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                huo_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                if acc > 4027:
                    shan_damage = shan_damage[0:-1]
                    shui_damage = shui_damage[0:-1]
                    huo_damage = huo_damage[0:-1]
                    shan_damage.append((Judge(res,Skill(res).bing,["祝祷","荧入白","鬼遁"]).d()[0]*6,"兵主逆"))
                    shui_damage.append((Judge(res,Skill(res).bing,["祝祷","荧入白","鬼遁"]).d()[0]*6,"兵主逆"))
                    huo_damage.append((Judge(res,Skill(res).bing,["祝祷","荧入白","鬼遁"]).d()[0]*6,"兵主逆"))
                    if acc > 6298:
                        shan_damage.append((Judge(res,Skill(res).dou,["祝祷","荧入白","鬼遁"]).d()[0]*2,"天斗旋"))
                        shui_damage.append((Judge(res,Skill(res).dou,["祝祷","荧入白","鬼遁"]).d()[0]*2,"天斗旋"))
                        huo_damage.append((Judge(res,Skill(res).dou,["祝祷","荧入白","鬼遁"]).d()[0]*2,"天斗旋"))
                        shan_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                        shui_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                        huo_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                        if acc > 8782:
                            shan_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                            shui_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                            huo_damage.append((Judge(res,Skill(res).lin,["祝祷","荧入白","鬼遁"]).d()[0]*2,"三星临"))
                            if acc > 10153:
                                shan_damage = shan_damage[0:-1]
                                shui_damage = shui_damage[0:-1]
                                huo_damage = huo_damage[0:-1]
                                shan_damage.append((Judge(res,Skill(res).bing,["祝祷","荧入白","鬼遁"]).d()[0]*6,"兵主逆"))
                                shui_damage.append((Judge(res,Skill(res).bing,["祝祷","荧入白","鬼遁"]).d()[0]*6,"兵主逆"))
                                huo_damage.append((Judge(res,Skill(res).bing,["祝祷","荧入白","鬼遁"]).d()[0]*6,"兵主逆"))


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
        "卦象·火离":0,
    }
    huo_times = int(res["huo_percentage"])/10
    shan_times = int(res["shan_percentage"])/10
    shui_times = int(res["shui_percentage"])/10
    for k in range(0,10):
        if shan_times > 0 :
            shan_times -= 1
            for i in shan_damage:
                dam += i[0]
                dam_dic[i[1]] += i[0]
        if huo_times > 0 :
            huo_times -= 1
            for i in huo_damage:
                dam += i[0]
                dam_dic[i[1]] += i[0]
        if shui_times > 0 :
            shui_times -= 1
            for i in shui_damage:
                dam += i[0]
                dam_dic[i[1]] += i[0]
    dps = int(dam/900)
    damage_ding = str(round(100*dam_dic["往者定"]/dam,2))+"%"
    damage_dou = str(round(100*dam_dic["天斗旋"]/dam,2))+"%"
    damage_ling = str(round(100*dam_dic["灵器"]/dam,2))+"%"
    damage_po = str(round(100*dam_dic["破"]/dam,2))+"%"
    damage_sha = str(round(100*dam_dic["杀星在尾"]/dam,2))+"%"
    damage_bing = str(round(100*dam_dic["兵主逆"]/dam,2))+"%"
    damage_lin = str(round(100*dam_dic["三星临"]/dam,2))+"%"
    damage_kai = str(round(100*dam_dic["鬼星开穴"]/dam,2))+"%"
    damage_huo = str(round(100*dam_dic["卦象·火离"]/dam,2))+"%"
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
                        },
                "code": 20000,
            }
    return JsonResponse(msg, safe=False)


