#Author:Jason Song
class Skill:
    def __init__(self,res):
        acc = int(res["jiasu"])
        #技能基础伤害，技能系数，武伤系数，伤害秘籍+套装伤害+奇穴增伤，会心秘籍+会心奇穴，会效奇穴,GCD,CD,名称]
        self.ding = [68,1.301,0,0,0,0,1.5,20,"往者定"]
        self.bing = [578,1.197453,0,0,0,0,1,5,"兵主逆"]
        self.lin = [116,1.0778,0,0,0,0,1.5,1.5,"三星临"]
        self.dou = [833,2.274,0,0,0,0,1.5,5.5,"天斗旋"]
        # self.po = [16.116,0,0,0,0,0,2,0,"破"]
        self.po = [14.504,0,0,0,0,0,2,0,"破"]
        self.sha = [290,0.93715,0,0,0,0,1.5,45,"杀星在尾"]
        self.kai = [519,3.29,0,0,0,0,0,5,"鬼星开穴"]
        self.pozhao = int(res["pozhao"])
        self.po[0] = self.po[0] * self.pozhao




        if res["qixue_11"] == "2":
            self.huo = [97,1.0414,0,0,0,0,2,0,"卦象·火离"]
            self.ling = [65,0.5205,0,0,0,0,0,0,"灵器"]
        elif res["qixue_11"] == "3":
            self.huo = [97,1.565,0,0,0,0,2,0,"卦象·火离"]
            self.ling = [0,0,0,0,0,0,0,0,"灵器"]
        else:
            self.huo = [97,1.075,0,0,0,0,2,0,"卦象·火离"]
            self.ling = [0,0,0,0,0,0,0,0,"灵器"]
        if res["ping"] == 2:
            self.ding[6] += 0.0625
            self.lin[6] += 0.0625
            self.dou[6] += 0.0625
            self.sha[6] += 0.0625
        elif res["ping"] == 3:
            self.ding[6] += 0.125
            self.lin[6] += 0.125
            self.dou[6] += 0.125
            self.sha[6] += 0.125
        elif res["ping"] == 4:
            self.ding[6] += 0.1875
            self.lin[6] += 0.1875
            self.dou[6] += 0.1875
            self.sha[6] += 0.1875




        if acc > 43:
            self.ding[6] -= 0.0625
            self.bing[6] -= 0.0625
            self.lin[6] -= 0.0625
            self.dou[6] -= 0.0625
            self.po[6] -= 0.0625
            self.huo[6] -= 0.0625
            self.sha[6] -= 0.0625
            if acc > 1457:
                self.po[6] -= 0.0625
                self.huo[6] -= 0.0625
                if acc >1928:
                    self.ding[6] -= 0.0625
                    self.lin[6] -= 0.0625
                    self.dou[6] -= 0.0625
                    self.sha[6] -= 0.0625
                    if acc > 2956:
                        self.bing[6] -= 0.0625
                        self.po[6] -= 0.0625
                        self.huo[6] -= 0.0625
                        if acc > 4027:
                            self.ding[6] -= 0.0625
                            self.lin[6] -= 0.0625
                            self.dou[6] -= 0.0625
                            self.sha[6] -= 0.0625
                            if acc > 4541:
                                self.po[6] -= 0.0625
                                self.huo[6] -= 0.0625
                                if acc > 6298:
                                    self.ding[6] -= 0.0625
                                    self.bing[6] -= 0.0625
                                    self.lin[6] -= 0.0625
                                    self.dou[6] -= 0.0625
                                    self.po[6] -= 0.0625
                                    self.huo[6] -= 0.0625
                                    self.sha[6] -= 0.0625
                                    if acc > 8140:
                                        self.po[6] -= 0.0625
                                        self.huo[6] -= 0.0625
                                        if acc > 8782:
                                            self.ding[6] -= 0.0625
                                            self.lin[6] -= 0.0625
                                            self.dou[6] -= 0.0625
                                            self.po[6] -= 0.0625
                                            self.huo[6] -= 0.0625
                                            self.sha[6] -= 0.0625
                                            if acc > 10153:
                                                self.bing[6] -= 0.0625


        # 秘籍奇穴
        if res["qixue_1"] == "1": # 正夏
            self.lin[3] += 0.1
        if res["qixue_1"] == "2": # 明心
            self.lin[4] += 0.1
            self.lin[5] += 0.1
        if res["qixue_2"] == "1":# 望旗BUFF
            self.bing[3] += 0.1
        if res["qixue_3"] == "1":# 相蚀BUFF
            self.lin[3] += 0.3
        if "伤害+5%" in res["miji_lin"]:
            self.lin[3] += 0.05
        if "伤害+4%" in res["miji_lin"]:
            self.lin[3] += 0.04
        if "伤害+3%" in res["miji_lin"]:
            self.lin[3] += 0.03
        if "会心+4%" in res["miji_lin"]:
            self.lin[4] += 0.04
        if "会心+3%" in res["miji_lin"]:
            self.lin[4] += 0.03
        if "会心+2%" in res["miji_lin"]:
            self.lin[4] += 0.02
        if "伤害+5%" in res["miji_bing"]:
            self.bing[3] += 0.05
        if "伤害+4%" in res["miji_bing"]:
            self.bing[3] += 0.04
        if "伤害+3%" in res["miji_bing"]:
            self.bing[3] += 0.03
        if "会心+4%" in res["miji_bing"]:
            self.bing[4] += 0.04
        if "会心+3%" in res["miji_bing"]:
            self.bing[4] += 0.03
        if "伤害+5%" in res["miji_dou"]:
            self.dou[3] += 0.05
        if "伤害+4%" in res["miji_dou"]:
            self.dou[3] += 0.04
        if "伤害+3%" in res["miji_dou"]:
            self.dou[3] += 0.03
        if "会心+4%" in res["miji_dou"]:
            self.dou[4] += 0.04
        if "会心+3%" in res["miji_dou"]:
            self.dou[4] += 0.03
        if "会心+2%" in res["miji_dou"]:
            self.dou[4] += 0.02
        if "伤害+5%" in res["miji_kai"]:
            self.kai[3] += 0.05
        if "伤害+4%" in res["miji_kai"]:
            self.kai[3] += 0.04
        if "会心+4%" in res["miji_kai"]:
            self.kai[4] += 0.04
        if "会心+3%" in res["miji_kai"]:
            self.kai[4] += 0.03
    def print_obj(obj):
        print(obj.__dict__)