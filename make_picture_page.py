import os
from random import shuffle

from PIL import Image
import numpy as np


index_page_html = '<html><body>'

# file_list = os.listdir('./waybackpics')
# shuffle(file_list)

os.chdir('waybackpics')
file_list = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
os.chdir('..')

file_list.reverse()

x = []

for img_file in file_list:
    try:
        img = Image.open('waybackpics/'+img_file).convert('L')
        # values = abs(np.fft.fft2(np.asarray(img.convert('L')))).flatten().tolist()
        # high_values = [x for x in values if x > 10000]
        # high_values_ratio = 100*(float(len(high_values))/len(values))
        # x.append(high_values_ratio)

        try:
            img.thumbnail((200, 200), Image.ANTIALIAS)
        except AttributeError:
            img.thumbnail((200, 200), Image.LANCZOS)
        w, h = img.size
        pct = ( sum(x[0] for x in sorted(img.convert('RGB').getcolors(w*h), key=lambda x: x[0], reverse=True)[:5])/float((w*h)))
        x.append(pct)
        
    except OSError:
        continue

    if(pct < 0.4):
        index_page_html += str(pct)+'<br/><IMG SRC="./waybackpics/'+img_file+'" /><br/><br/>'    
        

f = open('index_page.html', 'w')
f.write(index_page_html + '</body></html>')
f.close()
