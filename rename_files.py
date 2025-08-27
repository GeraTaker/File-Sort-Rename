import os
from datetime import datetime
from collections import defaultdict
#prueba
#hola
## Configuración de variables
"hola"
directory = r'D:\Descargas\Disco duro\Extras'
extension_count = defaultdict(int)
total_changes = 0
variable_name = 'exampleVariable'

## Método para organizar archivos por fecha y nombre
def get_creation_date(file_path):
    creation_time = os.path.getctime(file_path)
    return datetime.fromtimestamp(creation_time).strftime('%Y_%m_%d')

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1]
        creation_date = get_creation_date(file_path)
        new_name = f"{creation_date}_{variable_name}{ext}"
        new_path = os.path.join(directory, new_name)

        counter = 1
        base_name = f"{creation_date}_{variable_name}"
        while os.path.exists(new_path):
            new_name = f"{base_name}_{counter}{ext}"
            new_path = os.path.join(directory, new_name)
            counter += 1

        os.rename(file_path, new_path)
        total_changes += 1
        extension_count[ext] += 1

print(f"Total files renamed: {total_changes}")
for ext, count in extension_count.items():
    print(f"Extension '{ext}': {count} files renamed")
