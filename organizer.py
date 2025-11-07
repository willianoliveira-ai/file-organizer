import os
import shutil

# Pasta que será organizada
folder_path = r"C:\Users\SEU_USUARIO\Downloads"  # Troque pelo caminho da sua pasta

# Tipos de arquivos e destinos
file_types = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mp4", ".mov", ".avi"],
    "Compactados": [".zip", ".rar"],
    "Executáveis": [".exe", ".msi"],
}

def organize_files(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)

            moved = False
            for folder, extensions in file_types.items():
                if extension.lower() in extensions:
                    folder_path = os.path.join(path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, folder_path)
                    print(f"Movido: {file} → {folder}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(path, "Outros")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, other_folder)
                print(f"Movido: {file} → Outros")

if __name__ == "__main__":
    organize_files(folder_path)
    print("\nOrganização concluída!")
