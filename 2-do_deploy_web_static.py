#!/usr/bin/python3
from fabric.api import local, task, put, run, env
from datetime import datetime
import os


env.hosts = ["52.204.190.21", "54.237.66.214"]
env.user = 'ubuntu'


@task
def do_pack():
    """pack web_static folder"""
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")

    filename = f"web_static_{year}{month}{day}{hour}{minute}{second}.tgz"
    try:
        local("mkdir -p versions")
        local(f"tar -czvf versions/{filename} web_static/")
        return f"versions/{filename}"
    except Exception:
        return None


@task
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = os.path.basename(archive_path)
        name = filename.split('.')[0]
        put(archive_path, '/tmp/')
        run(f"tar -xzvf /tmp/{filename} -C /data/web_static/releases/{name}/")
        run(f"rm /tmp/{filename}")
        run("rm /data/web_static/current")
        run(f"ln -sf /data/web_static/releases/{name}\
            /data/web_static/current")
    except Exception:
        return False
    return True
