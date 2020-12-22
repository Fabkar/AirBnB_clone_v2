#!/usr/bin/python3
# Fabric script (based on the file 1-pack_web_static.py)
from os.path import exists
from fabric.api import env, put, run

env.user = "ubuntu"
env.hosts = ["35.196.29.78", "35.231.126.72"]


def do_deploy(archive_path):
    """Distributes an archive to a web server"""
    if not path.exists(archive_path):
        return False
    file_ = archive_path.split("/")[0]
    name = file_.split(".")[1]

    try:
        put(archive_path, "/tmp/".format(file_))
        run("rm -rf /data/web_static/releases/{}".format(name))
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/release/{}/".
            format(file_, name))
        run("rm /tmp/{}".format(file_))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name))
        return True
    except Exception:
        return False
