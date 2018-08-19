from sys import exit

def yu_wen():
    print("暑假要结束了，你做完语文作业了吗?")
    print("请选择'做完了'或'没有'")

    choice = input(">")
       
    if "做完了" in choice:
       print("真是个勤奋的好孩子，开学继续加油！")
       exit(0)
    if "没有" in choice:
       print("如果把所有语文作业看成10，你还剩多少作业？")
       答案 = input(">")
       shu_zi = int(答案)
       if shu_zi > 5:
             print("还有十多天还来得及。")
             exit(0)
       if shu_zi < 5:
             print("我相信你一定会不择手段的完成的")
             exit(0)
       else:
           print("请写一个数字！")
           yu_wen()

         

def shu_xue():
    print("暑假要结束了，你做完数学作业了吗?")
    print("请选择'做完了'或'没有'")

    choice = input(">")
       
    if "做完了" in choice:
       print("真是个勤奋的好孩子，开学继续加油！")
       exit(0)
    if "没有" in choice:
       print("如果把所有数学作业看成10，你还剩多少作业？")
       答案 = input(">")
       shu_zi = int(答案)
       if shu_zi > 5:
             print("还有十多天还来得及。")
             exit(0)
       if shu_zi < 5:
             print("我相信你一定会不择手段的完成的")
             exit(0)
       else:
           print("请写一个数字！")
           shu_xue()



def ying_yu():
    print("暑假要结束了，你做完英语作业了吗?")
    print("请选择'做完了'或'没有'")

    choice = input(">")
       
    if "做完了" in choice:
       print("真是个勤奋的好孩子，开学继续加油！")
       exit(0)
    if "没有" in choice:
       print("如果把所有语文作业看成10，你还剩多少作业？")
       答案 = input(">")
       shu_zi = int(答案)
       if shu_zi > 5:
             print("还有十多天还来得及。")
             exit(0)
       if shu_zi < 5:
             print("我相信你一定会不择手段的完成的")
             exit(0)
       else:
           print("请写一个数字！")
           ying_yu()
def start():
     print("进入高中，在语数外三科里，你最喜欢哪一科？")
     choice = input(">")
     if choice == "语文":
        yu_wen()
     if choice == "数学": 
        shu_xue()
     if choice == "英语":
        ying_yu()
     else:
        print("请选择'语文'或'数学'或'英语'")
        start()


                              
start()                        