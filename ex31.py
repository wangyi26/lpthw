print("""门
你想通过门 #1 或门 #2？""")

门 = input(">")

if 门 == "1":
   print("这里有一个巨熊在这里吃一个奶酪蛋糕。")
   print("你怎么做？")
   print("1.带走蛋糕。")
   print("2.朝熊叫。")

   熊 = input(">")

   if 熊 == "1":
      print("这个熊吃掉了你的脸蛋。做得好！")
   elif 熊 == "2":
      print("这个熊吃掉了你的腿。做得好！")
   else:
      print(f"好吧，做{熊}可能更好。")
      print("熊跑远了。")

elif 门 == "2":
   print("你盯着Cthulhu的视网膜的无尽深渊。")
   print("1.蓝莓。")
   print("2.黄夹克衫夹子。")
   print("3.了解左轮手枪的旋律。")

   精神病 = (">")

   if 精神病 == "1" or 精神病 == "2":
      print("你的身体幸存于果冻的头脑。")
      print("干得好！")
   else:
      print("精神错乱会把你的眼睛变成一团泥。")
      print("做得好！")

else:
    print("你绊倒在刀子上死了。做得好！")                  