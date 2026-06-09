# Approach:
# Check each transaction to see if its amount is greater than 1000.
# For each transaction, compare it with every other transaction to find
# same-name transactions in different cities within 60 minutes.
# If either condition is met, mark the transaction as invalid.
#
# Time: O(n^2)
# Space: O(1)


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        res = []

        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")

            time = int(time)
            amount = int(amount)

            invalid = False

            if amount > 1000:
                invalid = True

            for j in range(len(transactions)):
                if i == j:
                    continue

                name2, time2, amount2, city2 = transactions[j].split(",")
                time2 = int(time2)

                if name == name2 and city != city2 and abs(time - time2) <= 60:
                    invalid = True
                    break

            if invalid:
                res.append(transactions[i])

        return res
