import user_interface
import export
import importt

def button_click():
    res_process = user_interface.get_process()
    if res_process == 1:
        export.export_structure()
    else: importt.import_structure2()