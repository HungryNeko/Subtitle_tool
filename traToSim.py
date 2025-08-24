import os
from zhconv import convert  # 需要安装zhconv库：pip install zhconv


def convert_traditional_to_simple(src_folder, dst_folder):
    """
    将源文件夹中的繁体字幕转换为简体字幕

    :param src_folder: 源文件夹路径(包含繁体字幕)
    :param dst_folder: 目标文件夹路径(将保存简体字幕)
    """
    # 确保目标文件夹存在
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # 支持的字幕文件扩展名
    subtitle_exts = ('.srt', '.ass', '.ssa', '.vtt', '.txt')

    # 遍历源文件夹
    for filename in os.listdir(src_folder):
        if filename.startswith('.') or filename.startswith('._'):
            continue
        # 检查是否是字幕文件
        if filename.lower().endswith(subtitle_exts):
            src_path = os.path.join(src_folder, filename)
            dst_path = os.path.join(dst_folder, filename)

            try:
                # 读取繁体字幕文件
                with open(src_path, 'r', encoding='utf-8') as f:
                    traditional_content = f.read()

                # 转换为简体中文
                simplified_content = convert(traditional_content, 'zh-cn')

                # 写入简体字幕文件
                with open(dst_path, 'w', encoding='utf-8') as f:
                    f.write(simplified_content)

                print(f"succeed: {filename}")

            except Exception as e:
                print(f"Failed {filename}: {str(e)}")


if __name__ == '__main__':
    source_folder = input('Source Folder: ').strip().strip("'").strip('"')
    destination_folder = input('Destination Folder: ').strip().strip("'").strip('"')

    source_folder = os.path.abspath(source_folder)
    destination_folder = os.path.abspath(destination_folder)

    if not os.path.exists(source_folder):
        print(f"Source not exist: {source_folder}")
    else:
        run = input('Run? (y/n): ')
        if run.lower() == 'y':
            convert_traditional_to_simple(source_folder, destination_folder)
            print("Done.")
        else:
            print("Cancelled.")
