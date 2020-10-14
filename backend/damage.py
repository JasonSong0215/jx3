"""
已弃用
"""
# shan_damage = [
#         Judge(res,Skill(res).ding,["鬼遁","祝祷"]).d(),
#         Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白",]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).po,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).po,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).sha,["鬼遁","祝祷","荧入白"]).d(),
#         #第一个兵斗临
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         #第二个兵斗临
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         #第三个兵斗临
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白",]).d(),
#         Judge(res,Skill(res).ling,["鬼遁","祝祷","荧入白"]).d(),
#         #第二波起卦
#         Judge(res,Skill(res).ding,["鬼遁","祝祷",]).d(),
#         Judge(res,Skill(res).po,["祝祷","荧入白"]).d(),
#         # 第四个兵斗临
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).dou,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).lin,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         # 第五个兵斗临
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).dou,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).lin,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         # 第六个兵斗临 准备爆灯
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).bing,["祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).ling,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).kai,["祝祷","荧入白"]).d(),
#         Judge(res,Skill(res).dou,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).lin,["鬼遁","祝祷","荧入白","重山"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷"]).d(),
#         Judge(res,Skill(res).bing,["鬼遁","祝祷"]).d(),
#         Judge(res,Skill(res).po,["鬼遁","祝祷"]).d(),
#                    ]



# class Damage:
#     def __init__(self,res):
#         self.current_skill = []
#         self.current_sing_time = [0]
#         self.skill_cd = [0,0,0,0,0,0,0,0] # 斗 兵 杀星 定 起卦 魂阵 临 炸灯
#         self.skill_list = []
#         self.qi_delay = [0]
#         self.buff = ["祝祷","鬼遁"]
#         self.buff_time = [90,25]
#         self.guaxiang = "水坎"
#         self.bing = Skill(res).bing
#         self.dou = Skill(res).dou
#         self.lin = Skill(res).lin
#         self.kai = Skill(res).kai
#         self.po = Skill(res).po
#         self.huo = Skill(res).huo
#         self.ling = Skill(res).ling
#         self.sha = Skill(res).sha
#         self.ding = Skill(res).ding
#         self.res = res
#         if self.res["qixue_9"] == "5":
#             self.dou_chongneng = 3
#         else:
#             self.dou_chongneng = 1
#
#     """
#     有火卦的时候什么时候爆灯
#     杀星什么时候爆
#     """
#
#     def qi_gua(self):
#         if "兵主逆" not in self.current_skill:
#             if "天斗旋" not in self.current_skill:
#                 if self.skill_cd[4] == 0:
#                     if self.qi_delay[0] <= 0:
#                         self.qi_delay[0] = 2
#                         self.skill_cd[4] = 20
#                         # print(self.skill_cd)
#     def qi_men(self):
#         if "兵主逆" not in self.current_skill:
#             if "天斗旋" not in self.current_skill:
#                 if "魂阵" in self.buff:
#                     pass
#                 else:
#                     if self.skill_cd[2] < Judge(self.res,Skill(self.res).ding,self.buff).d()[2][6]:
#                         self.buff.append("魂阵")
#                         self.buff_time.append(40)
#     def kai_xue(self):
#         if "兵主逆" not in self.current_skill:
#             if "天斗旋" not in self.current_skill:
#                 if "鬼遁" in self.buff:
#                     pass
#                 else:
#                     locate = self.buff.index("魂阵")
#                     if self.buff_time[locate] < 3.0625:
#                         self.buff.append("鬼遁")
#                         self.buff_time.append(30)
#     def skill_ding(self):
#         if self.current_skill == []:
#             if self.skill_cd[3] == 0:
#                 current_buff = copy.copy(self.buff)
#                 ding = Judge(self.res,Skill(self.res).ding,current_buff).d()
#                 self.skill_list.append((ding[1],ding[0],current_buff))
#                 self.current_skill.append(ding[2][8])
#                 self.current_sing_time[0]= ding[2][6]
#                 self.skill_cd[3] = ding[2][7]
#
#     def skill_sha(self):
#         if self.current_skill == []:
#             if self.skill_cd[2] == 0:
#                 current_buff = copy.copy(self.buff)
#                 if "山艮" in current_buff:
#                     current_buff.remove("山艮") #杀星不吃山艮
#                 sha = Judge(self.res,Skill(self.res).sha,current_buff).d()
#                 for i in range(0,12):
#                     self.skill_list.append((sha[1],sha[0],current_buff))
#                 self.current_skill.append(sha[2][8])
#                 self.current_sing_time[0]= sha[2][6]
#                 self.skill_cd[2] = sha[2][7]
#     def skill_bing(self):
#         if self.current_skill == []:
#             if self.skill_cd[1] == 0:
#                 current_buff = copy.copy(self.buff)
#                 bing = Judge(self.res,Skill(self.res).bing,current_buff).d()
#                 for i in range(0,3):
#                     self.skill_list.append((bing[1],bing[0],current_buff))
#                     if "魂阵" in current_buff:
#                         if "山艮" in current_buff:
#                             cur_buff = copy.copy(current_buff)
#                             cur_buff.remove("山艮")
#                             ling = Judge(self.res,Skill(self.res).ling,cur_buff).d()
#                             self.skill_list.append((ling[1],ling[0],cur_buff))
#                 self.current_skill.append(bing[2][8])
#                 self.current_sing_time[0]= bing[2][6]*3
#                 # print(self.current_sing_time)
#                 self.skill_cd[1] = bing[2][7]
#     def skill_dou(self):
#         if self.current_skill == []:
#             if self.dou_chongneng > 0:
#                 self.dou_chongneng -= 1
#                 current_buff = copy.copy(self.buff)
#                 dou = Judge(self.res,Skill(self.res).dou,current_buff).d()
#                 if "魂阵" in current_buff:
#                     if "山艮" in current_buff:
#                         cur_buff = copy.copy(current_buff)
#                         cur_buff.remove("山艮")
#                         ling = Judge(self.res,Skill(self.res).ling,cur_buff).d()
#                         self.skill_list.append((ling[1],ling[0],cur_buff))
#                 self.skill_list.append((dou[1],dou[0],current_buff))
#                 self.current_skill.append(dou[2][8])
#                 self.current_sing_time[0]= dou[2][6]
#                 # print(dou[2][7])
#                 if self.res["qixue_9"] == "5":
#                     if self.dou_chongneng == 2:
#                         self.skill_cd[0] = dou[2][7]
#                 else:
#                     self.skill_cd[0] = dou[2][7]
#                 # print(self.skill_cd)
#     def skill_lin(self):
#         if self.current_skill == []:
#             if self.skill_cd[6] == 0:
#                 current_buff = copy.copy(self.buff)
#                 lin = Judge(self.res,Skill(self.res).lin,current_buff).d()
#                 self.skill_list.append((lin[1],lin[0],current_buff))
#                 if "魂阵" in current_buff:
#                         if "山艮" in current_buff:
#                             cur_buff = copy.copy(current_buff)
#                             cur_buff.remove("山艮")
#                             ling = Judge(self.res,Skill(self.res).ling,cur_buff).d()
#                             self.skill_list.append((ling[1],ling[0],cur_buff))
#                 self.current_skill.append(lin[2][8])
#                 self.current_sing_time[0]= lin[2][6]
#                 self.skill_cd[6] = lin[2][7]
#
#     def gua_pass(self): #卦象生效倒计时
#         gua_list = ["火离","山艮","水坎"]
#         gua = random.choice(gua_list)
#         if self.qi_delay[0] == 0 :
#             self.buff.append(gua)
#             self.buff_time.append(19)
#             self.buff.append("荧入白")
#             self.buff_time.append(19)
#             self.qi_delay[0] -= 0.0625
#             # print(self.qi_delay)
#         else:
#             # print(self.qi_delay)
#             self.qi_delay[0] -= 0.0625
#     def bian_gua(self): #变卦
#         if "水坎" in self.buff: # 水卦直接变
#             for i in range(0,len(self.buff)):
#                 if self.buff[i] == "水坎":
#                     gua_list_shui = ["火离","山艮"]
#                     self.buff[i] == random.choice(gua_list_shui)
#         elif "火离" in self.buff: # 判断什么时候爆灯 看是否需要变卦
#             for i in range(0,len(self.buff)):
#                 if self.buff[i] == "火离":
#                     gua_list_shui = ["水坎","山艮"]
#                     self.buff[i] == random.choice(gua_list_shui)
#
#     def buff_past(self): #buff消失倒计时
#         buff_del = []
#         for i in range(0,len(self.buff_time)):
#             self.buff_time[i] -= 0.0625
#             if self.buff_time[i] == 0:
#                 buff_del.append(i)
#         m = 0
#         # 清理消失的BUFF和BUFF_TIME
#         for i in buff_del:
#             del self.buff[i+m]
#             del self.buff_time[i+m]
#             m -= 1
#     def sing_past(self): #吟唱倒计时
#         if self.current_sing_time[0] >0:
#             self.current_sing_time[0] -= 0.0625
#             for i in range(0,len(self.skill_cd)):
#                 if self.skill_cd[i] <0.0625:
#                     self.skill_cd[i] = 0
#                     print(i,self.skill_cd[i],self.dou_chongneng)
#                     if i == 0:
#                         if self.res["qixue_9"] == "5":
#                             if self.dou_chongneng > 2:
#                                 self.dou_chongneng =3
#                             else:
#                                 self.dou_chongneng += 1
#                                 self.skill_cd[0] = 4
#                 else:
#                     self.skill_cd[i] -= 0.0625
#             if self.current_sing_time[0] == 0:
#                 self.current_skill = []
#     def time_pass(self):
#         self.buff_past()
#         self.sing_past()
#         self.gua_pass()
#
#
#     def start(self):
#         # t = 90
#         t = 12
#         for i in numpy.arange(0,t,0.0625):
#             self.qi_gua()
#             self.qi_men()
#             self.skill_ding()
#             self.skill_sha()
#
#             self.skill_dou()
#             self.skill_bing()
#             self.skill_lin()
#             print(i,"正在读条：",self.current_skill,self.current_sing_time[0])
#             # print("buff：",self.buff)
#             # print("buff时间：",self.buff_time)
#             # print("技能CD",self.skill_cd)
#             self.time_past()
#         print(self.skill_list)