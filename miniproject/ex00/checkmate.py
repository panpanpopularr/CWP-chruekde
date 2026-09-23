PIECES = "PBRQK"


def print_board(title, board):
    print(title)

    width = len(" ".join(board[0]))
    border = "+" + "-" * (width + 2) + "+"

    print(border)

    for row in board:
        print("| " + " ".join(row) + " |")

    print(border)


def validate_board(board):
    if not isinstance(board, str):
        print("Error: Board must be a string.")
        return None

    rows = board.splitlines()

    if len(rows) == 0:
        print("Error: Board is empty.")
        return None

    size = len(rows)

    for row in rows:
        if len(row) != size:
            print("Error: Board is not square.")
            return None

    king_count = 0

    for row in rows:
        king_count += row.count("K")

    if king_count == 0:
        print("Error: King is missing.")
        return None

    if king_count > 1:
        print("Error: Too many Kings.")
        return None

    return rows


def check_direction(
    board,
    attack_map,
    start_row,
    start_col,
    row_step,
    col_step
):
    size = len(board)

    row = start_row + row_step
    col = start_col + col_step

    while 0 <= row < size and 0 <= col < size:
        current = board[row][col]

        if current == "K":
            attack_map[row][col] = "X"
            return True

        if current in PIECES:
            return False

        attack_map[row][col] = "X"

        row += row_step
        col += col_step

    return False


def checkmate(board, debug=False):
    rows = validate_board(board)

    if rows is None:
        return

    size = len(rows)

    attack_map = []

    for row in rows:
        attack_map.append(list(row))

    king_attacked = False

    for row in range(size):
        for col in range(size):
            piece = rows[row][col]

            if piece == "P":
                attack_row = row - 1

                if attack_row >= 0:
                    for attack_col in [col - 1, col + 1]:
                        if 0 <= attack_col < size:
                            target = rows[attack_row][attack_col]

                            if target == "K":
                                attack_map[attack_row][attack_col] = "X"
                                king_attacked = True

                            elif target not in PIECES:
                                attack_map[attack_row][attack_col] = "X"

            elif piece == "R":
                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)
                ]

                for row_step, col_step in directions:
                    if check_direction(
                        rows,
                        attack_map,
                        row,
                        col,
                        row_step,
                        col_step
                    ):
                        king_attacked = True

            elif piece == "B":
                directions = [
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1)
                ]

                for row_step, col_step in directions:
                    if check_direction(
                        rows,
                        attack_map,
                        row,
                        col,
                        row_step,
                        col_step
                    ):
                        king_attacked = True

            elif piece == "Q":
                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1)
                ]

                for row_step, col_step in directions:
                    if check_direction(
                        rows,
                        attack_map,
                        row,
                        col,
                        row_step,
                        col_step
                    ):
                        king_attacked = True

    if debug:
        print()

        print_board("Original Board:", rows)

        print()

        print_board("Attack Map:", attack_map)

        print()

    if king_attacked:
        print("Success")
    else:
        print("Fail")