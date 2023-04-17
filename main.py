from reapy import open_project, FX


# def get_preset_index_from_name(fx: FX, name: str):
#     for idx in range(fx.n_preset):
#         if fx.preset == name:
#             return idx
#
#     return None


prj = open_project("R:/Production/Projets REAPER/base-project-00/base-project-00.rpp")

prj.bpm = 60

track = prj.add_track(name="my track 2")
fx = track.add_fx("Kontakt (Native Instruments) (64 out)")


print(f"{fx.preset_index}")



# fx.preset = r"R:\Production\Projets REAPER\prj-for-reapy-01\_me-simple.sine.nmsv"

item = track.add_midi_item(start=1.0, end=3.0)

take = item.takes[0]

take.add_note(start=0.0, end=1.0, pitch=60)


prj.close()






