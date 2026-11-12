import pyperclip, json, os, time, threading
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

Clipboard = "clipboard.json"

def load():
    return json.load(open(Clipboard)) if os.path.exists(Clipboard) else []

def save(items):
    json.dump(items, open(Clipboard, "w"), indent=2)

def refresh():
    for w in list_frame.winfo_children():
        w.destroy()
    for i, item in enumerate(load()):
        row = ctk.CTkFrame(list_frame)
        row.pack(fill="x", pady=2)
        ctk.CTkButton(row, text=item[:50], anchor="w", fg_color="transparent",
                      hover_color="gray30", command=lambda i=i: copy(i)
                      ).pack(side="left", fill="x", expand=True, padx=5)
        ctk.CTkButton(row, text="✕", width=30, fg_color="transparent",
                      hover_color="darkred", command=lambda i=i: delete(i)
                      ).pack(side="right", padx=5)

def copy(i):
    pyperclip.copy(load()[i])
    status.configure(text="Copied")

def delete(i):
    items = load()
    items.pop(i)
    save(items)
    refresh()
    status.configure(text=f"Saved: {len(items)}")

def watch():
    last = ""
    while True:
        try:
            cur = pyperclip.paste()
            items = load()
            if cur and cur != last and cur not in items:
                last = cur
                items.insert(0, cur)
                save(items)
                root.after(0, refresh)
        except Exception:
            pass
        time.sleep(1)

root = ctk.CTk()
root.title("Clipboard History")
root.geometry("400x600")

ctk.CTkLabel(root, text="Clipboard History", font=("Arial", 24, "bold")).pack(pady=(20, 10))

list_frame = ctk.CTkScrollableFrame(root, label_text="History")
list_frame.pack(pady=10, padx=20, fill="both", expand=True)

status = ctk.CTkLabel(root, text=f"Saved: {len(load())}")
status.pack(pady=(5, 0))

ctk.CTkButton(root, text="Clear All", width=120, fg_color="transparent",
              border_width=1, command=lambda: (save([]), refresh(), status.configure(text="Saved: 0"))
              ).pack(pady=(5, 20))

refresh()
threading.Thread(target=watch, daemon=True).start()
root.mainloop()