"""
AnalyticalBlackLight
Made by perpetualCreations

GUI wrapper using Tkinter for main.py.
"""

import tkinter.messagebox as dialogue, tkinter
from subprocess import call

root = tkinter.Tk()
root.title("ABL: GUI")
root.geometry('{}x{}'.format(560, 300))
root.resizable(width = False, height = False)
date_start_data = tkinter.StringVar(root)
date_start_label = tkinter.Label(root, text = "Start of Date Range")
date_start_label.pack(side = tkinter.TOP)
date_start_entry = tkinter.Entry(root, textvariable = date_start_data)
date_start_entry.pack(side = tkinter.TOP)
date_end_data = tkinter.StringVar(root)
date_end_label = tkinter.Label(root, text = "End of Date Range")
date_end_label.pack(side = tkinter.TOP)
date_end_entry = tkinter.Entry(root, textvariable = date_end_data)
date_end_entry.pack(side = tkinter.TOP)
country_data = tkinter.StringVar(root)
country_label = tkinter.Label(root, text = "Country")
country_label.pack(side = tkinter.TOP)
country_entry = tkinter.Entry(root, textvariable = country_data)
country_entry.pack(side = tkinter.TOP)
state_data = tkinter.StringVar(root)
state_label = tkinter.Label(root, text = "State")
state_label.pack(side = tkinter.TOP)
state_entry = tkinter.Entry(root, textvariable = state_data)
state_entry.pack(side = tkinter.TOP)
county_data = tkinter.StringVar(root)
county_label = tkinter.Label(root, text = "County Numeric Code")
county_label.pack(side = tkinter.TOP)
county_entry = tkinter.Entry(root, textvariable = county_data)
county_entry.pack(side = tkinter.TOP)
export_selection_options = [
    "None",
    "CSV",
    "Graph",
    "Interact. Graph",
]
export_selection_data = tkinter.StringVar(root)
export_selection_data.set(export_selection_options[0])
export_label = tkinter.Label(root, text = "Export Type")
export_label.pack(side = tkinter.TOP)
export_select = tkinter.OptionMenu(root, export_selection_data, export_selection_options[0], export_selection_options[1], export_selection_options[2], export_selection_options[3])
export_select.configure(relief = tkinter.FLAT)
export_select.pack(side = tkinter.TOP)

def parse(s, e, n, p, x, export):
    """
    Parses parameters into call().
    :param s: str, start date.
    :param e: str, end date.
    :param n: str, name of country.
    :param p: str, name of state.
    :param x: str, name of county.
    :param export: str, export type.
    :return: none.
    """
    if export == "None":
        return None
    pass
    export_visible_to_command = {"CSV":"--csv 1", "Graph":"--graph 1", "Interact. Graph":"--showgraph 1"}
    export = export_visible_to_command[export]
    dialogue.showinfo("ABL: Task Started", "Task has been issued. If no output shows up, check parameters including export options, and refer to documentation. \nIn Windows, ABL will freeze for a few seconds, please standby.")
    call("python main.py " + export + " -s " + s + " -e " + e + " -n " + n + " -p " + p + " -x " + x + " --dialogue 1", shell = True)
pass

parse_button = tkinter.Button(root, fg = "white", bg = "#006699", text = "Process", relief = tkinter.FLAT, command = lambda: parse(date_start_data.get(), date_end_data.get(), country_data.get(), state_data.get(), county_data.get(), export_selection_data.get()))
parse_button.pack(side = tkinter.BOTTOM, pady = (0, 10))
root.mainloop()
