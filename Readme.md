# N-Queens Solver: Imperative vs Declarative Approaches

## 📌 Project Overview

This project implements the classic **N-Queens problem** using **two fundamentally different programming paradigms**:

1. **Imperative (State-Based) Approach**
2. **Declarative / Functional (Recursive Generator) Approach**

Both approaches are tested using **the same Tkinter-based GUI**, ensuring a **fair comparison** in terms of visualization, user interaction, and environment.

The goal is to compare:
- Algorithm design
- Data structures
- Performance
- Readability and maintainability

---

## ♟️ The N-Queens Problem

The N-Queens problem asks:

> How can N queens be placed on an N×N chessboard so that no two queens threaten each other?

This means:
- No two queens share the same row
- No two queens share the same column
- No two queens share the same diagonal

---

## 🧠 Approach 1: Imperative (Backtracking with Mutable State)

### 🔧 Key Characteristics

- Uses **explicit backtracking**
- Maintains **mutable state**
- Uses **sets** to track:
  - Columns
  - Positive diagonals (`row + col`)
  - Negative diagonals (`row - col`)
- Uses **loops + recursion**
- Modifies the board in-place

### 🧩 Core Techniques

- Backtracking with pruning
- Fast conflict detection using hash sets
- Direct board mutation and rollback

### 📋 Example Concepts Used

- `for` loops to iterate columns
- Sets to store used columns and diagonals
- Explicit add/remove operations during recursion
- Board updated using `"Q"` and `"."`

### ⚠️ Challenges

- Careful bookkeeping required when:
  - Adding/removing diagonals
  - Resetting board state
- Higher chance of bugs if state cleanup is incorrect

---

## 🧠 Approach 2: Declarative / Functional (Recursive Generator)

### 🔧 Key Characteristics

- Uses **pure recursion**
- No mutable shared state
- Each solution is a **new tuple**
- Uses a **mathematical `is_safe` check**
- Uses **generators (`yield`)**

### 🧩 Core Techniques

- Recursive problem definition
- Conflict detection via:
  - Column comparison
  - Diagonal math: `abs(row₁ - row₂) != abs(col₁ - col₂)`
- Immutable tuples for queen positions

### 📋 Example Concepts Used

- Recursion only (no loops for backtracking control)
- Tuple creation for every recursive step
- Functional-style safety checks

### ⚠️ Challenges

- Repeated safety checks increase computation
- Creating new tuples for every recursive call adds overhead
- Less intuitive for beginners to trace execution

---

## ⚖️ Fair Comparison

To ensure fairness:

- ✅ **Same GUI** is used for both solvers
- ✅ Same board size and visualization
- ✅ Same machine and Python interpreter
- ✅ Only the solving algorithm differs

This isolates **algorithmic performance** from UI overhead.

---

## 🔁 Loops vs Recursion

| Aspect | Imperative | Declarative |
|------|-----------|------------|
| Control Flow | Loops + recursion | Recursion only |
| State | Mutable | Immutable |
| Board | Modified in-place | Rebuilt via tuples |
| Safety Check | O(1) using sets | O(n) using math |

---

## ⏱️ Performance Comparison

Measured execution times for both algorithms running under identical conditions
(using the same GUI, same machine, and same Python interpreter).

> Times are approximate and represent total solution generation time.

| N | Imperative Time | Declarative Time |
|---|-----------------|------------------|
| 4 | < 0.1 s         | < 0.1 s          |
| 5 | < 0.1 s         | < 0.1 s          |
| 6 | < 0.1 s         | < 0.1 s          |
| 7 | < 0.1 s         | < 0.1 s          |
| 8 | < 0.1 s         | < 0.1 s          |
| 9 | < 0.1 s         | < 0.1 s          |
| 10 | < 0.1 s        | < 0.1 s          |
| 11 | < 0.2 s        | 2.4 s            |
| 12 | 1.2 s          | 13 s             |
| 13 | 5.8 s          | 1 min 17 s       |

---

### 📊 Observations

- For **small board sizes (N ≤ 10)**, both approaches perform similarly and complete almost instantly.
- Starting at **N = 11**, performance differences become significant.
- The **imperative approach scales far better** as N increases.
- The **declarative approach experiences exponential slowdown** due to repeated safety checks and immutable data creation.

---

## 🏁 Final Verdict

The **imperative backtracking implementation is faster and more scalable** for larger N.

**Reasons:**
- Constant-time conflict detection using sets
- Early pruning of invalid placements
- No repeated scanning of previous queens
- In-place state updates with minimal memory allocation

**Declarative trade-offs:**
- Cleaner, more expressive logic
- Easier to reason about correctness
- Slower due to:
  - Linear-time `is_safe` checks
  - Tuple creation at every recursive step
  - Less aggressive pruning

---

## 🎯 Conclusion

| Criteria | Imperative | Declarative |
|--------|-----------|------------|
| Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Memory Efficiency | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Readability | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Functional Purity | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Educational Value | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

Both approaches are valid and educational:
- The **imperative approach** excels in performance and scalability.
- The **declarative approach** excels in clarity and functional design.


## 📚 Technologies Used

- Python 3
- Tkinter (GUI)
- Backtracking Algorithms
- Functional Programming Concepts
