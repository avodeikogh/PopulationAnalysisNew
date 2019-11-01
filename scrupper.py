{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Progress: |██████████████████████████████████████████████████| 10368/10368 Complete\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import shutil\n",
    "import requests\n",
    "\n",
    "from io import BytesIO\n",
    "from PIL import Image\n",
    "from random import randint\n",
    "from pygeotile.point import Point\n",
    "\n",
    "class rect_2d:\n",
    "    def __init__(self, minX, minY, maxX, maxY):\n",
    "        if maxX < minX:\n",
    "            minX, maxX = maxX, minX\n",
    "        if maxY < minY:\n",
    "            minY, maxY = maxY, minY\n",
    "        self.minX = minX\n",
    "        self.minY = minY\n",
    "        self.maxX = maxX\n",
    "        self.maxY = maxY\n",
    "\n",
    "tile_size = 256\n",
    "def to_tile_rect(rect, zoom):\n",
    "    minPoint = Point.from_latitude_longitude(rect.minX, rect.minY)\n",
    "    maxPoint = Point.from_latitude_longitude(rect.maxX, rect.maxY)\n",
    "    minTilePoint = minPoint.pixels(zoom)\n",
    "    maxTilePoint = maxPoint.pixels(zoom)\n",
    "    return rect_2d(minTilePoint[0] // tile_size, minTilePoint[1] // tile_size, maxTilePoint[0] // tile_size, maxTilePoint[1] // tile_size)\n",
    " \n",
    "\n",
    "def get_limit_rect():\n",
    "    return rect_2d(53.963885, 25.181123, 53.810128, 25.474735)\n",
    "\n",
    "def get_zoom_level():\n",
    "    return 17\n",
    "\n",
    "def get_url_for(x, y, z):\n",
    "   return \"http://mts\" + str(randint(0, 3)) + \".google.com/vt/lyrs=s&hl=x-local&x=\" + str(x) + \"&y=\" + str(y) + \"&z=\" + str(z)\n",
    "\n",
    "def print_progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):\n",
    "    filledLength = int(length * iteration // total)\n",
    "    bar = fill * filledLength + '-' * (length - filledLength)\n",
    "    print('\\r %s |%s| %s/%s %s' % (prefix, bar, iteration, total, suffix), end = '\\r')\n",
    "    if iteration == total: \n",
    "        print()\n",
    "\n",
    "rect = get_limit_rect()\n",
    "z = get_zoom_level()\n",
    "\n",
    "rect = to_tile_rect(rect, z)\n",
    "\n",
    "x_range = range(rect.minX, rect.maxX + 1) \n",
    "y_range = range(rect.minY, rect.maxY + 1) \n",
    "\n",
    "total = len(x_range) * len(y_range)\n",
    "i = 0\n",
    "for x in x_range:\n",
    "    for y in y_range:\n",
    "        url = get_url_for(x, y, z)\n",
    "        response = requests.get(url, stream=True)\n",
    "        if not os.path.exists(str(z)):\n",
    "            os.mkdir(str(z))\n",
    "        local_file = open(str(z) + \"/local_image\" + \"X\"+ str(x) + \"Y\"+ str(y) + \".jpg\", \"wb\")\n",
    "        response.raw.decode_content = True\n",
    "        shutil.copyfileobj(response.raw, local_file)\n",
    "        del response        \n",
    "        print_progress_bar(i + 1, total, prefix = 'Progress:', suffix = 'Complete', length = 50)\n",
    "        i += 1\n",
    "        \n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
