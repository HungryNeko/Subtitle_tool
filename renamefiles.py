import os
import re
import shutil
from tempfile import mkdtemp

def natural_key(s):
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split(r'(\d+)', s)]

def rename_files_sorted(directory):

    files = [f for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f)) and not f.startswith('.')]
    
    ass=[]
    vid=[]
    temp_dir = mkdtemp()
    video_exts = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv',
              '.webm', '.m4v', '.3gp', '.mpg', '.mpeg', '.rmvb', '.ts', '.vob')
    subtitle_exts = ('.srt', '.ass', '.ssa', '.vtt', '.txt')
    try:

        for filename in files:
            if filename.lower().endswith(subtitle_exts):
                ass.append(filename)
                src = os.path.join(directory, filename)
                dst = os.path.join(temp_dir, filename)
                shutil.move(src, dst)
            elif filename.lower().endswith(video_exts):
                vid.append(filename)
            

        ass.sort(key=natural_key)
        vid.sort(key=natural_key)
        

        for index, filename in enumerate(ass):

            name, ext = os.path.splitext(filename)
            

            new_name = f"{vid[index]}{ext}"
            new_path = os.path.join(directory, new_name)
            

            if os.path.exists(new_path):
                raise ValueError(f"target file {new_name} already exists, stop")
            

            src = os.path.join(temp_dir, filename)
            shutil.move(src, new_path)
            print(f"rename: {filename} -> {new_name}")
            
            
    finally:

        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

if __name__ == "__main__":

    path = input("Input file absolute path").strip().strip("'").strip('"')
    target_directory = os.path.abspath(path)


    confirm = input(f"Sure to rename files under {target_directory}? (y/n): ")
    if confirm.lower() == 'y':
        try:
            rename_files_sorted(target_directory)
            print("Done")
        except Exception as e:
            print(f"Error{str(e)}")
    else:
        print("halted by user")
