# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 示例 1:
# 输入: 123
# 输出: 321
# 示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
# 注意：假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

# update 

def reverse(num):
    reverse_num = ""
    if num == 0:
        return num
    # 正数
    elif num > 0:
        while num:
            tem = num%10
            tem = str(tem)
            reverse_num += tem
            num = num//10
        reverse_num = int(reverse_num)
        if reverse_num > (pow(2, 31)-1):
            return 0
        else:
            return reverse_num
    # 负数
    else:
        num = abs(num)
        while num:
            tem = num % 10
            tem = str(tem)
            reverse_num += tem
            num = num//10
        reverse_num = 0 - int(reverse_num)
        if reverse_num < -(pow(2, 31)):
            return 0
        else:
            return reverse_num


if __name__ == "__main__":
    a = 120
    print(reverse(a))
