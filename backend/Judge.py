#Author:Jason Song
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
class Judge:
    def __init__(self,res,skill,buff):
        self.skill_name = skill[8]
        # print(self.skill_name,buff)
        self.weapon = 0 # 武伤，衍天没有所以直接0
        self.skill_basic_damage = skill[0] # 技能基础伤害
        self.skill_damage_per = skill[1] # 技能伤害系数
        self.skill_weapon_damage = skill[2] # 技能武器伤害系数
        self.jichugongji = int(res["jichugongji"]) # 人物初始基础攻击
        self.huixin = float(res["huixin"])*0.01 + skill[4] # 人物基础会心+技能奇穴会心
        self.huixiao = float(res["huixiao"])*0.01 + skill[5] # 人物基础会效+技能奇穴会效
        self.jiasu = int(res["jiasu"])
        self.wushuang = float(res["wushuang"])
        self.yuanqi = int(res["yuanqi"])
        self.pofang = float(res["pofang"])
        self.pozhao = int(res["pozhao"])
        self.limit_reduce_defence = 0 #固定减防御
        self.reduce_defence = 0
        self.target = res["target"] # 目标等级 1-110级，2-111级，3-112级，4-113级，5-114级
        self.skill = skill

        # 战斗BUFF+阵眼+小吃小药 带来的额外收益
        self.ex_gongji = 0
        self.ex_pofang = 0
        self.ex_huixin = 0
        self.ex_huixiao = 0

        self.zengshang = 1
        self.zengshang += skill[3]




        # 这里处理填数值时选择了神元奇穴但是面板没实际加成上的情况
        if res["shenyuan_isinclude"] is False and res["qixue_8"] == "1":
            self.huixin += self.yuanqi*0.1*0.42/dic["huixin"]
            self.pofang += self.yuanqi*0.1*0.3/dic["pofang"]
            self.jichugongji += int(self.yuanqi*0.1*0.18)
            self.yuanqi = int(self.yuanqi*1.1)
        if "梅花盾" in res["buff"]:
            self.reduce_defence += 0.15 #无视百分比防御
        if "清涓" in res["buff"]:
            self.ex_pofang += float(0.09765*self.pofang) #基础破防
        if "破苍穹" in res["buff"]:
            self.ex_huixin += 0.05
            self.ex_huixiao += 0.10
        if "弘法" in res["buff"]:
            self.ex_gongji += int(0.14928*self.jichugongji)
        if "分澜" in res["buff"]:
            self.ex_gongji += int(0.14928*self.jichugongji)
        if "荧入白" in buff:
            if  res["qixue_10"] == "1":
                self.reduce_defence += 0.5 #无视百分比防御
        if "鬼遁" in buff: # 判断buff是否存在
            if res["qixue_6"] == "1": # 判断是否点奇穴
                self.ex_gongji += int(0.14928*self.jichugongji)

        #阵眼效果
        if res["zhenyan"] == "2": #花间阵
            # 基础攻击提高5 % int(4.976 %)
            # 基础破防提高 int(0.29297)
            self.ex_gongji += int(0.04976*self.jichugongji)
            self.ex_pofang += float(0.29297*self.pofang)
        if res["zhenyan"] == "3": #气纯阵
            self.wushuang += 0.0195
            self.ex_huixin += 0.08
            self.ex_huixiao += 0.15
        if res["zhenyan"] == "4": #大师阵
            self.wushuang += 0.0195
            self.ex_gongji += int(0.14928*self.jichugongji)
            self.ex_pofang += float(0.09765*self.pofang)
        if res["zhenyan"] == "5": # 田螺阵
            self.ex_gongji += int(0.04976 * self.jichugongji)
            self.reduce_defence += 0.05  # 无视百分比防御
            self.ex_huixin += 0.05
            self.ex_huixiao += 0.15
        if res["zhenyan"] == "6": #毒经阵
            self.ex_gongji += int(0.04976 * self.jichugongji)
            self.ex_huixin += 0.03
            self.ex_huixiao += 0.10
            self.ex_pofang += float(0.09765*self.pofang)
        if res["zhenyan"] == "7": #衍天阵-自己阵
            self.wushuang += 0.0195
            self.ex_gongji += int(0.04976 * self.jichugongji)
            self.ex_gongji += int(0.02488 * self.jichugongji)
            self.ex_huixiao += 0.10
            self.zengshang += 0.025
        if res["zhenyan"] == "8": #衍天阵-同门
            self.wushuang += 0.0195
            self.ex_gongji += int(0.04976 * self.jichugongji)
            self.ex_huixiao += 0.10
            self.zengshang += 0.025


        # 处理整体技能增伤
        if "祝祷" in buff:
            if res["qixue_7"] == "1":
                self.zengshang += 0.1
        if "山艮" in buff:
            if res["qixue_4"] == "1":
                if self.skill_name in ["兵主逆","天斗旋","三星临",]: # 重山只加成九字诀
                    self.zengshang = self.zengshang * 1.15
            else:
                if self.skill_name in ["兵主逆","天斗旋","三星临",]: # 重山只加成九字诀
                    self.zengshang = self.zengshang * 1.05


        self.fin_gongji = self.jichugongji+int(dic["xinfa_gongji"]*self.yuanqi)+int(self.ex_gongji)  # 这边要加上元气的额外攻击和BUFF提供的攻击
        self.fin_pofang = self.pofang+self.ex_pofang
        self.fin_yuanqi = self.yuanqi
        self.fin_huixin = self.huixin+self.ex_huixin
        self.fin_huixiao = self.huixiao+self.ex_huixiao
        self.fin_jiasu = self.jiasu
        self.fin_wushuang = self.wushuang


    #防御减伤计算,limit_reduce_defence是固定减防御，reduce_defence是无视百分比防御
    def guo_defence(self,limit_reduce_defence,reduce_defence):
        tar_defence_level_111 = (def_dic["111"][0]-limit_reduce_defence)*(1-reduce_defence)
        tar_defence_level_112 = (def_dic["112"][0]-limit_reduce_defence)*(1-reduce_defence)
        tar_defence_level_113 = (def_dic["113"][0]-limit_reduce_defence)*(1-reduce_defence)
        tar_defence_level_114 = (def_dic["114"][0]-limit_reduce_defence)*(1-reduce_defence)
        def_111 = int(tar_defence_level_111*1024/(tar_defence_level_111+def_dic["111"][1]))
        def_112 = int(tar_defence_level_112*1024/(tar_defence_level_112+def_dic["112"][1]))
        def_113 = int(tar_defence_level_113*1024/(tar_defence_level_113+def_dic["113"][1]))
        def_114 = int(tar_defence_level_114*1024/(tar_defence_level_114+def_dic["114"][1]))
        res = [def_111,def_112,def_113,def_114]
        return res

    #计算郭氏破防值
    def guo_pofang(self,fin_pofang):
        pofang_value = int(fin_pofang*0.01*dic["pofang"])
        guo_pf = int(pofang_value*1024/dic["pofang"])
        return guo_pf
    # 原始伤害
    def damage_ori(self):
        damage_ori = int(self.skill_basic_damage) + int(float(self.fin_gongji)*self.skill_damage_per)+int(self.weapon*self.skill_weapon_damage)
        return damage_ori
    # 计算伤害
    def d(self):
        guo_pf = self.guo_pofang(self.fin_pofang)
        guo_fy = self.guo_defence(self.limit_reduce_defence,self.reduce_defence)[int(self.target)-2]
        Y = 1024+guo_pf-int((1024+guo_pf)*guo_fy/1024)
        damage_basic = int(self.damage_ori()*Y/1024) # 基准伤害(破防伤害)
        # print("最终无双",1+self.fin_wushuang*0.01)
        damage_basic_wushuang = damage_basic*(1+self.fin_wushuang*0.01) #无双加成后的伤害
        # 计算会心伤害
        # 郭氏会效值
        guo_huixiao = int((self.fin_huixiao-1.75)*1024)
        damage_basic_wushuang_huixin = int(damage_basic_wushuang*1.75)+int(damage_basic_wushuang * guo_huixiao/1024)
        damage_final = ((1-self.fin_huixin)*damage_basic_wushuang+self.fin_huixin*damage_basic_wushuang_huixin)*self.zengshang
        return damage_final,self.skill_name,self.skill
    def t(self):
        guo_pf = self.guo_pofang(self.fin_pofang)
        guo_fy = self.guo_defence(self.limit_reduce_defence,self.reduce_defence)[int(self.target)-2]
        Y = 1024+guo_pf-int((1024+guo_pf)*guo_fy/1024)
        damage_basic = int(self.damage_ori()*Y/1024) # 基准伤害(破防伤害)
        # print("最终无双",1+self.fin_wushuang*0.01)

        damage_basic_wushuang = damage_basic*(1+self.fin_wushuang*0.01)*self.zengshang #无双加成后的伤害
        # 计算会心伤害
        # 郭氏会效值
        guo_huixiao = int((self.huixiao-1.75)*1024)
        # print("郭氏会效值",guo_huixiao)
        damage_basic_wushuang_huixin = int(damage_basic_wushuang*1.75)+int(damage_basic_wushuang * guo_huixiao/1024)*self.zengshang
        damage_final = (1-self.huixin)*damage_basic_wushuang+self.huixin*damage_basic_wushuang_huixin
        # print("普通命中",damage_basic_wushuang*self.zengshang,self.zengshang)
        # print(damage_basic_wushuang_huixin)
        # print("伤害预期",damage_final)
        # if self.skill_name == "三星临":
        #     print(self.fin_gongji,self.fin_pofang,self.yuanqi,self.wushuang,)
        #     print(damage_basic_wushuang,self.zengshang)
        return damage_basic_wushuang,damage_basic_wushuang_huixin
    def print_obj(obj):
        print(obj.__dict__)