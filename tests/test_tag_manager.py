import unittest import tempfile import os import json from memory.tag_manager import TagManager

class TestTagManager(unittest.TestCase): def setUp(self): self.temp_dir = tempfile.TemporaryDirectory() self.tag_db_path = os.path.join(self.temp_dir.name, 'tags.json')

def tearDown(self):
    self.temp_dir.cleanup()

def test_add_valid_tags(self):
    tag_manager = TagManager(self.tag_db_path)
    tags = ["memory", "context"]
    added_tags = tag_manager.add_tags_to_node("node-1", tags)
    self.assertEqual(set(added_tags), set(tags))

    with open(self.tag_db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        self.assertIn("memory", data)
        self.assertIn("context", data)
        self.assertIn("node-1", data["memory"])

def test_add_tags_with_duplicates_and_case_insensitivity(self):
    tag_manager = TagManager(self.tag_db_path)
    tags = ["Memory", "memory", "MEMORY", "Context"]
    added_tags = tag_manager.add_tags_to_node("node-2", tags)
    self.assertIn("memory", added_tags)
    self.assertIn("context", added_tags)
    self.assertEqual(len(added_tags), 2)

def test_max_tags_limit(self):
    tag_manager = TagManager(self.tag_db_path)
    tags = [f"tag{i}" for i in range(10)]
    added_tags = tag_manager.add_tags_to_node("node-3", tags)
    self.assertEqual(len(added_tags), 5)

def test_add_tags_to_same_node_twice(self):
    tag_manager = TagManager(self.tag_db_path)
    tags = ["tag"]
    added_once = tag_manager.add_tags_to_node("node-4", tags)
    added_again = tag_manager.add_tags_to_node("node-4", tags)
    self.assertEqual(added_once, ["tag"])
    self.assertEqual(added_again, ["tag"])

def test_add_tags_empty_input(self):
    tag_manager = TagManager(self.tag_db_path)
    added_tags = tag_manager.add_tags_to_node("node-5", [])
    self.assertEqual(added_tags, [])

def test_add_tags_invalid_entries(self):
    tag_manager = TagManager(self.tag_db_path)
    tags = ["   ", "", "@@@@", "valid_tag"]
    added_tags = tag_manager.add_tags_to_node("node-6", tags)
    self.assertEqual(added_tags, ["valid_tag"])

if name == 'main': unittest.main()

