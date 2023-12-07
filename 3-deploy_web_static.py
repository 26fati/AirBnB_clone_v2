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
        run(f"mkdir -p /data/web_static/releases/{name}/")
        run(f"tar -xzvf /tmp/{filename} -C /data/web_static/releases/{name}/")
        run(f"rm /tmp/{filename}")
        run(f"mv /data/web_static/releases/{name}/web_static/* \
            /data/web_static/releases/{name}/")
        run(f"rm -rf /data/web_static/releases/{name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{name}/ \
            /data/web_static/current")
        print("New version deployed!")
    except Exception:
        return False
    return True


@task
def deploy():
    """creates and distributes an archive to the web servers"""
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)