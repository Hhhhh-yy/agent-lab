# 字母异位词分组：字母一样、顺序不同的单词，归到同一组
# 套路：把单词的字母排好序当「指纹」，指纹相同的放一起

# 定义函数：words 是一串单词
def group_anagrams(words):
    # 建一个空字典：键是排好序的字母，值是一组同指纹的单词
    groups_by_key = {}

    # --- 上一步拿到空字典 → 这一块给每个单词算指纹并按指纹分组
    # 一个个看单词，word 是当前这个词
    for word in words:
        # 把字母排好序再拼回字符串，当这个单词的指纹
        sorted_key = "".join(sorted(word))
        # 字典里还没这个指纹，就先放一个空列表占位
        if sorted_key not in groups_by_key:
            groups_by_key[sorted_key] = []
        # 把当前单词追加到它指纹对应的那一组
        groups_by_key[sorted_key].append(word)

    # --- 上一步拿到「指纹 → 单词组」的字典 → 这一块只要每个组本身
    # 取出字典里所有的值，收成列表就是答案
    return list(groups_by_key.values())


# --- 上一步有了分组函数 → 这一块用例子看谁和谁被分到一起
# 测试数据：eat/tea/ate 同组，tan/nat 同组，bat 单独
test_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 调用函数，拿到分组结果
answer = group_anagrams(test_words)
# 打印原始列表，方便对照
print("单词列表:", test_words)
# 打印分组结果，同组单词会挤在同一个方括号里
print("分组结果:", answer)