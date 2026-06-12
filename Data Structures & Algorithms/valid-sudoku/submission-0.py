from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Create dictionaries to hold our sets of "seen" numbers
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        # 2. Use a nested loop to visit every single cell in the 9x9 grid
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # 3. If the cell is empty, skip it and keep moving
                if val == ".":
                    continue
                
                # 4. Calculate which 3x3 sub-box coordinate we are in
                box_coord = (r // 3, c // 3)
                
                # 5. Check if this number has already been seen in this row, col, or box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_coord]):
                    return False # Duplicate found! The board is invalid.
                
                # 6. If it's a new number, add it to our records
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_coord].add(val)
                
        # If we check the whole board without any collisions, it's valid!
        return True
        