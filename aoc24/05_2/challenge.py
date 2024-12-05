from collections import defaultdict
from functools import cmp_to_key

from .. import tools


pages_before = defaultdict(set)


def check_ordering(pages: list[str], pages_before: dict[set[int]]):
    seen_pages = set()
    for page in pages:
        for page_before in pages_before[page]:
            if page_before in pages and page_before not in seen_pages:
                return False
        seen_pages.add(page)

    return True


def get_middle(pages: list[int]):
    return pages[int((len(pages) - 1) / 2)]


def compare_pages(page1: int, page2: int) -> int:
    if page1 in pages_before[page2]:
        print(f"Found {page1} before {page2}")
        return -1
    elif page2 in pages_before[page1]:
        print(f"Found {page2} before {page1}")
        return 1
    print(f"Found no rule for {page1} and {page2} in pages_before: {pages_before}")
    return 0


def process(input: list[int]):
    ordering_rules, updates = input

    for line in ordering_rules.splitlines():
        before, after = line.split("|")
        pages_before[int(after)].add(int(before))

    updates = [[int(page) for page in line.split(",")] for line in updates.splitlines()]

    answer = 0
    for update in updates:
        if not check_ordering(update, pages_before):
            print(f"Found invalid order: {update}")
            update = sorted(update, key=cmp_to_key(compare_pages))
            print(f"Fixed order: {update}")
            answer += get_middle(update)

    return answer


def challenge():
    return process(tools.read_to_two_sections("./inputs/05_1.txt"))
