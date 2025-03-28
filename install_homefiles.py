import os
import pathlib
import shutil

file_dir = pathlib.Path(__file__).parent.resolve()
home = pathlib.Path(os.getenv('HOME')).resolve()
source_dir = file_dir / 'home'

def copy_with_replace(src, dst):
    try:
        if src.is_dir():
            if not dst.exists():
                dst.mkdir(parents=True)
            for item in src.iterdir():
                copy_with_replace(item, dst / item.name)
        else:
            shutil.copy2(src, dst, follow_symlinks=False)
    except Exception as e:
        print(f"Ошибка при копировании {src} -> {dst}: {e}")

if source_dir.exists():
    # Копируем всё содержимое с заменой
    for item in source_dir.iterdir():
        copy_with_replace(item, home / item.name)
    
    # Удаляем исходники
    shutil.rmtree(source_dir, ignore_errors=True)
