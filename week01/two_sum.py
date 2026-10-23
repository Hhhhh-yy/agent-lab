# 两数之和：在数组里找两个数，加起来等于目标值，返回它们的下标
# 套路：用字典记下「见过的数字 → 下标」，一次遍历就能凑齐

# 定义函数：numbers 是数字列表，target 是要凑出来的和
def two_sum(numbers, target):
    # 建一个空字典：存「数字 → 它的下标」，查一次是瞬间的事
    seen_index = {}

    # --- 上一步拿到一个空字典 → 这一块边遍历边往字典里存见过的数字
    # 用 enumerate 同时拿到下标和数字，省得自己数
    for position, current_number in enumerate(numbers):
        # 算「还差多少」：目标和减去当前数字，就是我要找的搭档
        need_number = target - current_number
        # 去字典里查搭档：查到了说明两个数凑齐了
        if need_number in seen_index:
            # 返回两个下标，先出现的搭档放前面
            return [seen_index[need_number], position]
        # 没查到就把当前数字记下来，留给后面的数字当搭档
        seen_index[current_number] = position

    # 循环走完都没返回，说明没有解，给个空列表
    return []


# --- 上一步拿到了能算下标的方法 → 这一块用具体数据验证它
# 测试数据：数字列表，随便改这里
test_numbers = [2, 7, 11, 15]
# 目标和：看这个数能不能被其中两个数凑出来
test_target = 9

# 调用函数，把返回的下标存起来
answer = two_sum(test_numbers, test_target)
# 打印输入，方便自己对照
print("数组:", test_numbers, "目标:", test_target)
# 打印答案，第一次应该看到 [0, 1]
print("答案下标:", answer)