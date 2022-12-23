import os
import yaml
import logging

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

OUTPUT_PATH = config['output_dir'] + config['output_filename']
BASE_PATH = config['source_path']

masks_raw = config['masks']
masks = {}
for mask in masks_raw:
    braced_mask = '[' + mask + ']'
    masks.update({braced_mask: masks_raw[mask]})

for k in masks:
    print(k)
    print(masks[k])

# Global static

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
    replaced = replace_keywords(base, masks)
    write_to_file(OUTPUT_PATH, replaced)