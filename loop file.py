import os, getopt
import sys
import glob
from PIL import Image
from multiprocessing import Pool
import multiprocessing as mp
import time

def thumbnail_pic(path,a,f):
    name = os.path.join(path, f)
    im = Image.open(name)
    width, height = im.size
    for x in range(width):
        for y in range(height):
            r,g,b,a = im.getpixel((x,y))
            if(r>150 or b>155 or g>155):
                xset=x-720
                yset=y-1280
                xset=abs(xset)
                yset=abs(yset)
                pixelset=long(xset**2+yset**2)
                pixelset=pixelset ** 0.5
                fpixelset=(float(pixelset)/1464.0)#1463.7
                pixelset=int(70*fpixelset)
                pixelset=185+pixelset
                im.putpixel((x,y), (pixelset,pixelset,pixelset))
                # im.putpixel((x,y), (255,0,0))

    im.save(name, 'PNG')

    print str(f) + ' file Done'


def multicore(path):
    pool=mp.Pool()
    a = glob.glob(path+'\\'+'*.png')
    print path+'\\'+'*.png'
    for f in a:
        pool.apply_async(thumbnail_pic,(path,a,f))
    pool.close()
    pool.join() # Wait for all child processes to close.

if __name__ == '__main__':
    # print 'main'
    path = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hp:",["path="])
    except getopt.GetoptError:
        print 'test.py -p <path>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -p <path>'
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
    print path
    multicore(path)
    print 'All files Done'
