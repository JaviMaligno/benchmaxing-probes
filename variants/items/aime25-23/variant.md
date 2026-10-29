# aime25-23 variant

From an unlimited supply of $1$-cent coins, $10$-cent coins, and $24$-cent coins, Maya wants to find a collection of coins that has a total value of $N$ cents, where $N$ is a positive integer. She uses the so-called *greedy algorithm*, successively choosing the coin of greatest value that does not cause the value of her collection to exceed $N$. For example, to get $40$ cents, Maya will choose a $24$-cent coin, then a $10$-cent coin, then $6$ $1$-cent coins. However, this collection of $8$ coins uses more coins than necessary to get a total of $40$ cents; indeed, choosing $4$ $10$-cent coins achieves the same total with only $4$ coins.

In general, the greedy algorithm *succeeds* for a given $N$ if no other collection of $1$-cent, $10$-cent, and $24$-cent coins gives a total value of $N$ cents using strictly fewer coins than the collection given by the greedy algorithm. Find the number of values of $N$ between $1$ and $1000$ inclusive for which the greedy algorithm succeeds.

**Answer:** 675
