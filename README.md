# Sudoku

A Python program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character `'.'`

## Installation

You can install this using `pip`. Just run `pip install sudoku9`

## Usage

### Initial Sudoku

![initial Sudoku](initial.png)

### Final sudoku

![Final Image](final.png)

For the above given diagrams, the corresponding input to the program will be

```python
["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
```

And corresponding output will be

```python
["534678912","672195348","198342567","859761423","426853791","713924856","961537284","287419635","345286179"]
```

## Example

```python
# import package
from sudoku9.sudoku import Sudoku
# input board
board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]

# create sudoku
puzzle = Sudoku(board)
# solve puzzle
# return solved board
output = puzzle.solveSudoku()
# output = ['534678912', '672195348', '198342567', '859761423', '426853791', '713924856', '961537284', '287419635', '345286179']
```

## Contact

If you find any bugs then open a issue on this repository.
