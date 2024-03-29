## Justice Served 

#### Input 

$` n \in (1..2e5) `$

$` x_i, y_i \in (1..1e9) `$

There is no i,j such that: 
```x_i == x_j && y_i == y_j```

#### 
$f(i)$ for each $i \in (1..n)$

$f(i) = max (f(j) + 1)$ where $(x_j, y_j) \subset (x_i, y_i)$   

#### 
---
***NOTE***

> "if (x, y) in (a, b) then len(x,y) < len(a, b)"

so we only need to consider larger segments when computing f (i) 
---
#### Solution 1 

1. Sort segments by length 
2. Go through segments from largest to smallest -> consider each possible pair 

Time complexity: O(N^2) 

---
#### Solution 2

1. Go from left to right through segment endpoints, keep track of all current segments and their value. 
2. When entering new segment, find max previous segment that end after this segment. 





---


