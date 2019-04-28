# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 注意：
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。


def str_add2(num1, num2):
    nu1 = 0
    nu2 = 0
    for i in num1:
        nu1 = nu1*10 + ord(i) - ord('0')
    for i in num2:
        nu2 = nu2*10 + ord(i) - ord('0')
    return str(nu1 + nu2)


if __name__ == "__main__":
    nu1 = '98'
    nu2 = '9'
    print(str_add2(nu1,nu2))



