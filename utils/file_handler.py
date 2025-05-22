import json 
import os 

def save_case(case_data, filename, folder="case_data"):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    with open(filepath, "w") as f: 
        json.dump(case_data, f, indent=4)
    print(f"[+] Case saved to {filepath}")

def load_case(filename, folder="case_data"):
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        print(f"[!] File {filepath} not found.")
        return None
    with open(filepath, "r") as f:
        return json.load(f)


def list_cases(folder="case_data"):
    return [f for f in os.listdir(folder) if f.endswith(".json")]

def view_case(case_id_or_filename):
    """
    Load and display case content by case ID or filename.
    """
    from pprint import pprint 
    if not case_id_or_filename.endswith(".json"):
        case_id_or_filename = f"case_{case_id_or_filename}.json"
    try: 
        case = load_case(case_id_or_filename)
        pprint(case)
    except FileNotFoundError:
        print(f" Case '{case_id_or_filename}' not found.")


def search_cases(keyword): 
    """
    Search all cases for a keyword in title, MO, or notes.
    """
    keyword = keyword.lower()
    matches = []
    for filename in list_cases():
        case = load_case(filename)
        if (
            keyword in case.get("title", "").lower()
            or any(keyword in mo.lower() for mo in case.get("modi_operandi", []))
            or keyword in case.get("notes", "").lower()
        ):
            matches.append((filename, case["title"]))
    
    if matches: 
        print(f" Found {len(matches)} match(es):")
        for file, title in matches: 
            print(f" - {file}: {title}")
    else: 
        print("No mathces found.")


def print_all_case_summaries():
    """
    Load and print a summary of all saved cases.
    """
    print("All Case Summaries:\n")
    for filename in list_cases():
        try: 
            case = load_case(filename)
            print(f"  {case.get('case_id')} | {case.get('title')}")
            print(f"   Date: {case.get('date')}")
            print(f"   Location: {case.get('location')}")
            print(f"   Status: {case.get('status')}")
            suspects = case.get('suspects', [])
            print(f"   Suspects: {', '.join(suspects) if suspects else 'None'}")
            print("-" * 50)
        except Exception as e:
            print(f"Could not load {filename}: {e}")