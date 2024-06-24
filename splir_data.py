import os
import shutil
import random

# Orijinal veri seti yolu
dataset_path = "..."
# Bölünecek klasörlerin yolları
part1_path = "..."
part2_path = "...."


# Eğer klasörler yoksa oluştur
os.makedirs(part1_path, exist_ok=True)
os.makedirs(part2_path, exist_ok=True)

# Klasör isimleri
class_names = ["1", "2", "3", "4"]

# Dosya yollarını kontrol et
print(f"Checking dataset path: {dataset_path}")
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset path does not exist: {dataset_path}")

# Her sınıf için işlemi tekrarla
for class_name in class_names:
    class_path = os.path.join(dataset_path, class_name)
    
    # Klasörün var olup olmadığını kontrol et
    print(f"Checking class path: {class_path}")
    if not os.path.exists(class_path):
        print(f"Error: Directory {class_path} does not exist.")
        continue
    
    files = os.listdir(class_path)
    
    # Dosyaları karıştır
    random.shuffle(files)
    
    # Dosyaları ikiye böl
    half = len(files) // 2
    part1_files = files[:half]
    part2_files = files[half:]
    
    # Sınıf için yeni klasörler oluştur
    os.makedirs(os.path.join(part1_path, class_name), exist_ok=True)
    os.makedirs(os.path.join(part2_path, class_name), exist_ok=True)
    
    # Dosyaları yeni klasörlere kopyala
    for file_name in part1_files:
        src_file = os.path.join(class_path, file_name)
        dest_file = os.path.join(part1_path, class_name, file_name)
        shutil.copy(src_file, dest_file)
    
    for file_name in part2_files:
        src_file = os.path.join(class_path, file_name)
        dest_file = os.path.join(part2_path, class_name, file_name)
        shutil.copy(src_file, dest_file)

print("Veri seti başarıyla ikiye bölündü.")



