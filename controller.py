import random as ran, datetime as dt

class SelectController:
    def __init__(self):
        pass
    def choiceMenu(self, list):
        self.list = list
        result = list[ran.randint(0,len(list)-1)]
        self.resultFile(result)
        return result
    def resultFile(self,result):
        date = dt.datetime.now()
        dateStr = date.strftime("%Y-%m-%d")
        with open("./result/result.txt",'a',encoding="utf-8") as f:
            f.write(f"{dateStr} : {result} \n")
