from .. import tools


def check_report(report):
    report_increasing = [(a < b and a >= b - 3) for a, b in zip(report, report[1:])]
    report_decreasing = [(a > b and a <= b + 3) for a, b in zip(report, report[1:])]

    return all(report_increasing) or all(report_decreasing), report_increasing, report_decreasing


def safe_report_after_removing_one_value(report):
    # Iterate over each combination of report after one value removed
    for i in range(len(report)):
        dampened_report = report[:i] + report[i + 1 :]  # noqa: E203
        if check_report(dampened_report)[0]:
            return True


def process(input: list[list[int]]):
    safe_reports = 0
    for report in input:
        report_increasing = [(a < b and a >= b - 3) for a, b in zip(report, report[1:])]
        report_decreasing = [(a > b and a <= b + 3) for a, b in zip(report, report[1:])]

        safe, report_increasing, report_decreasing = check_report(report)

        print(f"report: {report}, len {len(report)}, safe {safe}, increasing: {report_increasing}, decreasing: {report_decreasing}")

        if safe:
            safe_reports += 1
        elif (sum(report_increasing) >= len(report) - 3 or sum(report_decreasing) >= len(report) - 3) and safe_report_after_removing_one_value(report):
            safe_reports += 1

    return safe_reports


def challenge():
    return process(tools.read_to_int2d("./inputs/02_1.txt"))
