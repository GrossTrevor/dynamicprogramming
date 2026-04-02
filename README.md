# Greedy Algorithms
Python implementation of the FIFO (First-In, First-Out), LRU (Least Recently Used), and OPTFF (Belady’s Farthest-in-Future) algorithms for cache access.

## Authors
* Nicholas Farr UFID: 17993779
* Trevor Gross UFID: 11440394

## Project Structure
```
greedyalgorithms/
├── src/
│   ├── fifo.py    # Code and functions for FIFO algorithm
│   ├── lru.py          # Code and functions for LRU algorithm
│   ├── main.py          # Ingests input, runs algorithms, and creates output file
│   ├── optff.py          # Code and functions for Belady's algorithm
│   ├── q1.ipynb          # Used to answer written question 1
│   └── test_generator.py       # Generate test cases and files
├── data/                    # Input/Output test files
└── tests/            # Input test files
```

## Prerequisites
* Python [version, e.g., 3.10+]

### Data Formatting
#### Input
Input data must be placed into `data/input.in` and formatted as follows:
```
k m
r1 r2 r3 ... rm
```
Where:
* `k` = cache capacity (`k >= 1`)
* `m` = number of requests
* `r1 r2 r3 ... rm` = sequence of integer IDs

#### Output
Output data will be placed in `data/output.out` and formatted as follows:
```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```

## Running the Algorithms
* Create input based on instructions above
* Run the following command from the `greedyalgorithms/` directory: `python src/main.py`
* Examine the output in the `data/output.out` file

## Written Component
### Question 1

| File | k | m | FIFO | LRU | OPTFF |
|------|---|---|------|-----|-------|
| 1 | 10 | 50 | 28 | 24 | 20 |
| 2 | 35 | 250 | 173 | 173 | 110 |
| 3 | 25 | 100 | 78 | 74 | 53 |

Does OPTFF have the fewest misses? Yes, OPTFF proves to be the most effective algorithm of the three tested. This is because it looks ahead on the input data and makes a perfect eviction choice.

How does FIFO compare to LRU? LRU generally does at least equal or fewer misses to the FIFO algorithm. This is because FIFO just evicts the oldest item, rather than the one being the least frequently used - LRU is being smarter about which ID to evict.

### Question 2

Consider the sequence : 1 2 3 1 4 2.
At request 4, the LRU algorithm will choose to evict 2, as it is the least recently used item in our cache. Which will result in an additional miss directly after when 2 reappears. Howevever the OPT algorithm will evict either 1 or 3 as they are not used again in this sequence, preventing 2 from being evicted. The total miss count for LRU is 5, while the OPT algorithm only has 4 misses.

### Question 3
$$
\begin{aligned}
&\text{Let OPTFF be Belady’s Farthest-in-Future algorithm} \\
&\text{Let } A \text{ be any offline algorithm that knows the full request sequence} \\
&\text{Prove that the number of misses of OPTFF is no larger than that of } A \text{ on any fixed sequence} \\
& \\
&\text{Let } m_{\text{OPTFF}} \text{ be the number of misses from the OPTFF algorithm} \\
&\text{Let } m_{A} \text{ be the number of misses from algorithm } A \\
&\text{We must show that } m_{\text{OPTFF}} \leq m_{A} \\
& \\
&\text{Assume the first point of disagreement between the two algorithms is at time } t \\
&\text{Meaning, the algorithms always evict the same page up until time } t-1 \\
& \\
&\text{Let:} \\
&x = \text{the page OPTFF evicts at time } t \\
&y = \text{the page $A$ evicts at time } t \\
&\text{Thus, } x \ne y \\
& \\
&\text{By definition of OPTFF, the next time $x$ is accessed must occur after the next time $y$ is accessed} \\
&\text{Assume we have $A'$ that is the same algorithm as $A$, but evicts $x$ when $A$ evicts $y$, and vice versa} \\
&\text{Let } m_{A'} \text{ be the number of misses from algorithm } A' \\
& \\
&\text{Since we know $y$ is accessed next before $x$, when $y$ is accessed $A$ misses, but $A'$ hits} \\
&\text{So, we know $A$ will have at least one miss} \\
&\text{Going forward, we do not know if $A'$ will miss, since $x$ may or may not be accessed} \\
&\text{We also do not know if $A$ will miss on $x$ later, as it still could be evicted} \\
&\text{This uncertainty means that } m_{A} \geq m_{A'} \\
&\text{This is a contradiction because we created $A'$ under the pretext that it will have no more misses than $A$ and will agree with OPTFF a step further than $A$} \\
&\text{So, no algorithm can be more optimal than OPTFF} \\
\end{aligned}
$$
