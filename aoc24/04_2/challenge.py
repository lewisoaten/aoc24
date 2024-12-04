from .. import tools


def test_x_mas(input: list[list[str]]) -> bool:
    assert len(input) == 3
    assert len(input[0]) == 3
    assert len(input[1]) == 3
    assert len(input[2]) == 3

    if input[0][0] == "M" and input[2][0] == "M" and input[1][1] == "A" and input[0][2] == "S" and input[2][2] == "S":
        return True
    return False


def find_xmas(input: list[list[str]]) -> bool:
    if test_x_mas(input):
        return True

    rotated_90 = tools.rotate_char2d(input)
    if test_x_mas(rotated_90):
        return True

    rotated_180 = tools.rotate_char2d(rotated_90)
    if test_x_mas(rotated_180):
        return True

    rotated_270 = tools.rotate_char2d(rotated_180)
    if test_x_mas(rotated_270):
        return True

    return False


def process(input: list[list[str]]):
    count_xmas = 0

    for y in range(len(input) - 2):
        for x in range(len(input[y]) - 2):
            if find_xmas(tools.copy_char2d_sub(input, x, y, 3, 3)):
                count_xmas += 1

    return count_xmas


def challenge():
    return process(tools.read_to_char2d("./inputs/04_1.txt"))
