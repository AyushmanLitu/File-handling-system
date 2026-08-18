from pathlib import Path
import shutil

givenFolder = Path("../The file")

file_catagories = {
    ".jpeg" : "Photos",
    ".png" : "Photos",
    ".jpg" : "Photos",
    ".img" : "Photos",

    ".mp3" : "Musics",
    ".wav" : "Musics",
    
    ".mp4" : "Videos",

    ".txt" : "Documents",
    ".pdf" : "Documents",
    ".docs" : "Documents",
}

which_files = []
for items in givenFolder.iterdir():

    extension = items.suffix.lower()

    if extension not in file_catagories:
        print(f"Skipped {items}")
        continue

    if extension in file_catagories.keys():
        folder_name = file_catagories.get(extension)
        destination_dir = givenFolder/ folder_name
        destination_dir.mkdir(parents=True,exist_ok=True)
        shutil.move(items,destination_dir)
        print(f"{items.stem} -> {folder_name}")
    else:
        print("This can't get into any folders")
