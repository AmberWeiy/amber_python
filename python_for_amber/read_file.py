#close关闭
# f= open("./data.txt", "r", encoding = "utf_8")
# content = f.read()
# print(content)
# f.close()

#with关闭
# with open("./data.txt", "r", encoding = "utf_8") as f:
#   content = f.read()
#   print(content)

#readline函数
# with open("./data.txt", "r", encoding = "utf_8") as f:
#   print(f.readline())
#   print(f.readline())

#readlines函数
# with open("./data.txt", "r", encoding = "utf_8") as f:
#   print(f.readlines())


with open("./data.txt", "r", encoding = "utf_8") as f:
  lines = f.readlines()
  for line in lines:
      print(line)