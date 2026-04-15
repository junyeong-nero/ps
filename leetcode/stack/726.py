class Solution:

    def func(self, formula, multiple=1):

        n = len(formula)
        counter = Counter()
        i = 0

        while i < n:
            if formula[i].isupper():
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                atom = formula[i:j]

                k = j
                while k < n and formula[k].isnumeric():
                    k += 1

                num = int(formula[j:k]) if formula[j:k] else 1
                counter[atom] += num
                # print(atom, num)

                i = k

            elif formula[i] == "(":

                count = 1
                j = i + 1
                while j < n and count > 0:
                    if formula[j] == "(":
                        count += 1
                    if formula[j] == ")":
                        count -= 1

                    j += 1

                sub_formula = formula[i:j]

                k = j
                while k < n and formula[k].isnumeric():
                    k += 1

                num = int(formula[j:k]) if formula[j:k] else 1
                # print(sub_formula, num)

                counter += self.func(sub_formula[1:-1], multiple=num)

                i = k

        if multiple > 1:
            for key in counter:
                counter[key] = counter[key] * multiple

        return counter

    def countOfAtoms(self, formula: str) -> str:

        temp = self.func(formula)

        res = ""
        for key in sorted(temp.keys()):
            res += key + (str(temp[key]) if temp[key] > 1 else "")

        return res

