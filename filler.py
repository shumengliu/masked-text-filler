import os

# Change those field to generate a new letter
OUTPUT_PATH = "./output/cover-letter-personify.txt"
JOB_TITLE = "Java Software Engineer"
COMPANY_NAME = "Personify"

# Map tokens to variables
ENTITY_MAP = {
    '[Job Title]': JOB_TITLE,
    '[Company Name]': COMPANY_NAME,
}


# Global static
BASE_PATH = "cover-letter-base.txt"



def get_base_text() -> str:
    with open(BASE_PATH, 'r') as f:
        text = f.read()
        return text

def replace_keywords(text, entity_map):
    for placeholder in entity_map:
        actual = entity_map[placeholder]
        text = text.replace(placeholder, actual)
    return text

def write_to_file(path, content):
    with open(path, 'w') as f:
        print(content)
        f.seek(0)
        text = f.write(content)
        f.truncate()
        return text

if __name__ == "__main__":
    base = get_base_text()
    replaced = replace_keywords(base, ENTITY_MAP)
    write_to_file(OUTPUT_PATH, replaced)