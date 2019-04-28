# 对于非负整数X而言，X的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果X = 1231，那么其数组形式为[1, 2, 3, 1]。
# 给定非负整数X的数组形式A，返回整数X + K的数组形式。
# 示例
# 输入：A = [1, 2, 0, 0], K = 34
# 输出：[1, 2, 3, 4]
# 解释：1200 + 34 = 1234
# 提示：
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# 如果A.length > 1，那么A[0] != 0


def li_sum(a,k):
    n = ''
    for i in a:
        n += str(i)
    sum = int(n) + k
    li = []
    for i in str(sum):
        li.append(int(i))
    return li


def li_sum2(a,k):
    # 123 + 912，我们把它表示成[1, 2, 3 + 912]。然后，我们计算3 + 912 = 915。5留在当前这一位，将910 / 10 = 91以进位的形式加入下一位。
    # 然后，我们再重复这个过程，计算[1, 2 + 91, 5]。我们得到93，3留在当前位，将90 / 10 = 9以进位的形式加入下一位。
    # 继而又得到[1 + 9, 3, 5]，重复这个过程之后，最终得到结果[1, 0, 3, 5]。
    li = []
    lenght = len(a)
    while lenght > 0 or k > 0:
        if lenght > 0:
            k += a[lenght-1]
            lenght -= 1
        li.append(k % 10)
        k //= 10
    li.reverse()
    return li


if __name__ == "__main__":
    a = [0]
    k = 34
    print(li_sum2(a, k))
