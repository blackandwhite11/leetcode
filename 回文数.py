# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 示例 1:
# 输入: 121
# 输出: true
# 示例 2:
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。


def solution(x):
    # 反转数字后判断
    # if x < 0:
    #     return False
    # if x == 0:
    #     return True
    # if x%10 == 0:
    #     return False
    # rev_num = ''
    # t = x
    # while t:
    #     tem = str(t % 10)
    #     rev_num += tem
    #     t = t // 10
    # if x == int(rev_num):
    #     return True
    # else:
    #     return False

    # 反转一半数字
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev_num = 0
        while rev_num < x:
            rev_num = rev_num * 10 + x % 10
            x = x // 10

        if rev_num == x or (rev_num // 10 == x):
            return True
        else:
            return False


if __name__ == "__main__":
    x = 121
    print(solution(x))