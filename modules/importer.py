# 匯入單字檔：把 words/ 的單字檔讀進來，做成卡片
count = 0
with open("words/大考中心_第1級.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("#"):
            continue
        count = count + 1
        parts = line.strip().split("\t")
        word = parts[0]
        back = parts[1]
        print(back)
print(count)









