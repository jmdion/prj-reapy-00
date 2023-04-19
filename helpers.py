import datetime
import pathlib

from reapy import open_project as _open_project


# def create_new_project_based_on(base_path: str):
#
#     prj = _open_project(base_path)
#
#     date_time = datetime.datetime.now()
#     datetime_string = str(date_time.date()) + 'T'
#     datetime_string += str(date_time.hour) + str(date_time.minute) + str(date_time.second)
#     date_time_string = '{:%Y-%m-%dT%H%M%S}'.format(date_time)
#
#     posix_path = pathlib.PurePosixPath(base_path)
#     new_path = posix_path.root + posix_path.stem + '-' + date_time_string + posix_path.suffix
#
#     prj.save(force_save_as=True)
#
#     return prj
