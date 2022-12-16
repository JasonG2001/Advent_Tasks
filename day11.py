from collections import defaultdict, deque as queue
from typing import Dict, List, Union


def open_file(file_name: str) -> List[str]:
    with open(file_name) as f:
        lines: List[str] = [line.strip() for line in f]

    return lines


def make_monkey_rules(file: List[str]) -> Dict[str, Dict[str, str]]:

    rule: Dict[str, str] = {}
    monkeys: List[str] = []
    rules: List[Dict[str, str]] = []

    line: str
    for index, line in enumerate(file):

        if len(line) == 0:
            continue

        elif "Monkey" in line:
            monkeys.append(line[7])

        else:
            description: List[str] = line.split(":")

            if description[0] in rule:
                rules.append(rule)
                rule: Dict[str, str] = {}

            rule[description[0]] = description[1]

            if file[index] == file[-1]:
                rules.append(rule) 
    return dict(zip(monkeys, rules))


def convert_to_queue(file: List[str]) -> Dict[str, Dict[str, Union[queue, str]]]:

    monkey_rules: Dict[str, str] = make_monkey_rules(file)

    rules: Dict[str]
    for rules in monkey_rules.values():
        
        items_list: List[int] = [int(number) for number in rules["Starting items"].split(",")]
        item_queue: queue = queue(items_list)

        rules["Starting items list"]: queue = item_queue

    return monkey_rules


def get_inspections(monkey_rules: Dict[str, Dict[str, Union[queue, str]]],
    inspections: Dict[str, int], number_of_rounds: int, current_rounds: int = 0) -> Dict[str, int]:

    if current_rounds == number_of_rounds:
        return inspections
    
    monkey: str
    rules: Dict[str, Union[queue, str]]
    for monkey, rules in monkey_rules.items():

        starting_items: queue = rules["Starting items list"]
        operation: str = rules["Operation"][11]
        factor: str = rules["Operation"][13:]
        dividing_term: int = int(rules["Test"][14:])
        monkey_receiving_when_true: str = rules["If true"][-1]
        monkey_receiving_when_false: str = rules["If false"][-1]

        for _ in range(len(starting_items)):
            inspected_item: int = starting_items.popleft()
            
            if factor == "old":
                factor: int = inspected_item

            if operation == "+":
                inspected_item += int(factor)
            else:
                inspected_item *= int(factor)

            inspected_item //= 3

            if inspected_item % dividing_term == 0:
                monkey_rules[monkey_receiving_when_true]["Starting items list"].append(inspected_item)
            else:
                monkey_rules[monkey_receiving_when_false]["Starting items list"].append(inspected_item)

            inspections[monkey] += 1

    current_rounds += 1

    return get_inspections(monkey_rules, inspections, number_of_rounds, current_rounds)


def get_monkey_business(inspections: Dict[str, int]) -> int:
    ordered_inspections: List[int] = sorted(inspections.values(), reverse=True)

    return ordered_inspections[0] * ordered_inspections[1]


if __name__ == "__main__":
    file: List[str] = open_file("day11.txt")
    monkey_rules: Dict[str, Dict[str, Union[queue, str]]] = convert_to_queue(file)   
    inspection_dict_template: Dict[str, int] = defaultdict(int)
    inspections = get_inspections(monkey_rules, inspection_dict_template, 20)
    print(inspections)
    monkey_business = get_monkey_business(inspections)
    print(monkey_business)

    
