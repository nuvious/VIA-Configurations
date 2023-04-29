import json

MK47_FILENAME = 'mk47.layout.json'
TECHNIK_O_FILENAME = 'technik_o.layout.json'


if __name__ == "__main__":
    # Use the MK47 as the base
    with open(MK47_FILENAME, 'r') as f:
        mk47_layout = json.load(f)
        
    with open(TECHNIK_O_FILENAME, 'r') as f:
        technik_layout = json.load(f)
    
    technik_layout["layers"] = mk47_layout["layers"]
    # Technik has two keys for space instead of 1 for the MK47 so make the
    # 43rd key KC_SPC as well to make the layouts the same.
    technik_layout["layers"][0][42] = "KC_SPC"
    
    with open(TECHNIK_O_FILENAME, 'w') as technik_f:
        json.dump(technik_layout, technik_f, indent=True)
