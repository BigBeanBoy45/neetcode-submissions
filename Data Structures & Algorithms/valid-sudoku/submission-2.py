class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkArray(array: List[List[str]]) -> bool:
            memory: set[str] = set()
            for r in array:
                for x in r:
                    if x == ".": 
                        continue
                    elif x in memory:
                        print(f"failed at: \n{r}\nduplicate {x}")
                        return False
                    else:
                        memory.add(x)
                memory.clear()
            return True

        
        # check rows
        if checkArray(board) == False:
            return False
            

        # check cols
        cols: list[list[str]] = [[] for _ in range(9)]
        for i in range(9):
            for r in board:
                cols[i].append(r[i])
        if checkArray(cols) == False:
            return False
        

        # check boxes
        # construct boxes array
        boxes: list[list[list[str]]] = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                boxes[i // 3][j // 3].append(board[i][j])

        for r in boxes:
            if checkArray(r) == False:
                return False
        
        return True
            
