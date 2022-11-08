from pathlib import Path
from datetime import datetime as DateTime

import sys 


def scanv1(nom,ext) :
    p = Path('.') #liste les sous-dossiers
    list = p.glob(f"**/*.{ext}") #liste les fichiers ayant la bonne extension

    for q in list : 
        size = q.stat().st_size
        dt = DateTime.fromtimestamp(q.stat().st_mtime)
        with open(str(q), 'r') as f:
            line = f.readline().strip('\n')
        
        print(f""" File {str(q)}
        {size} B last modified on {dt}
        first line : {line}          
        """)

path = sys.argv[1]
ext = sys.argv[2]

scanv1(path,ext)