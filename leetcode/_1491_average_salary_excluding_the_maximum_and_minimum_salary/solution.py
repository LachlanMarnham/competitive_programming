from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary, max_salary = min(salary), max(salary)
        return (sum(salary) - min_salary - max_salary) / (len(salary) - 2)
