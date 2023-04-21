import json
import re

#data pulled from uberduck api https://api.uberduck.ai/voices?mode=tts-all 03/31/2023

#load json file into data variable
with open("voices.json","r",encoding="utf-8") as f:
    data = json.load(f) 

def clean_filename(filename):
    # Replace any unacceptable characters with an underscore
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

category_files = {}

for entry in data:
    category = entry["category"]
    name = entry["name"]

    cleaned_category = clean_filename(category)

    if cleaned_category not in category_files:
        category_files[cleaned_category] = open(f"{cleaned_category}.txt", "w")

    category_files[cleaned_category].write(f"{name}\n")

for file in category_files.values():
    file.close()