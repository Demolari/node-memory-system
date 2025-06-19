from tools.tag_manager import TagManager

# Ścieżka do bazy tagów
TAG_DB_PATH = "memory/tags.json"  # dostosuj jeśli masz inną lokalizację

def main():
    tag = input("🔍 Enter tag to search for:\n> ").strip().lower()

    tm = TagManager(TAG_DB_PATH)
    nodes = tm.get_nodes_by_tag(tag)

    if nodes:
        print(f"\n📌 Nodes with tag '{tag}':")
        for nid in nodes:
            print(f"- {nid}")
    else:
        print(f"\n⚠️ No nodes found with tag '{tag}'.")

if __name__ == "__main__":
    main()
