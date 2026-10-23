# 最长连续序列：在乱序数字里找「数字连续」的最长一段有多长
# 套路：先扔进集合，只从「没有前一个数」的起点开始往右数

# 小工具：从某个起点往后数，看到底能连多长
def count_run_from(start_number, number_set):
    # 起点自己算一个，所以长度从 1 开始
    run_length = 1
    # 一直往后试 +1、+2，只要还在集合里就继续
    while start_number + run_length in number_set:
        # 下一个数也在，长度加一，接着试再下一个
        run_length += 1
    # 数到头了，把这一段的总长度还回去
    return run_length


# 定义函数：numbers 是一堆乱序整数
def longest_consecutive(numbers):
    # 先放进集合：自动去重，而且查「在不在」非常快
    number_set = set(numbers)
    # 用一个变量记住目前最长的一段，先设 0
    longest_length = 0

    # --- 上一步拿到能瞬间查数的集合 → 这一块只从每段的起点开始数
    # 逐个看集合里的数字，current_number 是当前这个数
    for current_number in number_set:
        # 前一个数也在集合里，说明它不是起点，跳过免得重复数
        if current_number - 1 in number_set:
            continue
        # 是起点就交给小工具去数，拿到这一段有多长
        run_length = count_run_from(current_number, number_set)
        # 和目前最长的比，谁大留谁
        longest_length = max(longest_length, run_length)

    # 全部数字看完，返回最长的那一段长度
    return longest_length


# --- 上一步有了算法 → 这一块用一组乱序数字验证答案
# 测试数据：1、2、3、4 连着，长度应该是 4
test_numbers = [100, 4, 200, 1, 3, 2]
# 调用函数，拿到最长连续长度
answer = longest_consecutive(test_numbers)
# 打印输入，方便自己心算
print("数字列表:", test_numbers)
# 打印答案，第一次应该看到 4
print("最长连续长度:", answer)