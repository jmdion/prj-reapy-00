from reapy import open_project, show_message_box

import helpers


def main():

    base_project_path = "R:/Production/Projets REAPER/base-project-00/base-project-00.rpp"
    prj = open_project(base_project_path)
    prj.save(force_save_as=True)

    prj.bpm = 60

    track = prj.add_track(name="my track 2")
    fx = track.add_fx("Kontakt (Native Instruments) (64 out)")

    # fx.preset = r"R:\Production\Projets REAPER\prj-for-reapy-01\_me-simple.sine.nmsv"

    item = track.add_midi_item(start=1.0, end=3.0)

    take = item.takes[0]

    take.add_note(start=0.0, end=1.0, pitch=60)

    # show_message_box("Asdf!")


main()
