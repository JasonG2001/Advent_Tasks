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
    for line in file:

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
    return dict(zip(monkeys, rules))


def convert_to_queue(file: List[str]) -> Dict[str, Dict[str, Union[queue, str]]]:

    monkey_rules: Dict[str, str] = make_monkey_rules(file)

    rules: Dict[str]
    for rules in monkey_rules.values():
        list_of_worry_level: List[int] = [int(number) for number in rules["Starting items"].split(",")]

        rules["Starting items"] = queue(list_of_worry_level)
    return monkey_rules


def make_inspections_dict(monkey_rules: Dict[str, Dict[str, Union[queue, str]]]) -> Dict[str, int]:

    inspections: Dict[str, int] = {monkey:0 for monkey in monkey_rules}
    return inspections


def get_outcome(monkey_rules: Dict[str, Dict[str, Union[queue, str]]],
    inspections: Dict[str, int], number_of_rounds: int, current_rounds: int = 0) -> Dict[str, int]:

    if current_rounds == number_of_rounds:
        return inspections
    
    monkey: str
    rules: Dict[str, Union[queue, str]]
    for monkey, rules in monkey_rules.items():

        starting_items: queue = rules["Starting items"]
        operation: str = rules["Operation"][11]
        factor: int = int(rules["Operation"][13:])
        dividing_term: int = int(rules["Test"][14:])
        monkey_receiving_when_true: str = rules["If true"][-1]
        monkey_receiving_when_false: str = rules["If false"][-1]

        for _ in range(len(starting_items)):
            inspected_item: int = starting_items.popleft()
            
            if factor == "old":
                factor: int = inspected_item
            if operation == "+":
                inspected_item += factor
            else:
                inspected_item *= factor

            inspected_item //= 3

            if inspected_item % dividing_term == 0:
                monkey_rules[monkey_receiving_when_true]["Starting items"].append(inspected_item)
            else:
                monkey_rules[monkey_receiving_when_false]["Starting items"].append(inspected_item)

            inspections[monkey] + 1


        current_rounds += 1

        return get_outcome(monkey_rules, inspections, number_of_rounds, current_rounds)


if __name__ == "__main__":
    file: List[str] = open_file("day11.txt")
    monkey_rules: Dict[str, Dict[str, Union[queue, str]]] = convert_to_queue(file)
    #inspection_dict: Dict[str, int] = make_inspections_dict(monkey_rules)
    inspection_dict: Dict[str, int] = defaultdict(int)
    print(get_outcome(monkey_rules, inspection_dict, 20))

    
