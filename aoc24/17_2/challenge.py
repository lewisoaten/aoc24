from collections import ChainMap
from enum import IntEnum

from .. import tools


class Ins(IntEnum):
    adv = 0  # performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand.
    # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then
    # written to the A register.
    bxl = 1  # calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
    bst = 2  # calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    jnz = 3  # does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand;
    # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    bxc = (
        4  # calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    )
    out = 5  # calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    bdv = 6  # works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    cdv = 7  # works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)


def compute_instruction(opcode: Ins, operand: int, registers: dict[str, int], pointer: int) -> tuple[dict[str, int], int, int]:

    output = None
    combo_operand = None

    if operand <= 3:
        combo_operand = operand
    elif operand == 4:
        combo_operand = registers["Register A"]
    elif operand == 5:
        combo_operand = registers["Register B"]
    elif operand == 6:
        combo_operand = registers["Register C"]

    pointer += 2

    if opcode == Ins.adv:
        assert combo_operand is not None
        registers["Register A"] //= 2**combo_operand
    elif opcode == Ins.bxl:
        registers["Register B"] ^= operand
    elif opcode == Ins.bst:
        assert combo_operand is not None
        registers["Register B"] = combo_operand % 8
    elif opcode == Ins.jnz:
        if registers["Register A"] != 0:
            pointer = operand
    elif opcode == Ins.bxc:
        registers["Register B"] ^= registers["Register C"]
    elif opcode == Ins.out:
        assert combo_operand is not None
        output = combo_operand % 8
    elif opcode == Ins.bdv:
        assert combo_operand is not None
        registers["Register B"] = registers["Register A"] // (2**combo_operand)
    elif opcode == Ins.cdv:
        assert combo_operand is not None
        registers["Register C"] = registers["Register A"] // (2**combo_operand)

    return registers, pointer, output


def run_program(registers: dict[str, int], instructions: tuple[int]) -> tuple[int]:
    output = []

    pointer = 0

    while pointer is not None:
        opcode = instructions[pointer]
        operand = instructions[pointer + 1]

        registers, pointer, output_value = compute_instruction(opcode, operand, registers, pointer)

        if output_value is not None:
            output.append(output_value)

        if pointer >= len(instructions):
            break
    return tuple(output)


def process(input: tuple[dict[str, int], tuple[int]]) -> int:
    registers, instructions = input

    # Couldn't crack this one, so took inspiration from reddit. Implemented this very nice algorithm:
    # https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2glx6y/
    target = instructions[::-1]

    def find_a(a=0, depth=0):
        if depth == len(target):
            return a
        for i in range(8):
            output = run_program({"Register A": a * 8 + i, "Register B": 0, "Register C": 0}, instructions)
            if output and output[0] == target[depth]:
                if result := find_a((a * 8 + i), depth + 1):
                    return result
        return 0

    return find_a()


def parse_input(input: str) -> tuple[dict[str, int], tuple[int]]:
    # Register A: 729
    # Register B: 0
    # Register C: 0
    #
    # Program: 0,1,5,4,3,0
    registers, program = tools.str_to_two_sections(input)

    _, instructions = program.split(" ", 1)

    instructions = tools.item_split(instructions, ",", int)

    registers = tools.str_to_lines(registers, process_line=tools.key_value_split_dict, process_line_kwargs={"separator": ": ", "process_value": int})

    flattened_registers = dict(ChainMap(*registers))

    return flattened_registers, instructions


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/17_1.txt")))
