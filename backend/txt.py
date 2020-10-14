#Author:Jason Song
"""
所有技能只吃山卦的快照，荧入白/鬼遁 都是即时计算的

火卦不能挂队友了，只能刷新DOT，最大可能延长DOT时间

变卦炸灯需要消耗星运，self.xingyun>=self.skills["XXXXX"]["消耗"]
1。如果火卦了，并且18s内可以炸灯，等 这样只损失鬼遁，火离可以尽可能多的烫

PLAN A 火卦 火离 -18s- 炸灯 起卦 水变卦 火山不变 火离等卦象快结束了打出去
PLAN B 正常打


"""
"""
技能

1.判断充能是否好了
2.判断是否在GCD sing当中
3. self.skills["XXXXX"]["剩余充能"] -= 1                                  剩余充能
4. self.skills["XXXXX"]["cold_down"] = self.skills["XXXXX"]["CD"]
5. buff = copy.copy(self.current_buff)
6.  damage = [0,]
    damage = Judge(self.res,Skill(self.res).XXXXXX,buff).d()
7. self.log("XXXXX",damage,buff,t)                                       记录日志
8 self.xingyun -= self.skills["XXXXX"]["消耗"]                           星运消耗



"""
