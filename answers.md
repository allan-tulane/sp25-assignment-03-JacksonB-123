# CMPS 2200 Assignment 3
## Answers

**Name:**_____Jackson Burch____________________


Place all written answers from `assignment-03.md` here for easier grading.

1a) Given a $N$ dollars, a greedy algorithm for producing as few coins as possible that sum to $N$ would be to repeatedly subtract the largest power of 2 til $N$ equals 0.

1b)Prove that this algorithm is optimal by proving the greedy choice and optimal substructure properties.

"Greedy Choice Property: For any set of tasks, the task with earliest finish time is in some optimal solution." (class slides)
Chosing the largest coin less than or equal to $N$ because it is the "fastest" way to reach $N$. This works because any number can be broken down into sums of power of 2's. By chosing the largest coin less than or equal to $N$ you will reach $N$ with the ewest amount of coins

"Optimal substructure: An optimal solution can be constructed from optimal solutions of smaller subproblems." (class slides)
"Greedy choice: A greedy choice must be in some optimal solution (of a given size)." (class slides)
By chosing the greedy choice we are folowing the optimal substructure because we are making greedy choices of smaller sumproblems that are size N-2^k. At each level we choose the largest coin less than or equal to $N$.

1c) What is the work and span of your algorithm?

2a)  You realize the greedy algorithm you devised above doesn't work in Fortuito. Give a simple counterexample that shows that the greedy algorithm does not produce the fewest number of coins.

given an abitrary set of denomination such as (1,3,4) for a target such as $N$ = 6 the greedy algorithm in 1 does not work.
using the greedy algorithm in 1 we would first chose 4. Once we subtract 4 from 6 we have a remainder 2. We then chose 1 twice to get $N$ to equal 0.
we haven chose 3 coins to reach the target of $N$ = 6 but this is not the optimal solution. We could have chosen 3 twice, only using 2 coings to reach $N$ = 6. 







