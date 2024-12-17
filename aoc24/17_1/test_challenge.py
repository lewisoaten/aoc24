from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()
    )
    assert input == (
        {"Register A": 729, "Register B": 0, "Register C": 0},
        (0, 1, 5, 4, 3, 0),
    )


def test_compute_instruction_adv():
    # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's
    # combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer
    # and then written to the A register.
    assert challenge.compute_instruction(challenge.Ins.adv, 2, {"Register A": 8}, 0) == (
        {"Register A": 2},
        2,
        None,
    )
    assert challenge.compute_instruction(challenge.Ins.adv, 5, {"Register A": 8, "Register B": 3}, 0) == (
        {"Register A": 1, "Register B": 3},
        2,
        None,
    )


def test_compute_instruction_bxl():
    # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
    assert challenge.compute_instruction(challenge.Ins.bxl, 2, {"Register B": 8}, 0) == (
        {"Register B": 10},
        2,
        None,
    )


def test_compute_instruction_bst():
    # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    assert challenge.compute_instruction(challenge.Ins.bst, 1, {}, 0) == (
        {"Register B": 1},
        2,
        None,
    )
    assert challenge.compute_instruction(challenge.Ins.bst, 5, {"Register B": 123}, 0) == (
        {"Register B": 3},
        2,
        None,
    )


def test_compute_instruction_jnz():
    # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of
    # its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    assert challenge.compute_instruction(challenge.Ins.jnz, 7, {"Register A": 0}, 0) == (
        {"Register A": 0},
        2,
        None,
    )
    assert challenge.compute_instruction(challenge.Ins.jnz, 7, {"Register A": 1}, 0) == (
        {"Register A": 1},
        7,
        None,
    )


def test_compute_instruction_bxc():
    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads
    # an operand but ignores it.)
    assert challenge.compute_instruction(challenge.Ins.bxc, 0, {"Register B": 5, "Register C": 3}, 0) == (
        {"Register B": 6, "Register C": 3},
        2,
        None,
    )


def test_compute_instruction_out():
    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by
    # commas.)
    assert challenge.compute_instruction(challenge.Ins.out, 2, {}, 0) == (
        {},
        2,
        2,
    )
    assert challenge.compute_instruction(challenge.Ins.out, 6, {"Register C": 123}, 0) == (
        {"Register C": 123},
        2,
        3,
    )


def test_compute_instruction_bdv():
    # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    assert challenge.compute_instruction(challenge.Ins.bdv, 2, {"Register A": 8}, 0) == (
        {"Register A": 8, "Register B": 2},
        2,
        None,
    )
    assert challenge.compute_instruction(challenge.Ins.bdv, 5, {"Register A": 8, "Register B": 3}, 0) == (
        {"Register A": 8, "Register B": 1},
        2,
        None,
    )


def test_compute_instruction_cdv():
    # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
    assert challenge.compute_instruction(challenge.Ins.cdv, 2, {"Register A": 8}, 0) == (
        {"Register A": 8, "Register C": 2},
        2,
        None,
    )
    assert challenge.compute_instruction(challenge.Ins.cdv, 5, {"Register A": 8, "Register B": 3}, 0) == (
        {"Register A": 8, "Register B": 3, "Register C": 1},
        2,
        None,
    )


def test_challenge1():
    input = challenge.parse_input(
        """
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
""".strip()
    )

    assert challenge.process(input) == "0,1,2"


def test_challenge2():
    input = challenge.parse_input(
        """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()
    )

    assert challenge.process(input) == "4,2,5,6,7,7,7,7,3,1,0"


def test_challenge3():
    input = challenge.parse_input(
        """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()
    )

    assert challenge.process(input) == "4,6,3,5,6,3,5,2,1,0"
