class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        n = len(favoriteCompanies)
        company = [set(comp) for comp in favoriteCompanies]

        res = []
        for i in range(n):

            check = True
            for j in range(n):
                if i == j: continue
                if company[j] >= company[i]:
                    check = False
                    break

            if check:
                res.append(i)

        return res
                    

