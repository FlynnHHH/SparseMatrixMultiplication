class Triple:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
    




row1, col1 = map(int, input().split())
row2, col2 = map(int, input().split())
if row1 <= 0 or row1 > 20 or col1 <= 0 or col1 > 20 or row2 <= 0 or row2 > 20 or col2 <= 0 or col2 > 20:
    print("ERROR")
else:
    