# 1.  在第一行 显示一个 “A" 的字符，然后下一行 ，往右边12 个空格，显示 ”B“ 字符

# print("A............")
# print("             B")

# 2. 播放中文歌曲
import pygame

#初始化调音器
pygame.mixer.init()

#加载音乐文件
pygame.mixer.music.load("1.mp3")
#播放音乐文件
pygame.mixer.music.play()
# 等待播放完成
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


#3. 显示对象的信息
Gou={'name':"狗",'attribute':'动物'}
print(Gou)

