#!/usr/bin/python3
# Fabric script that generates a .tgz archive
# from the contents of the web_static folder
from time import strftime
from datetime import datetime
from os.path import exists
from fabric.api import env, run, put, local
env.hosts = ["35.196.29.78", "35.231.126.72"]


def do_pack():
    """Return the archive path if the archive has been correctly generated
    """
    time_format = strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    try:
        local("tar -czvf versions/web_static_{:s}.tgz web_static/".format(
              time_format))
        return ("versions/web_static_{:s}.tgz".format(time_format))
    except Exception:
        return None


def do_deploy(archive_path):
    """ do_deploy function that distributes an archive to web servers
    """
    # print(archive_path)
    # file = archive_path.split("/")[-1]
    # print(file)
    # print(file.split(".")[0])
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


def deploy():
    """ creates and distributes an archive to your web servers,
    using the function deploy
    """
    do_pack_path = do_pack()
    if do_pack_path:
        return do_deploy(do_pack_path)
    else:
        return False