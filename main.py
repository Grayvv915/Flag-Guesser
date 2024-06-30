import tkinter as tk

root = tk.Tk()
root.resizable(False,False)
root.attributes("-fullscreen", False)
root.overrideredirect(0)
root.iconbitmap("iconos/es.ico")
root.geometry("400x210+600+200")
root.title(string="Flag Guesser")

tk.Label(root, text="# Bienvenido a Flag Guesser. #",
         font="Arial 10", pady=10, fg="red").pack()
tk.Label(root, text="En la versión 1 del juego, se mostrará el nombre de un país o estado, y tendrás que adivinar cuál es su bandera entre cuatro opciones.",
         font="Arial 10", wraplength=400, pady=8).pack()
tk.Label(root, text="En la versión 2 del juego, se mostrará una bandera, y tendrás que adivinar a cuál país o estado pertenece entre cuatro opciones.",
         font="Arial 10", wraplength=391, pady=8).pack()

def v1():
    root.destroy()
    import v_one
def v2():
    root.destroy()
    import v_two
tk.Button(root, text="Versión 1", padx=5, pady=5, command=v1).place(x=20 ,y=160)
tk.Button(root, text="Versión 2", padx=5, pady=5, command=v2).place(x=310 ,y=160)

root.mainloop()