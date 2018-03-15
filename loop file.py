import os
import glob
from PIL import Image
from multiprocessing import Pool
import multiprocessing as mp

def thumbnail_pic(path,a,f):
    name = os.path.join(path, f)
    im = Image.open(name)
    width, height = im.size
    for x in range(width):
        for y in range(height):
            r,g,b,a = im.getpixel((x,y))
            if(r==255 and b==255 and g==255):
                xset=x-720
                yset=y-1280
                xset=abs(xset)
                yset=abs(yset)
                pixelset=long(xset**2+yset**2)
                pixelset=pixelset ** 0.5
                fpixelset=(float(pixelset)/1464.0)#1463.7
                pixelset=int(20*fpixelset)
                pixelset=235+pixelset
                im.putpixel((x,y), (pixelset,pixelset,pixelset))

    im.save(name, 'PNG')

    print str(f) + ' file Done'


def multicore(path):
    pool=mp.Pool()
    a = glob.glob(r'*.png')
    for f in a:
        pool.apply_async(thumbnail_pic,(path,a,f))
    pool.close()
    pool.join() # Wait for all child processes to close.

if __name__ == '__main__':
    path = '.'
    multicore(path)
    print 'All files Done'
