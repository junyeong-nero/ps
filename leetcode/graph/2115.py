class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        rec2ing = {r: ing for r, ing in zip(recipes, ingredients)}
        memo = {s: True for s in supplies}
        visiting = set()

        def query(x):
            if x in memo:
                return memo[x]
            if x in visiting:          # cycle
                return False
            if x not in rec2ing:       # unknown ingredient not in supplies/recipes
                return False

            visiting.add(x)
            ok = all(query(y) for y in rec2ing[x])
            visiting.remove(x)

            memo[x] = ok
            return ok

        return [r for r in recipes if query(r)]
