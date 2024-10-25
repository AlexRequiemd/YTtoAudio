import os
from pydub import AudioSegment


def convert(dir='.temp', new_form='.mp3', target_bitrate='320k'):
    files = os.listdir(dir)
    for f in files:
        print(dir + '/' + f)
        name, ext = os.path.splitext(f)
        old_form = ext.replace('.', '')
        target_form = new_form.replace('.', '')
        print(f'name = {name}, format = {old_form}')
        audio = AudioSegment.from_file(dir + '/' + f, old_form).export(dir+'/'+name+new_form, format=target_form, bitrate=target_bitrate)
        if os.path.exists(dir + '/' + f):
            os.remove(dir + '/' + f)
        else:
            pass