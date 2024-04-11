def identify_white_box(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    top = left = height = width = None
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'w':
                top = i
                left = j
                break
        if top is not None:
            break

    if top is not None:

        width = 0
        for j in range(left, cols):
            if matrix[top][j] == 'w':
                width += 1
            else:
                break

    
        height = 0
        for i in range(top, rows):
            if matrix[i][left] == 'w':
                height += 1
            else:
                break

    return {'top': top, 'left': left, 'height': height, 'width': width}


matrix = [
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
]

white_box = identify_white_box(matrix)
print(white_box)