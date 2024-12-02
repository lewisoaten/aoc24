from .. import tools


def process(input: list[list[int]]):
    safe_reports = 0
    for report in input:
        report_increasing = all((a < b and a >= b - 3) for a, b in zip(report, report[1:]))
        report_decreasing = all((a > b and a <= b + 3) for a, b in zip(report, report[1:]))

        print(f"report: {report}, increasing: {report_increasing}, decreasing: {report_decreasing}")

        if report_increasing or report_decreasing:
            safe_reports += 1
    return safe_reports


def challenge():
    return process(tools.read_to_int2d("./inputs/02_1.txt"))
