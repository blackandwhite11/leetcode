# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
# 示例:
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

# 递归
# def add(num):
#     if num >= 0 and num < 10:
#         return num
#     else:
#         sum = 0
#         # 注意 str 是可迭代对象
#         for i in str(num):
#             sum += int(i)
#         return add(sum)

# 循环
# def add(num):
#     while num > 9:
#         res = 0
#         while num:
#             res += num % 10
#             num //= 10
#         num = res
#     return num

# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

def add(num):
    if num == 0:
        return 0
    return num % 9


if __name__ == "__main__":
    num = 38
    print(add(num))