class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        #  Guard ve Wall konumlarını set içinde tutalım (hızlı erişim için)
        guards_set = set(map(tuple, guards))
        walls_set = set(map(tuple, walls))
        
        #  Görülen hücreleri tutacak set
        guarded = set()
        
        #  Her guard için 4 yönü kontrol et
        for r, c in guards:
            # Yukarı, aşağı, sol, sağ yönler
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                # Yön boyunca ilerle
                while 0 <= nr < m and 0 <= nc < n and (nr, nc) not in walls_set and (nr, nc) not in guards_set:
                    guarded.add((nr, nc))
                    nr += dr
                    nc += dc
        
        #  Sonuç = Toplam boş hücre - görülen hücreler
        total_cells = m * n
        occupied = len(guards) + len(walls)
        return total_cells - occupied - len(guarded)
