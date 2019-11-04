import os
import shutil
import requests

from io import BytesIO
from PIL import Image
from random import randint
from pygeotile.point import Point

class rect_2d:
    def __init__(self, minX, minY, maxX, maxY):
        if maxX < minX:
            minX, maxX = maxX, minX
        if maxY < minY:
            minY, maxY = maxY, minY
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY

tile_size = 256
def to_tile_rect(rect, zoom):
    minPoint = Point.from_latitude_longitude(rect.minX, rect.minY)
    maxPoint = Point.from_latitude_longitude(rect.maxX, rect.maxY)
    minTilePoint = minPoint.pixels(zoom)
    maxTilePoint = maxPoint.pixels(zoom)
    return rect_2d(minTilePoint[0] // tile_size, minTilePoint[1] // tile_size, maxTilePoint[0] // tile_size, maxTilePoint[1] // tile_size)
 

def get_limit_rect():
    #return rect_2d(53.912871, 25.259006, 53.856857, 25.335503)
    return rect_2d(54.047209, 25.386200, 53.975729, 25.641725)
def get_zoom_level():
    return 17

def get_url_for(x, y, z):
   return "http://mts" + str(randint(0, 3)) + ".google.com/vt/lyrs=s&hl=x-local&x=" + str(x) + "&y=" + str(y) + "&z=" + str(z)

def print_progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r %s |%s| %s/%s %s' % (prefix, bar, iteration, total, suffix), end = '\r')
    if iteration == total: 
        print()

rect = get_limit_rect()
z = get_zoom_level()

rect = to_tile_rect(rect, z)

x_range = range(rect.minX, rect.maxX + 1) 
y_range = range(rect.minY, rect.maxY + 1) 

total = len(x_range) * len(y_range)
i = 0
for x in x_range:
    for y in y_range:
        url = get_url_for(x, y, z)
        response = requests.get(url, stream=True)
        dir_path = str(z) + "_2";
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        local_file = open(dir_path + "/local_image" + "X"+ str(x) + "Y"+ str(y) + ".jpg", "wb")
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, local_file)
        del response        
        print_progress_bar(i + 1, total, prefix = 'Progress:', suffix = 'Complete', length = 50)
        i += 1
