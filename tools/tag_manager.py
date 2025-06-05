import os
import json
from tools.synonym_base import normalize_tag
from tools.id_logger import log_id_event

MAX_TAGS = 5

class TagManager:
    def __init__(self, tag_db_path):
        self.tag_db_path = tag_db_path
        self.tags = self.load_tags()

    def load_tags(self):
        if os.path.exists(self.tag_db_path):
            with open(self.tag_db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_tags(self):
        with open(self.tag_db_path, 'w', encoding='utf-8') as f:
            json.dump(self.tags, f, indent=2)

    def validate_tag(self, tag):
        tag = normalize_tag(tag)
        return tag if tag else None

    def add_tags_to_node(self, node_id, proposed_tags):
        added_tags = []

        for tag in proposed_tags:
            if len(added_tags) >= MAX_TAGS:
                break

            valid_tag = self.validate_tag(tag)
            if valid_tag and valid_tag not in added_tags:
                added_tags.append(valid_tag)
                if valid_tag not in self.tags:
                    self.tags[valid_tag] = []
                if node_id not in self.tags[valid_tag]:
                    self.tags[valid_tag].append(node_id)

        self.save_tags()
        self.log_tagging(node_id, added_tags)
        return added_tags

    def log_tagging(self, node_id, tags):
        message = f"Tagged node {node_id} with: {', '.join(tags)}"
        log_id_event(node_id, message)
