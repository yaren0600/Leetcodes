class Solution(object):
    def countOperations(self, num1, num2):
      
        count = 0  # kaç işlem yaptığımızı tutacağız

        # num1 veya num2 sıfır olana kadar devam et
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2  # büyük olandan küçük olanı çıkar
            else:
                num2 -= num1  # küçük olandan büyük olanı çıkar
            count += 1  # her işlemde sayacı artır

        return count
