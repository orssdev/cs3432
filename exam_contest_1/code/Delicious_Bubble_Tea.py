import heapq
n = int(input())
tea_prices = [int(x) for x in input().split()]
m = int(input())
topping_prices = [int(x) for x in input().split()]

heap = []
for i in range(n):
    valid_topping = [int(x) for x in input().split()]
    for topping_index in valid_topping[1:]:
        total_cost = tea_prices[i] + topping_prices[topping_index - 1]
        heapq.heappush(heap, total_cost)

money = int(input())
students = (money // heap[0]) - 1
if students < 0:
    print(0)
else:
    print(students)