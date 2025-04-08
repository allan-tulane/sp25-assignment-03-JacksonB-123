# CMPS 2200 Assignment 3
## Answers

**Name:**_____Jackson Burch____________________


Place all written answers from `assignment-03.md` here for easier grading.

1a) Given a $N$ dollars, a greedy algorithm for producing as few coins as possible that sum to $N$ would be to repeatedly subtract the largest power of 2 til $N$ equals 0.

1b)Prove that this algorithm is optimal by proving the greedy choice and optimal substructure properties.

"Greedy Choice Property: For any set of tasks, the task with earliest finish time is in some optimal solution." (class slides)

Chosing the largest coin less than or equal to $N$ because it is the "fastest" way to reach $N$. This works because any number can be broken down into sums of power of 2's. By chosing the largest power of 2 coin less than or equal to $N$ you will reach $N$ with the fewest amount of coins

"Optimal substructure: An optimal solution can be constructed from optimal solutions of smaller subproblems." (class slides)

By chosing the greedy choice we are folowing the optimal substructure because we are making greedy choices of smaller sumproblems that are size N-2^k. At each level we choose the largest coin less than or equal to $N$.

1c) What is the work and span of your algorithm?

work = O(log n)

span = O(log n)

2a)  You realize the greedy algorithm you devised above doesn't work in Fortuito. Give a simple counterexample that shows that the greedy algorithm does not produce the fewest number of coins.

given an abitrary set of denomination such as (1,3,4) for a target such as $N$ = 6 the greedy algorithm in 1 does not work.
using the greedy algorithm in 1 we would first chose 4. Once we subtract 4 from 6 we have a remainder 2. We then chose 1 twice to get $N$ to equal 0.
we haven chose 3 coins to reach the target of $N$ = 6 but this is not the optimal solution. We could have chosen 3 twice, only using 2 coings to reach $N$ = 6. 

2b)  Since you paid attention in Algorithms class, you realize that while this problem does not have the greedy choice property it does have an optimal substructure property. State and prove this property.

"Optimal substructure: An optimal solution can be constructed from optimal solutions of smaller subproblems." (class slides)

To solve for the optimal solution of N using d_i denomination you must first make change.

N' = N-d_i

N-d_i is a subproblem.

You are solving for the minimum number of coins for each sub problem C(n) to make N. C(n) is the minimum number of coins to make change for N.

C(n) = min d_i <= N(1+C(N-d_i)).

the sub problem is solved optimally, following the optimal substructure property.



2c) Use this optimal substructure property to design a dynamic programming algorithm for this problem. If you used top-down or bottom-up memoization to avoid recomputing solutions to subproblems, what is the work and span of your approach?

"Optimal substructure: An optimal solution can be constructed from optimal solutions of smaller subproblems." (class slides)

bottom up approach. The optimal solution for N using d_i denominations must include an optimal solved sub problem of N-d_i.

work W(n) = O(nk)
span S(n) = O(n)









