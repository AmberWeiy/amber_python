# 任务 1：
# 在一个新的名字为 "poem.txt" 的文件里，写入以下内容：
# 今见生人，
# 一念相见，
# 无不欢喜。
with open("./poem.txt", "w", encoding = "utf_8") as f:
    f.write("今见生人，\n一念相见，\n无不欢喜。\n")

# 任务 2：
# 在上面的 "poem.txt" 文件结尾处，添加以下两句：
# 同归华台，
# 同生莲上。
with open("./poem.txt", "a", encoding = "utf_8") as f:
    f.write("同归华台，\n同生莲上。")