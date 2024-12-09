class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        tmp = sorted(arr)
        j = 1
        d = {}
        for i in tmp:
            # key:value
            if i not in d:
                d[i] = j
                j += 1
        # for a in arr:
        #     l.append(d[a]) 推入陣列
        return [d[a] for a in arr] 

