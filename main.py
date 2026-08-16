import json
from drop_table import DropTable
from case import Case
from opener import CaseOpener

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_data():
    rarities = load_json("data/rarities.json")
    knives = load_json("data/knives.json")
    cases = load_json("data/cases.json")
    return rarities, knives, cases

def build_cases(rarities, knives, cases_data):
    case_objects = {}
    for case_name, case_info in cases_data.items():
        drop_table = DropTable(case_info["rarity_odds"])
        knife_pool = [knives[k] for k in case_info["knife_pool"]]
        case_objects[case_name] = Case(case_name, drop_table, knife_pool)
    return case_objects

def main():
    rarities, knives, cases_data = load_data()
    cases = build_cases(rarities, knives, cases_data)

    opener = CaseOpener()

    print("Available Cases:")
    for c in cases:
        print(f"- {c}")

    choice = input("Choose a case to open: ")

    if choice not in cases:
        print("Invalid case.")
        return

    result = opener.open_case(cases[choice])
    print("\n🎉 You unboxed:")
    print(f"Knife: {result['name']}")
    print(f"Category: {result['category']}")
    print(f"Rarity: {result['rarity']}")

if __name__ == "__main__":
    main()
