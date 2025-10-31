class Solution(object):
    def getSneakyNumbers(self, nums):
        #Counter listedeki her elemanın kaç kez geçtiğini sayar
        from collections import Counter

        #nums listesindeki her sayının kaç kez geçtiğini sayıyoruz
        count = Counter(nums)

        #coun sözlüğünde dolaşılır
        # Eğer sayı 2 kez geçmişse (freq ==2) onu cevaba ekleriz
        res = [num for num, freq in count.items() if freq == 2]
        return res
