import os
import re

# Шлях до вашого проєкту
project_path = "path\\"
requirements_path = "path\\requirements.txt"
output_file_path = "path\\unused_libraries.txt"

# Читаємо список бібліотек із requirements.txt
def get_libraries(requirements_path):
    with open(requirements_path, "r", encoding="utf-8") as f:
        return [line.split("==")[0] for line in f.readlines() if line.strip()]


# Функція для перевірки використання бібліотек
def find_library_usage(lib, path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as code_file:
                        if re.search(fr"\b{lib}\b", code_file.read()):
                            return True
                except Exception as e:
                    print(f"Error reading file {file}: {e}")
    return False


# Аналіз бібліотек
def analyze_libraries():
    libraries = get_libraries(requirements_path)
    unused_libraries = []
    
    for lib in libraries:
        if not find_library_usage(lib, project_path):
            unused_libraries.append(lib)

    return unused_libraries

# Запис результатів у файл
def write_results_to_file(unused_libraries, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(unused_libraries))

if __name__ == "__main__":
    unused_libraries = analyze_libraries()

    write_results_to_file(unused_libraries, output_file_path)
    print(f"Аналіз завершено. Результати збережено у файлі: {output_file_path}")
