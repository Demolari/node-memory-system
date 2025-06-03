## ✅ **📂 `docs/` – Dokumentacja i koncepcje**

| Status | Plik                     | Opis                                                                   |
| ------ | ------------------------ | ---------------------------------------------------------------------- |
| ✅      | `README.md`              | Główne wprowadzenie, struktura projektu                                |
| ✅      | `node-memory.md`         | Opis systemu węzłowej pamięci i struktury nodów (wcześniej `nodes.md`) |
| ✅      | `architecture.md`        | Architektura całego systemu i relacje między komponentami              |
| ⏳      | `usage.md`               | Przykładowe use-casy, jak system może być wykorzystywany               |
| ⏳      | `tagging.md`             | Zasady tagowania i zarządzania tagami w węzłach                        |
| ⏳      | `reinforcement.md`       | Opis systemu wzmacniania nodów (np. przez częste użycie)               |
| ⏳      | `rag-integration.md`     | Integracja z RAG: retrieval i rekontekstualizacja                      |
| ⏳      | `conversation-format.md` | Format zapisu rozmów, np. JSON z metadanymi                            |
| ❌      | `vision.md`              | Odrzucone – obecnie niepotrzebne                                       |

---

## 🧠 **📂 `memory/` – Logika i dane pamięci**

| Status | Plik                  | Opis                                          |
| ------ | --------------------- | --------------------------------------------- |
| ⏳      | `memory_interface.py` | Główne API do odczytu/zapisu nodów            |
| ⏳      | `tag_manager.py`      | Narzędzie do zarządzania tagami w nodach      |
| ⏳      | `*.pkl`, `*.json`     | Pliki z embeddingami i nodami (np. do testów) |

---

## 🛠️ **📂 `tools/` – Narzędzia pomocnicze**

| Status | Plik/Funkcja          | Opis                                                           |
| ------ | --------------------- | -------------------------------------------------------------- |
| ⏳      | Generator embeddingów | Skrypt do tworzenia embeddingów tekstu/tagów                   |
| ⏳      | Wizualizacja grafu    | (Opcjonalnie) narzędzie do wizualizacji połączeń między nodami |

---

## 📦 **📂 `examples/` – Przykłady**

| Status | Plik/Funkcja         | Opis                                 |
| ------ | -------------------- | ------------------------------------ |
| ⏳      | `basic_usage.md`     | Jak korzystać z nodów i interfejsu   |
| ⏳      | `example_graph.json` | Przykładowy graf pamięci użytkownika |

---

## 📑 **📂 `spec/` – Specyfikacje i formaty**

| Status | Plik                     | Opis                                             |
| ------ | ------------------------ | ------------------------------------------------ |
| ⏳      | `conversation-schema.md` | Szczegółowa struktura plików rozmów i metadanych |
| ⏳      | `node-schema.md`         | Format nodu (klucze, wartości, możliwe typy)     |

---

## 📁 Główne pliki repozytorium

| Status | Plik               | Opis                                                         |
| ------ | ------------------ | ------------------------------------------------------------ |
| ⏳      | `.gitignore`       | Ignorowanie danych tymczasowych (embeddingi, cache)          |
| ⏳      | `requirements.txt` | Wymagane biblioteki (jeśli zajdzie potrzeba testowania kodu) |
| ❌      | `setup.py`         | Na razie niepotrzebny – nie dystrybuujemy jako pakiet        |

---

## 🔄 Proponowana **kolejność prac (do dalszego działania)**

1. ✅ **Sfinalizować `docs/`**:

   * `README.md`, `node-memory.md`, `architecture.md` – ✅
   * Następnie: `tagging.md`, `reinforcement.md`, `rag-integration.md`

2. ⏳ **Stworzyć szkielety `memory/` i `spec/`**:

   * Pusty `memory_interface.py`, `tag_manager.py`
   * Plik `node-schema.md` jako specyfikacja formatu

3. ⏳ **Stworzyć `examples/` i `tools/`**:

   * Chociażby jeden `example_graph.json`
   * Skrypt lub opis generowania embeddingów

4. ⏳ **Zająć się warstwą RAG** (na końcu):

   * `rag-integration.md`
   * Jak przeszukiwać i rekontekstualizować
