import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
SMTH_OTHER = []
ARCHIVES = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'ZIP': ARCHIVES,
    'GZ' : ARCHIVES,
    'TAR': ARCHIVES,

}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename):
    return Path(filename).suffix[1:].upper()    # прибрали крапку для розширення


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():  # Якщо це папка то додаємо її зі списку FOLDERS і переходимо до наступного елемента папки
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'SMTH_OTHER'):   # перевіряємо, щоб папка не була тією, в яку ми складаємо вже файли.
                FOLDERS.append(item)
                scan(item) # скануємо цю вкладену папку - рекурсія

            continue # перейти до наступного елемента в сканованій папці

        ext = get_extension(item.name)  # взяли розширення
        full_way = folder / item.name  # взяли ПОВНИЙ шлях до файлу
        if not ext:  # якщо файл не має розширення:
            SMTH_OTHER.append(full_way) #додати до невідомих

        else:
            try:
                # взяти список куди покласти повний шлях до файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(full_way)
            except KeyError:
                # Якщо ми не реєстрували розширення у REGISTER_EXTENSIONS, то додати до іншого
                UNKNOWN.add(ext)
                SMTH_OTHER.append(full_way)

if __name__ == '__main__':

    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Archives: {ARCHIVES}')

    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')

    print(FOLDERS[::-1])