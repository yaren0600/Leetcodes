class Solution(object):
    def smallestNumber(self, n):
        # Eğer sayı pozitif değilse
        if n <= 0:
            return 0

        # Eğer n zaten tüm bitleri 1 olan bir sayı ise 1, 3, 7 gibi
        if (n & (n + 1)) == 0 :
            return n

        # n in binarydeki bit sayısını bul
        bits = n.bit_length()

        # O kadar bit uzunluğunda tüm 1lerden oluşan aday sayı 
        candidate = (1 << bits) - 1

        #Eğer aday >= n ise bu en küçük uygun sayıdır
        if candidate >= n:
            return candidate

        # Değilse bir bit daha ekleyerek yeni aday oluştur
        return ( 1 << (bits + 1)) - 1
        
        
