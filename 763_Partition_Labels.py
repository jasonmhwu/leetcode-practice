from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # run through the list once and record the start and end pos for each character
        # if you find other characters starting before the end time, use the longer end time as the new one (takes at most 2 sweeps)
        # overall takes O(N) time, O(N) space
        
        pos = dict()
        for idx, c in enumerate(S):
            if c not in pos.keys():
                pos[c] = [idx, idx]
            else:
                pos[c][1] = idx
                
        ans = []
        start, end = 0, 0
        while start < len(S):
            start, end = pos[S[start]][0], pos[S[start]][1]
            for _, (tmp_s, tmp_e) in pos.items():
                if tmp_s < end:
                    end = max(end, tmp_e)
            ans.append(end-start+1)
            start = end + 1
        return ans
            
sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabels("aaa"))
print(sol.partitionLabels("abcba"))
