# utility functions

import os
import requests
import shutil
from pathlib import Path

from PIL import Image


class GoliveLibrary():

    @staticmethod
    def dirnou(obj):
        # dir() listing without attributes that start with the underscore
        return [x for x in dir(obj) if not x.startswith('_')]  

    @staticmethod
    def lsal(path=''): 
        return os.popen('ls -al ' + path).readlines()

    @staticmethod
    def set_data_directory(dd):
        return str(Path.home()) + '/data/' + dd + '/'

    @staticmethod
    def show_github_image(username, repo, folder, source, localpath, localname, width, height):
        global home_d
        outf = os.path.join(localpath, localname)
        f = 'https://raw.githubusercontent.com/' + username + '/' + repo + '/master/' + folder + '/' + source
        a = requests.get(f, stream = True)
        if a.status_code == 200:
            with open(outf, 'wb') as f:
                a.raw.decode_content = True
                shutil.copyfileobj(a.raw, f)
        return Image.open(outf).resize((width,height),Image.ANTIALIAS)

    @staticmethod
    def show_local_image(directory, filename, width, height):
        f = os.path.join(directory, filename)
        return Image.open(f).resize((width, height), Image.ANTIALIAS)

    @staticmethod
    def get_golive_meridian(ds):       # This method is hard-coded to work for GoLIVE NetCDF files
        pstring = ds.input_image_details.attrs['image1_proj_WKT']
        locale = pstring.find('central_meridian')
        return int(pstring[locale+18:locale+22])

# Test either of the 'show image' functions
# GoliveLibrary.show_github_image('robfatland', 'othermathclub', 'images/cellular', 'conus_textile_shell_2.png', home_d, 'ctextile.jpg', 450, 250)
# GoliveLibrary.show_local_image(home_d, 'ctextile.jpg', 450, 250)
