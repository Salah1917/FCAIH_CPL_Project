import tkinter as tk
from tkinter import ttk


def is_safe(queens, row, col):
    def not_same_column(r, c):
        return col != c

    def not_same_diagonal(r, c):
        return abs(row - r) != abs(col - c)

    def no_conflict(queen_pos):
        r, c = queen_pos
        return not_same_column(r, c) and not_same_diagonal(r, c)

    return all(map(no_conflict, queens))


def solve_nqueens(n, row=0, queens=(), col=0):
    if row == n:
        yield queens
    elif col == n:
        return
    else:
        if is_safe(queens, row, col):
            yield from solve_nqueens(n, row + 1, queens + ((row, col),), 0)
        yield from solve_nqueens(n, row, queens, col + 1)

class NQueensGUI:
    def __init__(self, root):
        self.root = root
        root.title("N-Queens Solver")

        self.n_var = tk.IntVar(value=8)

        control_frame = ttk.Frame(root)
        control_frame.pack(pady=10)

        ttk.Label(control_frame, text="Board Size:").pack(side=tk.LEFT)
        ttk.Entry(control_frame, textvariable=self.n_var, width=5).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Solve", command=self.run_solver).pack(side=tk.LEFT)

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.solutions = []
        self.current_index = 0

        nav_frame = ttk.Frame(root)
        nav_frame.pack()

        ttk.Button(nav_frame, text="< Prev", command=self.prev_solution).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="Next >", command=self.next_solution).pack(side=tk.LEFT, padx=5)

        self.status = ttk.Label(root, text="No solutions yet.")
        self.status.pack(pady=5)

    def run_solver(self):
        n = self.n_var.get()
        self.solutions = list(solve_nqueens(n))
        self.current_index = 0
        if self.solutions:
            self.draw_solution(self.solutions[0])
            self.status.config(text=f"1 / {len(self.solutions)} solutions")
        else:
            self.canvas.delete("all")
            self.status.config(text="No solutions found.")

    def draw_solution(self, solution):
        self.canvas.delete("all")
        n = self.n_var.get()
        size = 400
        cell = size / n

        # Draw board
        for r in range(n):
            for c in range(n):
                color = "#eee" if (r + c) % 2 == 0 else "#555"
                self.canvas.create_rectangle(
                    c*cell, r*cell, (c+1)*cell, (r+1)*cell,
                    fill=color, outline="black"
                )

        # Draw queens
        for r, c in solution:
            self.canvas.create_oval(
                c*cell + cell*0.2,
                r*cell + cell*0.2,
                (c+1)*cell - cell*0.2,
                (r+1)*cell - cell*0.2,
                fill="red"
            )

    def next_solution(self):
        if not self.solutions:
            return
        self.current_index = (self.current_index + 1) % len(self.solutions)
        self.draw_solution(self.solutions[self.current_index])
        self.status.config(text=f"{self.current_index+1} / {len(self.solutions)} solutions")

    def prev_solution(self):
        if not self.solutions:
            return
        self.current_index = (self.current_index - 1) % len(self.solutions)
        self.draw_solution(self.solutions[self.current_index])
        self.status.config(text=f"{self.current_index+1} / {len(self.solutions)} solutions")


if __name__ == "__main__":
    root = tk.Tk()
    gui = NQueensGUI(root)
    root.mainloop()
