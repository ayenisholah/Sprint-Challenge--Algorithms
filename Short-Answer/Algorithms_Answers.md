#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
- The loop would run for n^3 times.
- if n = 2, the loop would run 8 times.
- the runtime of an assignment is always a constant O(1)
- final runtime complexity is O(n^3 + 1)

b)
- the first for loop would run n times O(n)
- the second while loop would also run n times O(n)
- Since we have a nested loop, we multiply both O(n^2)
- the two arithmetic computation is a constant O(1 + 1)
- final runtime analysis is O(n^2 + 2)

c)
- The recursive loops runs n times O(n)
- the return execute once O(1)
- final runtime analysis is O(n + 1)

## Exercise II
- Break = false
- Throw the egg down from the (n/2)th floor
- If it breaks, set Break = True and throw another from ((n/2)/2)th floor
- Otherwise, throw another from ((n + (n/2))/2)th floor
- Do this recursively until break = false

- The first function is being called recursively n times before reaching base case so its O(n), often called linear.
- The recursive function have a runtime complexity of O((n) + (n/2^1) + (n/2^2) + ... (n/2^i))
- Since we're using the divide and conquer approach, the O(n) is basically logarithmic.

