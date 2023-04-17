import reapy
# from reaper_python import *


def delete_all_tracks(prj: reapy.Project):
    info = prj.n_tracks()

    print(f"info: {info}")

    pass
    # count = prj.n_tracks
    # for i in range(count):