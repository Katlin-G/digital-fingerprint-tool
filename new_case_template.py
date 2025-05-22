from utils.file_handler import save_case 

case = {
    "case_id": "0004",
    "title": "Suspicious Fore at Storage Facility",
    "date": "2025-04-15",
    "location": "Riversdie Storage, Sacramento, CA",
    "description": "A fore broke out in a privately rented storage unit. No injuires reported, but contents were destroyed.",
    "modi_operandi": ["Accelerant use", "Night entry", "Remote ignition"],
    "victims": ["Storage renter - James Hoooway"],
    "suspects": ["Unknown individual spotted on nearby camera footage"],
    "status": "open",
    "evidence": ["Gasoline traces", "Surveillance footage", "Burn pattern"],
    "notes": "Fire inspector believes fire was deliberate. May be connected to insurance fraud." 
}

filename = f"case_{case['case_id']}.json"
save_case(case, filename)
print(f" Case {case['case_id']} saved.")



### How to Use it 
### Open new_case_template.py 
### Update the case dictionary values
### Run it --> python new_case_template.py 
### This will auto-save the new case into your /cases foilr using the filename pattern case_000x.json