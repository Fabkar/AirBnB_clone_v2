#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using do_deploy"""
from os.path import exists
import os
from datetime import datetime
from fabric.api import env
from fabric.api import put
from fabric.api import local
from fabric.api import run

env.user = "ubuntu"
env.hosts = ["35.196.29.78", "35.231.126.72"]


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


def do_deploy(archive_path):
    """Distributes an archive to a web server"""
    if not os.path.exists(archive_path):
        return False

    data_releases = "data/web_static/releases"
    file_ = archive_path.split("/")[-1]
    name = file_.split(".")[0]

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data_releases/{}".format(name))
        run("sudo tar -xzf /tmp/{} -C /data_releases/{}/".format(file_, name))
        run("sudo rm /tmp/{}".format(file_))
        run("sudo mv /data_releases/{}/web_static/* "
            "/data_releases/{}/".format(name, name))
        run("sudo rm -rf /data_releases/{}/web_static".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data_releases/{}/ /data/web_static/current".
            format(name))
        return True
    except Exception:
        return False


def deploy():
    """Create a distribute an archive to a web server"""
    file_ = do_pack()
    if file_ is None:
        return False
    return do_deploy(file_)
