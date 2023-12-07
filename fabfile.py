#!/usr/bin/python3
from fabric.api import local, task
from datetime import datetime


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
