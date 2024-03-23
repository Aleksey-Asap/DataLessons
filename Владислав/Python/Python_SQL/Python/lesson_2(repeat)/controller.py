import model
import view
import operation

def button_click():
    some_str = view.inp()
    some_tuple = operation.op(some_str)
    model.init(some_tuple[0], some_tuple[1])
    if some_tuple[2] == '+':
        result = model.sum()
    elif some_tuple[2] == '-':
        result = model.dif()
    elif some_tuple[2] == '*':
        result = model.proiz()
    else:
        result = model.div()
    view.view_data(result)