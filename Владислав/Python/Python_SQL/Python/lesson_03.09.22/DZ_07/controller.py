import user_interface
import export
import importt

def button_click():
    res_process = user_interface.get_process()
    res_format = user_interface.get_structure()
    if res_process == 1 and res_format == 1:
        export.export_structure1()
    elif res_process == 1 and res_format == 2:
        export.export_structure2()
    elif res_process == 2 and res_format == 1:
        importt.import_structure1()
    elif res_process == 2 and res_format == 2:
        importt.import_structure2()