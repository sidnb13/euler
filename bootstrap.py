#!/usr/local/bin/python3

import argparse
import os
import subprocess
from datetime import datetime

PY_PATH = 'project-euler/code/'
TEX_PATH = 'project-euler/docs/'

code2 ='''

import time

def solve():
    pass
            
if __name__ == "__main__":
    s = time.time()
    solve()
    e = time.time()
    print('%.3fms' % ((e-s)*1000))'''

def create_code(n):
    if os.path.exists(os.path.join(PY_PATH, '%d.py' % n)):
        print('Code already exists')
        return
    
    os.system('touch %s' % os.path.join(PY_PATH, '%d.py' % n))
    code1 = '# Project Euler #%d | Sidharth Baskaran | %s' % (n, datetime.now().strftime('%m/%d/%Y'))
    
    with open(os.path.join(PY_PATH, '%d.py' % n), 'w') as f:
        f.write(code1)
        f.write(code2)

def create_writeup(n):
    with open('./project-euler/template.tex','r') as f:
        lines = f.readlines()
        newLines = []
        for line in lines:
            if '{{1}}' in line:
                line = line.replace('{{1}}', str(n))
            if '{{2}}' in line:
                line = line.replace('{{2}}', datetime.now().strftime('%m/%d/%Y'))
            if '{{3}}' in line:
                line = line.replace('{{3}}', os.path.join('../code', '%d.py' % n))
            newLines.append(line)
        
    os.system('touch %s' % os.path.join(TEX_PATH, '%d.tex' % n))
    with open(os.path.join(TEX_PATH, '%d.tex' % n), 'w') as tf:
        tf.writelines(newLines)
        
def compile(n): # for use in current directory only
    subprocess.check_call(['pdflatex', './%d.tex' % n])
    exts = ('.out', '.aux', '.log')
    for fn in os.listdir('.'):
        if fn.lower().endswith(exts) :
            os.remove(fn)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Bootstrap Project Euler problems')
    parser.add_argument('filename', type=int, help='Project Euler problem number')
    parser.add_argument('--code', action='store_true', help='Create Python source code file')
    parser.add_argument('--writeup', '-w', action='store_true', help='Create template writeup TeX file')
    parser.add_argument('--compile', '-c', action='store_true', help='Compile writeup TeX file')
    
    args = parser.parse_args()
    
    if args.code:
        create_code(args.filename)
    elif args.writeup:
        create_writeup(args.filename)
    elif args.compile:
        compile(args.filename)