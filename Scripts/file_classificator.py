import os
import sys


def get_file_extension(filename):
    return os.path.splitext(filename)[1]

def main():
    path = sys.argv[1]
    formats = {
        ## Archivos texto plano
        ".txt": path + "/Text/",
        ".pdf": path + "/PDF/",

        ## Archivos paquete Office
        ".docx": path + "/Word/",
        ".ppt": path + "/PPT/",
        ".xls": path + "/Excel/",

        ## Archivos comprimidos
        ".zip": path + "/Zipped/",
        ".rar": path + "/Zipped/",

        ## Archivos de imagenes
        ".jpg": path + "/Images/",
        ".png": path + "/Images/"
    }

    for file in os.listdir(path):
        extension = get_file_extension(file)

        if extension in formats:
            if not os.path.exists(formats[extension]):
                os.mkdir(formats[extension])
            dest = formats[extension] + file
            os.rename(path + "/" + file, dest)

        else:
            if not os.path.exists(path + "/" + "Rest"):
                os.mkdir(path + "/" + "Rest")
            dest = path + "/Rest/" + file
            os.rename(path + "/" + file, dest)

if __name__ == "__main__":
    main()
