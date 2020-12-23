#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using do_deploy"""
from os.path import exists
import os
from fabric.api import env, put, run

env.user = "ubuntu"
env.hosts = ["35.196.29.78", "35.231.126.72"]


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
