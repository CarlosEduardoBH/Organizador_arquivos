import os
import shutil


# Função para criar as pastas
def create_folder(foldername):

    if not os.path.exists(foldername):
        os.mkdir(foldername)
            
    return os.getcwd() + os.sep + foldername


# Função para Mover os arquivos
def move_file(file_name, foldername):

    if os.path.isdir(str(foldername)):
        
        for file_ in file_name:
            
            try: 
                shutil.move(file_, foldername)
               
            except:
                pass


# Função para listar tipo de extensão dos arquivos.
def extension_type(event):

    extension_type = ([f for f in os.listdir('.') if f.endswith(event)])
    return extension_type



# Extensões
extensions = ['txt','pdf','xlsb','xlsx','png','jpg','jpeg','jfif','bmp','gif','raw','mp3','json',
              'doc','docx','ppt', 'pptx','pbix','mov','mp4','avi','flv','exe','msi','tar','zip',
              'rar','gz', 'py', 'cs', 'js', 'php', 'html', 'sql', 'css'
            ]

