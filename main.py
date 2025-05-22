from utils.file_handler import (
    print_all_case_summaries,
    view_case,
    search_cases, 
    list_cases
)

def menu():
    while True:
        print("\n Digital Fingerprint -Main Menu")
        print("[1] View All Case Summaries")
        print("[2] View a Case by ID")
        print("[3] Search Cases by Keyword")
        print("[4] List All Case Filenames")
        print("[5] Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            print_all_case_summaries()
        elif choice == "2":
            case_id = input("Enter Case ID (e.g., 0002): ").strip()
            view_case(case_id)
        elif choice == "3":
            keyword = input("Enter keyword to search: ").strip()
            search_cases(keyword)
        elif choice == "4":
            print("\n Available Case Files:")
            for f in list_cases():
                print(f"- {f}")
        elif choice == "5":
            print("Exiting. Stay sharp.")
            break
        else:
            print("Invalid choice. Try again")
if __name__ == "__main__":
    menu()