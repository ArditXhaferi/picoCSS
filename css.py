import json
import re

# Open the JSON file
with open('values.json', 'r') as f:
    styles = json.load(f)

usedKeys = []


# Open the CSS file for writing
with open('styles.css', 'w') as f:
    # Iterate through the JSON object
    for key, value in styles.items():
        # Write the class name and properties to the CSS file
        distance = 0
        realKey = ""
        keys = key.replace("/", "\/").replace(".", "\.").split("-")
        for key in keys:
            realKey += key[0]
        if realKey in usedKeys:
            keys = key.replace("/", "\/").replace(".", "\.").split("-")
            for key, index in enumerate(keys):
                if index == 0:
                    realKey += key[0:1]
        usedKeys.append(realKey)
        f.write("." + realKey + " {\n")
        pattern = r"\/\*.*\s*\*\/"

        # Replace the matched pattern with an empty string
        new_string = re.sub(pattern, "", value)
        f.write(new_string)
        f.write("}\n")

print("CSS file created successfully!")
