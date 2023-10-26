import tkinter as tk
from tkinter import END, ttk
import subprocess
import json
from tkinter import messagebox

with open("data.json", 'r', encoding='utf-8') as json_file:
    suggestions_dict = json.load(json_file)
   
def validate_numeric_input(P):
    if P == "" or P == "." or P.isdigit():
        return True
    elif P.count('.') == 1 and P.replace(".", "").isdigit():
        return True
    else:
        return False

def connect_to_vnc_server(host, port, password):
    try:
        command = ["C:\\Program Files\\RealVNC\\VNC Viewer\\vncviewer.exe", host + "::" + str(port),"-passwd", password]
        print("Executing command:", " ".join(command))
        subprocess.run(command)


    except Exception as e:
        print(f"Error: {e}")
        
def update_suggestions(event):
    global suggestions_dict
    search_term = nameEntry.get().lower()
    matching_suggestions = [(key,value) for key,value in suggestions_dict.items() if search_term in value[0].lower()]

    treeview.delete(*treeview.get_children())

    for key,value in matching_suggestions:
        treeview.insert('', tk.END, values=(key,value[0],value[1]))

def select_suggestion(event):
    global suggestions_dict
    selected_item = treeview.selection()
    if selected_item:
        item = treeview.item(selected_item)
        data = item['values']
        host = data[2]
        if __name__ == "__main__":
            host = host.replace(" ", "")
            port = 5900
            password = ""
            connect_to_vnc_server(host, port, password)
        


def update_sug_del(event):
    global suggestions_dict
    search_term1 = idEntry.get()
    matching_suggestions1 = [(key,value) for key,value in suggestions_dict.items() if search_term1 in str(key)]

    treeview.delete(*treeview.get_children())

    for key1,value in matching_suggestions1:
        treeview.insert('', tk.END, values=(key1,value[0],value[1]))

def insertData(event=None):
    global suggestions_dict
    newName = newNameEntry.get()
    newIP = newipEntry.get()
    newID = int(list(suggestions_dict.keys())[-1]) + 1
    suggestions_dict[newID] = (newName,newIP)
    with open("data.json","w",encoding="utf-8") as json_file:
        json.dump(suggestions_dict, json_file, ensure_ascii=False, indent=4)
    treeview.delete(*treeview.get_children())
    for key,value in suggestions_dict.items():
        treeview.insert('', tk.END, values=(key,value[0],value[1]))
    newNameEntry.delete('0',END)
    newipEntry.delete('0',END)
def deleteData(event=None):
    delID = idEntry.get()
    delID = int(delID)
    if str(delID) in suggestions_dict:
        delID = idEntry.get()
        suggestions_dict.pop(delID,None)
        with open('data.json','w',encoding="utf-8") as json_file:
            json.dump(suggestions_dict,json_file,ensure_ascii=False, indent=4)
        treeview.delete(*treeview.get_children())
        for key,value in suggestions_dict.items():
            treeview.insert('', tk.END, values=(key,value[0],value[1]))
    else :
        messagebox.showinfo("Error", "This ID not found.")
        with open('data.json','w',encoding="utf-8") as json_file:
            json.dump(suggestions_dict,json_file,ensure_ascii=False, indent=4)
        treeview.delete(*treeview.get_children())
        for key,value in suggestions_dict.items():
            treeview.insert('', tk.END, values=(key,value[0],value[1]))
    idEntry.delete('0',END)
def update_sug_up(event):
    global suggestions_dict
    search_term1 = idUEntry.get()
    matching_suggestions1 = [(key,value) for key,value in suggestions_dict.items() if search_term1 in str(key)]

    treeview.delete(*treeview.get_children())

    for key1,value in matching_suggestions1:
        treeview.insert('', tk.END, values=(key1,value[0],value[1]))
    

def updateData(event=None):
    global suggestions_dict
    idU = idUEntry.get()
    newipU = newipUEntry.get()
    newNameU = newNameUEntry.get()
    idU = int(idU)
    if str(idU) in suggestions_dict:
        idU = idUEntry.get()
        suggestions_dict[idU] = (newNameU,newipU)
        
        with open('data.json','w',encoding="utf-8") as json_file:
            json.dump(suggestions_dict,json_file,ensure_ascii=False, indent=4)
        treeview.delete(*treeview.get_children())
        for key,value in suggestions_dict.items():
            treeview.insert('', tk.END, values=(key,value[0],value[1]))
    else:
        messagebox.showinfo("Error", "This ID not found.")
        with open('data.json','w',encoding="utf-8") as json_file:
            json.dump(suggestions_dict,json_file,ensure_ascii=False, indent=4)
        treeview.delete(*treeview.get_children())
        for key,value in suggestions_dict.items():
            treeview.insert('', tk.END, values=(key,value[0],value[1]))
    idUEntry.delete('0',END)
    newipUEntry.delete('0',END)
    newNameUEntry.delete('0',END)
    
root = tk.Tk()

root.title("VNC Launcher")
root.iconbitmap(default="ico.ico")
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")
validate_numeric = root.register(validate_numeric_input)


frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.Frame(frame)
widgets_frame.grid(row=0,column=0,padx=10,pady=10)
#search frame
modify_frame = ttk.LabelFrame(widgets_frame,text="Search...")
modify_frame.grid(row=0,column=0)

nameLabel = ttk.Label(modify_frame,text="Name:")
nameLabel.grid(row=0,column=0,sticky='e')
nameEntry = ttk.Entry(modify_frame)
nameEntry.bind("<KeyRelease>", update_suggestions)
nameEntry.grid(row=0,column=1,sticky='w',padx=5,pady=5)

#Insert contact 

insert_frame = ttk.LabelFrame(widgets_frame,text="Insert Contact")
insert_frame.grid(row=1,column=0,pady=10)

newNameLabel = ttk.Label(insert_frame,text="Name:")
newNameLabel.grid(row=0,column=0,sticky='e')
newNameEntry = ttk.Entry(insert_frame)
newNameEntry.bind("<Return>",lambda e:e.widget.tk_focusNext().focus_set())
newNameEntry.grid(row=0,column=1,sticky='w',padx=5,pady=5)

newipLabel = ttk.Label(insert_frame,text="IP:")
newipLabel.grid(row=1,column=0,sticky='e')
newipEntry = ttk.Entry(insert_frame,validate="key", validatecommand=(validate_numeric, "%P"))
newipEntry.bind("<Return>",insertData)
newipEntry.grid(row=1,column=1,sticky='w',padx=5,pady=5)

addButton = ttk.Button(insert_frame,text="Add",command=insertData)
addButton.grid(row=2,column=1,pady=(0,5),padx=(0,30))

#Delete Contact 

delete_frame = ttk.LabelFrame(widgets_frame,text="Delete Contact")
delete_frame.grid(row=2,column=0)

idLabel = ttk.Label(delete_frame,text="ID:")
idLabel.grid(row=0,column=0,sticky='e',padx=(5,5))
idEntry = ttk.Entry(delete_frame,validate="key", validatecommand=(validate_numeric, "%P"))
idEntry.bind("<KeyRelease>", update_sug_del)
idEntry.bind("<Return>",deleteData)
idEntry.grid(row=0,column=1,sticky='w',padx=9,pady=5)
deleteButton = ttk.Button(delete_frame,text="Delete",command=deleteData)
deleteButton.grid(row=2,column=1,pady=(0,5),padx=(0,20))

#update contact 

update_frame = ttk.LabelFrame(widgets_frame,text="Update Contact")
update_frame.grid(row=3,column=0,pady=10)

idULabel = ttk.Label(update_frame,text="ID:")
idULabel.grid(row=0,column=0,sticky='e',padx=(5,5))
idUEntry = ttk.Entry(update_frame,validate="key", validatecommand=(validate_numeric, "%P"))
idUEntry.bind("<KeyRelease>", update_sug_up)
idUEntry.bind("<Return>",lambda e:e.widget.tk_focusNext().focus_set())
idUEntry.grid(row=0,column=1,sticky='w',padx=(5,0),pady=5)

newNameULabel = ttk.Label(update_frame,text="Name:")
newNameULabel.grid(row=1,column=0,sticky='e')
newNameUEntry = ttk.Entry(update_frame)
newNameUEntry.bind("<Return>",lambda e:e.widget.tk_focusNext().focus_set())
newNameUEntry.grid(row=1,column=1,sticky='w',padx=5,pady=5)

newipULabel = ttk.Label(update_frame,text="IP:")
newipULabel.grid(row=2,column=0,sticky='e')
newipUEntry = ttk.Entry(update_frame,validate="key", validatecommand=(validate_numeric, "%P"))
newipUEntry.bind("<Return>",updateData)
newipUEntry.grid(row=2,column=1,sticky='w',padx=5,pady=5)

updateButton = ttk.Button(update_frame,text="Update",command=updateData)
updateButton.grid(row=3,column=1,pady=(0,5),padx=(0,30))

#show data 

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10,padx=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("ID", "Namne", "IP")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set, columns=cols, height=22)
treeview.column("ID", width=50)
treeview.column("Namne", width=180)
treeview.column("IP", width=80)
treeview.bind("<Double-Button-1>", select_suggestion)
treeview.pack()
treeScroll.config(command=treeview.yview)

treeview.heading("#1", text="ID")
treeview.heading("#2", text="Namne")
treeview.heading("#3", text="IP")


for key,value in suggestions_dict.items():
    treeview.insert('', tk.END, values=(key,value[0],value[1]))
root.mainloop()
