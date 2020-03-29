temp=input("猜错啦！请重新输入新的数字：")
guess=int(temp)
while guess != 9:
     if guess == 9: #复习无限循环语句
          print("恭喜你，猜中啦！")
          print("猜中也没有奖励，哈哈哈哈！")
     else:
         if guess > 9:
              print("大了！大了！")
         else:
              print("小了！小了！")
