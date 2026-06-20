class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # ソートする
        sorted_hash = {}

        for s in strs:
            key = "".join(sorted(s))
            
            if key not in sorted_hash:
                sorted_hash[key] = []

            sorted_hash[key].append(s)
        
        return list(sorted_hash.values())

        # ソートしたものをhash mapで持つ


        # ループで同じものを見つけてarrayで管理

        # return