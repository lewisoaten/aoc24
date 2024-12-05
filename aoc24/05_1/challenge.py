from collections import defaultdict

from .. import tools


def check_ordering(pages: list[str], pages_before: dict[set[int]]):
    seen_pages = set()
    print(f"Starting check_ordering with pages: {pages}, pages_before: {pages_before}")
    for page in pages:
        for page_before in pages_before[page]:
            if page_before in pages and page_before not in seen_pages:
                return False
        seen_pages.add(page)

    return True


def get_middle(pages: list[int]):
    return pages[int((len(pages) - 1) / 2)]


def process(input: list[int]):
    ordering_rules, updates = input

    pages_before = defaultdict(set)
    for line in ordering_rules.splitlines():
        before, after = line.split("|")
        pages_before[int(after)].add(int(before))

    updates = [[int(page) for page in line.split(",")] for line in updates.splitlines()]

    answer = 0
    for update in updates:
        if check_ordering(update, pages_before):
            answer += get_middle(update)

    return answer


def challenge():
    return process(tools.read_to_two_sections("./inputs/05_1.txt"))
