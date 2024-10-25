import customtkinter as ctk
import conv
import os
import threading
import shutil
from time import sleep
from PIL import Image
from pytubefix import YouTube
from pytubefix.cli import on_progress
from customtkinter import filedialog as fd


form = ['.mp3', '.wav', '.ogg']
current_form = form[0]
bit_r = ['320k', '256k', '192k', '160k', '128k']
current_bitrate = bit_r[0]
out_opt = False
link_opt = False
temp_output = '.temp'
output = ''
url = ''
yt = None

def set_output():
    global output
    global link_opt, out_opt
    output = fd.askdirectory()
    out_opt = True
    if out_opt == True and link_opt == True:
        opt_5.configure(state='normal')
        lab_3.configure(text=statvar[1])

'''Declarando o endereço do vídeo e confirmando'''
def set_url():
    global url, yt, linkvar
    global link_opt, out_opt
    try:
        url = root.clipboard_get()
        link_opt = True
        yt = YouTube(url, on_progress_callback=on_progress)
        linkvar = ctk.StringVar(value=yt.title)
        url_fr.configure(textvariable=linkvar)
        if out_opt == True and link_opt == True:
            opt_5.configure(state='normal')
            lab_3.configure(text=statvar[1])
    except:
        linkvar = ctk.StringVar(value="Paste a valid link")
        url_fr.configure(textvariable=linkvar)
        sleep(2)
        linkvar = ctk.StringVar(value='Press "Paste URL" button.')
        url_fr.configure(textvariable=linkvar)

def set_format(value):
    global form, current_form
    current_form = value
    opt_1.set(current_form)
    print(current_form)

def set_bitrate(value):
    global bit_r, current_bitrate
    current_bitrate = value
    opt_2.set(current_bitrate)
    print(current_bitrate)

def init_download():
    threading.Thread(target=download).start()
def download():
    # statvar ['Waiting...', 'Ready!', 'Downloading...', 'Converting...', 'Done!', 'File Already Exists!']
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    '''Download do arquivo de audio e convertendo para mp3'''
    audiofile = yt.streams.get_audio_only().download(output_path=temp_output)
    lab_3.configure(text=statvar[2])
    p_bar.set(0.25)
    sleep(2)
    print('Download Completo!')

    '''Convertendo os arquivos para o formato desejado'''
    print('Convertendo...')
    lab_3.configure(text=statvar[3])
    p_bar.set(0.5)
    conv.convert(dir=temp_output, new_form=current_form, target_bitrate=current_bitrate)
    sleep(2)
    p_bar.set(0.75)

    '''Movendo os arquivos da pasta temporária para o diretório do user'''
    files = os.listdir(temp_output)
    for f in files:
        src_path = os.path.join(temp_output, f)
        dst_path = os.path.join(output, f)
        if os.path.exists(dst_path):
            print(f'O Arquivo {f}, já existe!')
            lab_3.configure(text=statvar[5])
            p_bar.set(0)
            sleep(2)
            pass
        else:
            shutil.move(src_path, dst_path)
            lab_3.configure(text=statvar[4])
            p_bar.set(1)
            sleep(2)
            print('Conversão Completa!')
    lab_3.configure(text=statvar[0])
    p_bar.set(0)
    os.startfile(output)


'''Setando a janela'''
root = ctk.CTk(fg_color='#fee50f')
root.iconbitmap('assets/icon.ico')
root.configure(bg='red')
root.geometry('800x500')
root.title('YT to Audio')
root.resizable(width=False, height=False)
root.configure(bg='red')
ctk.FontManager.load_font('assets/MinervaModern_Black.otf')
bg_img1 = ctk.CTkImage(light_image=Image.open('assets/root_bg.png'), dark_image=Image.open('assets/root_bg.png'), size=(800, 401))
bg_img2 = ctk.CTkImage(light_image=Image.open('assets/frame_bg.png'), dark_image=Image.open('assets/frame_bg.png'), size=(800, 100))
lab_img2 = ctk.CTkImage(light_image=Image.open('assets/label2_bg.png'), dark_image=Image.open('assets/label2_bg.png'), size=(400, 50))
logo_img = ctk.CTkImage(light_image=Image.open('assets/logo_nbg.png'), dark_image=Image.open('assets/logo_nbg.png'), size=(200, 100))

linkvar = ctk.StringVar(value='Press "Paste URL" button.')
statvar = ['Waiting...', 'Ready!', 'Downloading...', 'Converting...', 'Done!', 'File Already Exists!']



root_bg1 = ctk.CTkLabel(root, width=800, height=401, image=bg_img1, text=None).place(y=500-401)

fr_1 = ctk.CTkFrame(root, width=800, height=100, fg_color='#fff424', corner_radius=0).place(y=0, x=0)

root_bg2 = ctk.CTkLabel(root, width=800, height=100, image=bg_img2, text=None).place(y=0)

logo = ctk.CTkLabel(fr_1, width=200, height=100, fg_color='darkgoldenrod1', corner_radius=0, text=None, image=logo_img).place(y=0, x=10)

desc_label = ctk.CTkLabel(fr_1, width=400, height=50, fg_color=None, corner_radius=0, text_color='#2b2b2b',
                          text='Select format type, Bitrate, Output Folder and press Download Button.', image=lab_img2, font=('MinervaModern Black', 11),
                          ).place(y=25, x=10+200+10)

credits_label = ctk.CTkLabel(root, width=160, height=20, fg_color='#fee50f', corner_radius=0, text_color='#2b2b2b', text='by Alex Rocha (Requiemd)', font=('MinervaModern Black', 12)).place(y=470, x=10)

lab_1 = ctk.CTkLabel(root, width=100, height=25, text_color='#2b2b2b', text='Format', font=('MinervaModern Black', 18)).place(y=110, x=10)
lab_2 = ctk.CTkLabel(root, width=100, height=25, text_color='#2b2b2b', text='Bitrate', font=('MinervaModern Black', 18)).place(y=110, x=130)
lab_3 = ctk.CTkLabel(root, width=200, height=30, text_color='#2b2b2b', font=('MinervaModern Black', 16), text=statvar[0])
lab_3.place(y=335+40+10, x=18)
prog = 50.0
p_bar = ctk.CTkProgressBar(root, width=220, height=10, progress_color='#fbff80', fg_color='#2b2b2b', border_width=2, border_color='#2b2b2b')
p_bar.place(y=415, x=10)
p_bar.set(0)

opt_1 = ctk.CTkOptionMenu(root, values=form, width=100, height=40, bg_color='transparent', fg_color='#2b2b2b', button_color='#2b2b2b',
                          button_hover_color='#fbff80', dropdown_fg_color='#2b2b2b', dropdown_hover_color='#fbff80',
                          text_color='#fea328', dropdown_text_color='#fea328', font=('MinervaModern Black', 16),
                          dropdown_font=('MinervaModern Black', 16), command=set_format)
opt_1.set(current_form)
opt_1.place(y=145, x=10)
opt_2 = ctk.CTkOptionMenu(root, values=bit_r, width=100, height=40, bg_color='transparent', fg_color='#2b2b2b', button_color='#2b2b2b',
                          button_hover_color='#fbff80', dropdown_fg_color='#2b2b2b', dropdown_hover_color='#fbff80',
                          text_color='#fea328', dropdown_text_color='#fea328', font=('MinervaModern Black', 16),
                          dropdown_font=('MinervaModern Black', 16), command=set_bitrate)
opt_2.set(current_bitrate)
opt_2.place(y=145, x=130)
opt_3 = ctk.CTkButton(root, width=100, height=40, text='Output', fg_color='#2b2b2b', hover_color='#fbff80', font=('MinervaModern Black', 16), text_color='#fea328',
                      command=set_output)
opt_3.place(y=205, x=10)
opt_4 = ctk.CTkButton(root, width=100, height=40, text='Paste URL', fg_color='#2b2b2b', hover_color='#fbff80', font=('MinervaModern Black', 16), text_color='#fea328',
                      command=set_url)
opt_4.place(y=205, x=130)
url_fr = ctk.CTkEntry(root, width=220, height=30, fg_color='#2b2b2b', text_color='#fea328', state='disabled', textvariable=linkvar, font=('MinervaModern Black', 12))
url_fr.place(y=285, x=10)
opt_5 = ctk.CTkButton(root, width=100, height=40, text='Download', fg_color='#2b2b2b', hover_color='#fbff80', font=('MinervaModern Black', 16), text_color='#fea328', state='disabled',
                      command=init_download)
opt_5.place(y=335, x=65)

root.mainloop()
