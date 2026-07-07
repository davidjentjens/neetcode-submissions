class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        available_bills = {
            5: 0,
            10: 0,
            20: 0
        }

        for bill in bills:
            print(available_bills)
            if bill == 5:
                available_bills[5] += 1
            elif bill == 10:
                if available_bills[5] >= 1:
                    available_bills[5] -= 1
                    available_bills[10] += 1
                else:
                    return False
            elif bill == 20:
                if available_bills[10] >= 1 and available_bills[5] >= 1:
                    available_bills[5] -= 1
                    available_bills[10] -= 1
                    available_bills[20] += 1
                elif available_bills[5] >= 3:
                    available_bills[5] -= 3
                    available_bills[20] += 1
                else:
                    return False
            else:
                # Invalid bill
                return False

        return True