import heapq

nums = [34, 23, 54, 55, 87, 12, 35, 1]

# Find the largest 3 elements in nums
print(heapq.nlargest(3, nums))

# Find the smallest 3 elements in nums
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# Find the most expensive 3 elements in portfolio
print(heapq.nlargest(3, portfolio, key=lambda d: d['price']))


# heap sorted, the first element is always the smallest
heapq.heapify(nums)
print(nums)
