#!/usr/bin/python3
# Fabric script generates a .tgz archive from the contents of the web_static.
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tgz file"""
    try:
        file_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(file_time)
        com = "tar -cvzf versions/{} web_static".format(file_name)
        local("mkdir -p versions")
        return local(com)
    except Exception:
        return None
