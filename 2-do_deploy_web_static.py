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
    if (exists(archive_path) is False):
        return False
    try:
        path = "/data/web_static/releases/"
        path_2 = "/data/web_static/current"
        file = archive_path.split("/")[-1]
        ext_file = file.split(".")[0]
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, ext_file))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file, path, ext_file))
        run('sudo rm /tmp/{}'.format(file))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, ext_file))
        # here
        run('sudo rm -rf {}{}/web_static'.format(path, ext_file))
        run('sudo rm -rf {}'.format(path_2))
        run('sudo ln -s {}{}/ {}'.format(path, ext_file, path_2))
        return True
    except Exception:
        return False
