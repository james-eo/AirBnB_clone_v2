#!/usr/bin/python3
"""Fabric script that generates a tgz archive
from the contents of the web_static folder of
the AirBnB Clone version 2
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Generates a .tgz archive from the contents of
    the web_static folder
    """
    try:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        tgz_file = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(tgz_file))
        return tgz_file
    except Exception as e:
        return None
