# 🍂 LeetCode 75 — Autumn in NYC Edition 🗽

> 🧡 A fall-in-Central-Park kind of grind: pumpkin spice, falling leaves, and 75 LeetCode problems. One commit per solved problem, cozy sweater optional.

☕ **The plan:** DP got trimmed down to 2 essentials (just enough to get the state-transition vibes), and the leftover quota got rerouted into stacks, greedy, DFS, and design/simulation problems — the topics that actually show up in interviews.

---

## 🍁 1. Array Two Pointers (5 problems)
📖 Reference: *Two Pointers Technique for 7 Array Problems*, *One Method to Rule All nSum Problems*

| # | Problem | Core Technique |
|---|---|---|
| 1 | 26. Remove Duplicates from Sorted Array | 🐢🐇 Slow/fast pointers, in-place dedup |
| 2 | 283. Move Zeroes | 🐢🐇 Slow/fast pointers |
| 3 | 167. Two Sum II | ↔️ Left/right pointers |
| 4 | 344. Reverse String | ↔️ Left/right swap |
| 5 | 5. Longest Palindromic Substring | 🎯 Expand from center |

## 🧣 2. Linked List (6 problems)
📖 Reference: *Two Pointers for 7 Linked List Problems*, *Every Way to Reverse a Linked List*

| # | Problem | Core Technique |
|---|---|---|
| 6 | 141. Linked List Cycle | 🐢🐇 Fast/slow pointers, cycle detection |
| 7 | 19. Remove Nth Node From End of List | 🐢🐇 Fast/slow pointers |
| 8 | 21. Merge Two Sorted Lists | 🪢 Dummy head node |
| 9 | 25. Reverse Nodes in k-Group | 🔁 Recursive reversal |
| 10 | 206. Reverse Linked List | 🔁 Iterative / recursive reversal |
| 11 | 234. Palindrome Linked List | 🪞 Find midpoint + reverse second half |

## 🍂 3. Sliding Window (4 problems)
📖 Reference: *Sliding Window Core Template*

| # | Problem | Core Technique |
|---|---|---|
| 12 | 76. Minimum Window Substring | 🪟 Sliding window template |
| 13 | 567. Permutation in String | 🪟 Fixed-size window |
| 14 | 438. Find All Anagrams in a String | 🪟 Fixed-size window |
| 15 | 3. Longest Substring Without Repeating Characters | 🪟 Sliding window |

## 🗽 4. Binary Search (4 problems)
📖 Reference: *Binary Search Core Template*, *A Mental Framework for Binary Search*

| # | Problem | Core Technique |
|---|---|---|
| 16 | 704. Binary Search | 🔍 Basic binary search |
| 17 | 34. Find First and Last Position of Element in Sorted Array | 🔍 Left/right boundary search |
| 18 | 33. Search in Rotated Sorted Array | 🔍 Binary search variant |
| 19 | 875. Koko Eating Bananas | 🔍 Binary search on the answer |

## 🎃 5. Stack / Queue / Monotonic Structures (7 problems) ⬆️
📖 Reference: *Classic Stack Problems*, *Bracket Problems Roundup*, *Monotonic Stack Template*, *Monotonic Queue for Sliding Window*

| # | Problem | Core Technique |
|---|---|---|
| 20 | 20. Valid Parentheses | 📚 Basic stack |
| 21 | 232. Implement Queue using Stacks | 📚 Two-stack simulation |
| 22 | 155. Min Stack | 📚 Auxiliary stack |
| 23 | 394. Decode String | 📚 Stack for nested structures |
| 24 | 739. Daily Temperatures | 📈 Monotonic stack |
| 25 | 84. Largest Rectangle in Histogram | 📈 Monotonic stack |
| 26 | 239. Sliding Window Maximum | 📈 Monotonic queue |

## 🍁 6. Binary Tree (7 problems)
📖 Reference: *Core Principles of Binary Tree Algorithms*, *Binary Tree Mental Models (Think / Construct / Postorder)*

| # | Problem | Core Technique |
|---|---|---|
| 27 | 104. Maximum Depth of Binary Tree | 🌳 Recursion / traversal |
| 28 | 226. Invert Binary Tree | 🌳 Recursion |
| 29 | 102. Binary Tree Level Order Traversal | 🌳 BFS |
| 30 | 105. Construct Binary Tree from Preorder and Inorder Traversal | 🌳 Recursive construction |
| 31 | 236. Lowest Common Ancestor of a Binary Tree | 🌳 Postorder traversal |
| 32 | 124. Binary Tree Maximum Path Sum | 🌳 Postorder traversal |
| 33 | 297. Serialize and Deserialize Binary Tree | 🌳 Serialization |

## 🍂 7. Binary Search Tree (3 problems)
📖 Reference: *BST Properties*, *BST Basic Operations*

| # | Problem | Core Technique |
|---|---|---|
| 34 | 230. Kth Smallest Element in a BST | 🌲 Inorder traversal |
| 35 | 98. Validate Binary Search Tree | 🌲 Inorder / recursion |
| 36 | 450. Delete Node in a BST | 🌲 BST operations |

## 🧡 8. DFS / Grid Search (4 problems) ⬆️
📖 Reference: *One Article to Crush All Island Problems*

| # | Problem | Core Technique |
|---|---|---|
| 37 | 200. Number of Islands | 🏝️ DFS grid traversal |
| 38 | 695. Max Area of Island | 🏝️ DFS connected components |
| 39 | 79. Word Search | 🏝️ DFS + backtracking |
| 40 | 130. Surrounded Regions | 🏝️ DFS boundary marking |

## 🗽 9. Graph Theory (3 problems)
📖 Reference: *Bipartite Graph Check*, *Topological Sort*, *Dijkstra's Algorithm*, *Union-Find*

| # | Problem | Core Technique |
|---|---|---|
| 41 | 785. Is Graph Bipartite? | 🎨 Graph coloring |
| 42 | 210. Course Schedule II | 🧭 Topological sort |
| 43 | 743. Network Delay Time | 🧭 Dijkstra |

## 🍁 10. Backtracking (5 problems)
📖 Reference: *Backtracking Framework*, *Permutations/Combinations/Subsets*, *Sudoku & N-Queens*

| # | Problem | Core Technique |
|---|---|---|
| 44 | 46. Permutations | 🔀 Permutation template |
| 45 | 78. Subsets | 🔀 Subset template |
| 46 | 77. Combinations | 🔀 Combination template |
| 47 | 51. N-Queens | ♛ Classic backtracking |
| 48 | 22. Generate Parentheses | ✂️ Pruned backtracking |

## 🎃 11. BFS (3 problems)
📖 Reference: *BFS Framework*

| # | Problem | Core Technique |
|---|---|---|
| 49 | 111. Minimum Depth of Binary Tree | 🌊 Level-order BFS |
| 50 | 752. Open the Lock | 🌊 BFS shortest path |
| 51 | 1091. Shortest Path in Binary Matrix | 🌊 Grid BFS |

## 🍂 12. Dynamic Programming (2 problems) ⬇️
📖 Reference: *DP Framework*, *Classic DP: Longest Common Subsequence*

| # | Problem | Core Technique |
|---|---|---|
| 52 | 322. Coin Change | 🎒 Knapsack DP basics |
| 53 | 1143. Longest Common Subsequence | 🧵 Classic two-string DP |

## 🧡 13. Greedy Algorithms (6 problems) ⬆️
📖 Reference: *Greedy Framework*, *Interval Scheduling*, *Gas Station Problem*, *One-Liner Greedy Tricks*

| # | Problem | Core Technique |
|---|---|---|
| 54 | 435. Non-overlapping Intervals | 📅 Interval scheduling |
| 55 | 45. Jump Game II | 🦘 Greedy jumping |
| 56 | 134. Gas Station | ⛽ Circular greedy |
| 57 | 55. Jump Game | 🦘 Greedy reachability |
| 58 | 406. Queue Reconstruction by Height | 📏 Sort + greedy |
| 59 | 763. Partition Labels | ✂️ Greedy partitioning |

## 🍁 14. Prefix Sum / Difference Array (2 problems)
📖 Reference: *Prefix Sum Arrays*, *Difference Arrays*

| # | Problem | Core Technique |
|---|---|---|
| 60 | 303. Range Sum Query - Immutable | ➕ Prefix sum |
| 61 | 1109. Corporate Flight Bookings | ➖ Difference array |

## 🗽 15. Design / Simulation (5 problems) ⬆️
📖 Reference: *Build Your Own LRU Cache*, *Build Your Own LFU Cache*, *Fancy 2D Array Traversal*

| # | Problem | Core Technique |
|---|---|---|
| 62 | 146. LRU Cache | 🗂️ Hash map + doubly linked list |
| 63 | 460. LFU Cache | 🗂️ Hash map + frequency lists |
| 64 | 54. Spiral Matrix | 🌀 Shrinking boundary simulation |
| 65 | 48. Rotate Image | 🌀 Layer-by-layer rotation |
| 66 | 8. String to Integer (atoi) | 🧮 Simulation + edge cases |

## 🍂 16. Hash Table (2 problems)
📖 Reference: *More Hash Table Practice*

| # | Problem | Core Technique |
|---|---|---|
| 67 | 1. Two Sum | #️⃣ Hash map |
| 68 | 49. Group Anagrams | #️⃣ Hash map |

## 🎃 17. Sorting / Divide and Conquer (2 problems)
📖 Reference: *Merge Sort Explained*, *Quick Sort Explained*

| # | Problem | Core Technique |
|---|---|---|
| 69 | 912. Sort an Array | 🔀 Merge / quick sort |
| 70 | 215. Kth Largest Element in an Array | ⚡ Quickselect |

## 🍁 18. Math / Bit Manipulation (2 problems)
📖 Reference: *Essential Math Tricks*, *Common Bit Tricks*

| # | Problem | Core Technique |
|---|---|---|
| 71 | 204. Count Primes | 🔢 Sieve of Eratosthenes |
| 72 | 136. Single Number | 🔢 XOR |

## 🧡 19. Hard-Mode Favorites (3 problems)
📖 Reference: *Solving Trapping Rain Water Efficiently*, *Median with Two Heaps*

| # | Problem | Core Technique |
|---|---|---|
| 73 | 42. Trapping Rain Water | 🌧️ Two pointers / monotonic stack |
| 74 | 4. Median of Two Sorted Arrays | 🔍 Binary search |
| 75 | 295. Find Median from Data Stream | ⚖️ Two heaps |

---

## 🍂 Topic Count Summary

| Topic | Count | Change |
|---|---|---|
| Array Two Pointers | 5 | - |
| Linked List | 6 | - |
| Sliding Window | 4 | - |
| Binary Search | 4 | - |
| Stack/Queue/Monotonic | 7 | +2 |
| Binary Tree | 7 | - |
| BST | 3 | - |
| DFS/Grid | 4 | new |
| Graph Theory | 3 | -2 |
| Backtracking | 5 | - |
| BFS | 3 | - |
| DP | 2 | -10 |
| Greedy | 6 | +3 |
| Prefix Sum/Diff | 2 | - |
| Design/Simulation | 5 | +3 |
| Hash Table | 2 | - |
| Sorting/D&C | 2 | - |
| Math/Bit Manip | 2 | - |
| Hard-Mode Favorites | 3 | - |
| **Total** | **75** | 🍂 |

🎃 DP is trimmed down to the 2 most essential problems — just enough to get comfortable with state transitions. If DP ends up showing up a lot in interviews later, more can be pulled in from the *Classic DP Practice I & II* tutorials.

---

## 🗽 Progress Tracker

| # | Problem | Solution |
|---|---|---|
| 1 | 26. Remove Duplicates from Sorted Array | [`0026_remove_duplicates_from_sorted_array.py`](./0026_remove_duplicates_from_sorted_array.py) 🍁✅ |
| 2 | 283. Move Zeroes | [`283_move_zeroes.py`](./283_move_zeroes.py) 🍁✅ |
| 3 | 167. Two Sum II | [`0167_two_sum_ii.py`](./0167_two_sum_ii.py) 🍁✅ |

---

🍁 *74 leaves left to rake. One commit at a time.* 🧡
