class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        #  Guard ve Wall konumlarını set içinde tutalım (hızlı erişim için)
        guards_set = set(map(tuple, guards))
        walls_set = set(map(tuple, walls))
        
        #  Görülen hücreleri tutacak set
        guarded = set()
