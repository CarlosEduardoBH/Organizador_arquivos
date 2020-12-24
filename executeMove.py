import os
import shutil
from utilitiesMove import * 



def files():

    # EXTENSIONS
    pdf  = ""
    txt  = ""
    csv  = ""
    xlsx = ""
    xlsb = ""
    xls  = ""
    png  = ""
    jpg  = ""
    bmp  = ""
    gif  = ""
    raw  = ""
    jpeg = ""
    jfif = ""
    mp3  = ""
    json = ""
    doc  = ""
    docx = ""
    ppt  = ""
    pptx = ""
    pbix = ""
    mov  = ""
    mp4  = ""
    avi  = ""
    flv  = ""
    exe  = ""
    msi  = ""
    tar  = ""
    zip_ = ""
    rar  = ""
    gz   = ""
    ipynb= ""    
    py   = ""
    cs   = ""
    js   = ""
    php  = ""
    html = ""
    sql  = "" 
    css  = ""


    # PATH FOLDERS
    path_folder_pdf   = ""
    path_folder_txt   = ""
    path_folder_excel = ""
    path_folder_img   = ""
    path_folder_mp3   = ""
    path_folder_json  = ""
    path_folder_word  = ""
    path_folder_pp    = ""
    path_folder_pbi   = ""
    path_folder_video = ""
    path_folder_exc   = ""
    path_folder_zip   = ""
    path_folder_cod   = ""
    path_folder_jupyter = ""

    for extension in extensions:
        
        # type TXT
        if extension_type('txt') != []:

            extension == 'txt'
            txt = (extension_type('txt'))
            
            path_folder_txt = (create_folder('TXT'))
            
            move_file(txt, path_folder_txt)

            
        # type PDF
        elif extension_type('pdf') != []:

            extension == 'pdf'
            pdf = (extension_type('pdf'))
            
            path_folder_pdf = (create_folder('PDF'))
            
            move_file(pdf, path_folder_pdf)


        # type MP3
        elif extension_type('mp3') != []:

            extension == 'mp3'
            mp3 = (extension_type('mp3'))
            
            path_folder_mp3 = (create_folder('MP3'))
            
            move_file(mp3, path_folder_mp3)


        # type json
        elif extension_type('json') != []:

            extension == 'json'
            json = (extension_type('json'))
           
            path_folder_json = (create_folder('JSON'))
           
            move_file(json, path_folder_json)


        # type POWER BI
        elif extension_type('pbix') != []:

            extension == 'pbix'
            pbix = (extension_type('pbix'))
            
            path_folder_pbi = (create_folder('POWER BI'))
            
            move_file(pbix, path_folder_pbi)


        # type IMAGENS
        if extension in('png', 'jpg', 'bmp', 'gif', 'raw','jpeg','jfif'):
            
            if extension_type(extension) != []:

                png  = extension_type('png')
                jpg  = extension_type('jpg')
                bmp  = extension_type('bmp')
                gif  = extension_type('gif')
                raw  = extension_type('raw')
                jpeg = extension_type('jpeg')
                jfif = extension_type('jfif')
                            
                path_folder_img = (create_folder('IMAGENS'))
    
        
        # type EXCEL
        
        if extension in('xlsb', 'csv','xlsx', 'xls'):

            if extension_type(extension) != []:
            
                xlsb = extension_type('xlsb')
                csv  = extension_type('csv')
                xlsx = extension_type('xlsx')
                xls  = extension_type('xls')
                
                path_folder_excel = create_folder('EXCEL')

        
        # type WORD
        if extension in('doc', 'docx'):

            if extension_type(extension) != []:
            
                doc  = extension_type('doc')
                docx = extension_type('docx')
                
                path_folder_word = create_folder('WORD')    
        
        
        # type POWER POINT
        if extension in('ppt', 'pptx'):

            if extension_type(extension) != []:
            
                ppt  = extension_type('ppt')
                pptx = extension_type('pptx')
                
                path_folder_pp = create_folder('POWER POINT') 

        
        # type VIDEO
        if extension in('mov', 'mp4', 'avi', 'flv'):

            if extension_type(extension) != []:
            
                mov = extension_type('mov')
                mp4 = extension_type('mp4')
                avi = extension_type('avi')
                flv = extension_type('flv')
                
                path_folder_video = create_folder('VIDEO') 


        # type EXECUTAVEL
        if extension in('exe', 'msi'):

            if extension_type(extension) != []:
            
                exe = extension_type('exe')
                msi = extension_type('msi')
                
                path_folder_exc = create_folder('EXECUTAVEL') 


        # type ZIP
        if extension in('tar', 'zip','rar','gz'):

            if extension_type(extension) != []:
            
                tar   = extension_type('tar')
                zip_  = extension_type('zip')
                rar   = extension_type('rar')
                gz    = extension_type('gz')
                
                path_folder_zip = create_folder('ZIP') 


        # type JUPYTER NOTEBOOK
        elif extension_type('ipynb') != []:

            extension == 'ipynb'
            ipynb = (extension_type('ipynb'))

            path_folder_jupyter = (create_folder('JUPYTER NOTEBOOK'))

            move_file(ipynb, path_folder_jupyter)


        # type CODIGO
        if extension in('py', 'cs', 'js', 'php', 'html', 'sql', 'css'):

            if extension_type(extension) != []:
            
                py   = extension_type('py')
                cs   = extension_type('cs')
                js   = extension_type('js')
                php  = extension_type('php')
                html = extension_type('html')
                sql  = extension_type('sql')
                css  = extension_type('css')
               
                path_folder_cod = create_folder('CODIGO') 


    # MoveFile        
    move_file(xlsb, path_folder_excel)
    move_file(csv, path_folder_excel)
    move_file(xlsx, path_folder_excel)
    move_file(xls, path_folder_excel)

    move_file(doc, path_folder_word)
    move_file(docx, path_folder_word)

    move_file(ppt, path_folder_pp)
    move_file(pptx, path_folder_pp)

    move_file(png, path_folder_img)
    move_file(jpg, path_folder_img)
    move_file(bmp, path_folder_img)
    move_file(gif, path_folder_img)
    move_file(raw, path_folder_img)
    move_file(jfif, path_folder_img)

    move_file(mov, path_folder_video)
    move_file(mp4, path_folder_video)
    move_file(avi, path_folder_video)
    move_file(flv, path_folder_video)

    move_file(exe, path_folder_exc)
    move_file(msi, path_folder_exc)

    move_file(tar, path_folder_zip)
    move_file(zip_, path_folder_zip)
    move_file(rar, path_folder_zip)
    move_file(gz, path_folder_zip)

    move_file(py, path_folder_cod)
    move_file(cs, path_folder_cod)
    move_file(js, path_folder_cod)
    move_file(php, path_folder_cod)
    move_file(html, path_folder_cod)
    move_file(sql, path_folder_cod)
    move_file(css, path_folder_cod)

    
            
    return ('Local: ' + path_folder_txt + \
           "\nTotal Arquivo txt movido: " + str(len(txt)) + \
           "\n\nLocal: " + path_folder_pdf + \
           "\nTotal Arquivo pdf movido: " + str(len(pdf)) + \
           "\n\nLocal: " + path_folder_mp3 + \
           "\nTotal Arquivo mp3 movido: " + str(len(mp3)) + \
           "\n\nLocal: " + path_folder_json + \
           "\nTotal Arquivo json movido: " + str(len(json)) + \
           
           "\n\nLocal: " + path_folder_excel + \
           "\nTotal Arquivo xlsb movido: " + str(len(xlsb)) + \
           "\nTotal Arquivo xlsx movido: " + str(len(xlsx)) + \
           "\nTotal Arquivo xls  movido: " + str(len(xls)) + \
           "\nTotal Arquivo csv  movido: " + str(len(csv))  + \
           
           "\n\nLocal: " + path_folder_word + \
           "\nTotal Arquivo doc  movido: " + str(len(doc)) + \
           "\nTotal Arquivo docx movido: " + str(len(docx)) + \

           "\n\nLocal: " + path_folder_pp + \
           "\nTotal Arquivo ppt  movido: " + str(len(ppt)) + \
           "\nTotal Arquivo pptx movido: " + str(len(pptx)) + \

            "\n\nLocal: " + path_folder_pbi + \
           "\nTotal Arquivo pbix  movido: " + str(len(pbix)) + \

           "\n\nLocal: " + path_folder_img + \
           "\nTotal Arquivo png  movido: " + str(len(png)) + \
           "\nTotal Arquivo jpg  movido: " + str(len(jpg)) + \
           "\nTotal Arquivo bmp  movido: " + str(len(bmp)) + \
           "\nTotal Arquivo gif  movido: " + str(len(gif)) + \
           "\nTotal Arquivo raw  movido: " + str(len(raw)) + \
           "\nTotal Arquivo jpeg movido: " + str(len(jpeg)) + \
           "\nTotal Arquivo jfif movido: " + str(len(jfif)) + \
           
           "\n\nLocal: " + path_folder_video + \
           "\nTotal Arquivo mov movido: " + str(len(mov)) + \
           "\nTotal Arquivo mp4 movido: " + str(len(mp4)) + \
           "\nTotal Arquivo avi movido: " + str(len(avi)) + \
           "\nTotal Arquivo flv movido: " + str(len(flv)) + \

           "\n\nLocal: " + path_folder_exc + \
           "\nTotal Arquivo exe movido: " + str(len(exe)) + \
           "\nTotal Arquivo msi movido: " + str(len(msi)) +     

           "\n\nLocal: " + path_folder_zip + \
           "\nTotal Arquivo tar  movido: " + str(len(tar)) + \
           "\nTotal Arquivo zip_ movido: " + str(len(zip_)) + \
           "\nTotal Arquivo rar  movido: " + str(len(rar)) + \
           "\nTotal Arquivo gz   movido: " + str(len(gz))  + \
            
           "\n\nLocal: " + path_folder_jupyter + \
           "\nTotal Arquivo ipynb movido: " + str(len(ipynb)) + \

           "\n\nLocal: " + path_folder_cod + \
           "\nTotal Arquivo py   movido: " + str(len(py)) + \
           "\nTotal Arquivo cs   movido: " + str(len(cs)) + \
           "\nTotal Arquivo js   movido: " + str(len(js)) + \
           "\nTotal Arquivo php  movido: " + str(len(php)) + \
           "\nTotal Arquivo html movido: " + str(len(html)) +  
           "\nTotal Arquivo sql  movido: " + str(len(sql)) +  
           "\nTotal Arquivo css  movido: " + str(len(css)) 

           )


