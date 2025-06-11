from tools.tag_suggester_utils import suggest_tags
from tools.synonym_base import normalize_tag
if __name__ == "__main__":
    user_input = input("🧠 Describe your node content:\n> ")
    tags = suggest_tags(user_input)
    normalized = [normalize_tag(tag) for tag in tags]
    print("\n🏷️ Suggested Tags:", normalized)