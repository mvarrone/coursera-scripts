import os
import time
import json


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def create_readme(folder_path, content=""):
    """Crea un archivo README.md en la carpeta especificada con el contenido proporcionado."""
    readme_path = os.path.join(folder_path, 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write(content)


def extract_item_names(item_ids, items_data):
    """Extrae los nombres de los items dados los itemIds."""
    item_names = []
    for item_id in item_ids:
        for item in items_data:
            if item['id'] == item_id:
                item_names.append(item['name'])
                break
    return item_names


def get_week_description(week_id, modules_data):
    """Devuelve la descripción de una semana basado en su id en los módulos."""
    for module in modules_data:
        if module['id'] == week_id:
            return module.get('description', 'No description available.')
    return 'No description available.'


def create_folders(data, json_file_path):
    # Mapeo de los módulos a las semanas
    week_mapping: dict[str, str] = {
        'JDY2Z': 'week1',
        'Rc4jY': 'week2',
        'ayKfw': 'week3'
    }

    print(json_file_path)

    basename = os.path.basename(json_file_path)  # Extracts 'course1.json'
    print(basename)

    name_only = os.path.splitext(basename)[0]  # Removes the file extension
    print(name_only)  # Output: 'course1'

    # Crea la carpeta raíz 'course' con un README.md vacío
    # root_folder = 'course1'
    root_folder = name_only
    os.makedirs(root_folder, exist_ok=True)
    create_readme(root_folder)  # README vacío en course

    # Datos de los módulos para extraer descripciones
    modules_data = data['linked']['onDemandCourseMaterialModules.v1']

    # Crea las subcarpetas week1, week2, week3 y sus README con las descripciones
    for module_id, week in week_mapping.items():
        week_folder = os.path.join(root_folder, week)
        os.makedirs(week_folder, exist_ok=True)
        description = get_week_description(module_id, modules_data)
        # README con la descripción de la semana
        create_readme(week_folder, description)

    # Contadores para las lecciones de cada semana
    lesson_counters = {'week1': 1, 'week2': 1, 'week3': 1}

    # Extraemos los items para facilitar la búsqueda
    items_data = data['linked']['onDemandCourseMaterialItems.v2']

    # Itera sobre las lecciones y crea las carpetas dentro de las semanas correspondientes
    for lesson in data['linked']['onDemandCourseMaterialLessons.v1']:
        module_id = lesson['moduleId']
        if module_id in week_mapping:
            week_folder = week_mapping[module_id]
            lesson_number = lesson_counters[week_folder]
            # Formato 01, 02, 03...
            formatted_lesson_number = f"{lesson_number:02}"
            lesson_folder = os.path.join(root_folder, week_folder, f"{
                                         formatted_lesson_number}-{lesson['slug']}")
            os.makedirs(lesson_folder, exist_ok=True)

            # Obtener los itemIds de la lección
            item_ids = lesson.get('itemIds', [])
            # Extraer los nombres de los items correspondientes a los itemIds
            item_names = extract_item_names(item_ids, items_data)
            # Crear README.md con las secciones de '## informacion' por cada item encontrado
            create_readme(lesson_folder, '\n\n'.join(
                [f'## {name}' for name in item_names]))

            print(f"Carpeta creada: {lesson_folder}")
            lesson_counters[week_folder] += 1


def main():
    # Reemplaza esto con la ruta real de tu archivo JSON
    json_file_path = './course2.json'

    data = load_json(json_file_path)
    create_folders(data, json_file_path)


if __name__ == "__main__":
    start = time.time()

    main()

    total = (time.time() - start) * 1000
    print(f"\nElapsed time: {total:.2f} ms")
