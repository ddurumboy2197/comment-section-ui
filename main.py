import tkinter as tk
from tkinter import ttk

class CommentSection:
    def __init__(self, root):
        self.root = root
        self.root.title("Comment Section")
        self.root.geometry("800x600")

        self.comment_frame = tk.Frame(self.root)
        self.comment_frame.pack(fill="both", expand=True)

        self.comment_list = tk.Listbox(self.comment_frame)
        self.comment_list.pack(fill="both", expand=True)

        self.reply_frame = tk.Frame(self.root)
        self.reply_frame.pack(fill="x")

        self.reply_label = tk.Label(self.reply_frame, text="Reply to:")
        self.reply_label.pack(side="left")

        self.reply_var = tk.StringVar()
        self.reply_entry = tk.Entry(self.reply_frame, textvariable=self.reply_var)
        self.reply_entry.pack(side="left", fill="x", expand=True)

        self.reply_button = tk.Button(self.reply_frame, text="Reply", command=self.reply_comment)
        self.reply_button.pack(side="left")

        self.post_button = tk.Button(self.root, text="Post", command=self.post_comment)
        self.post_button.pack(fill="x")

        self.comment_text = tk.Text(self.root)
        self.comment_text.pack(fill="both", expand=True)

    def post_comment(self):
        comment = self.comment_text.get("1.0", "end-1c")
        self.comment_list.insert("end", comment)
        self.comment_text.delete("1.0", "end")

    def reply_comment(self):
        reply = self.reply_var.get()
        selected_index = self.comment_list.curselection()
        if selected_index:
            selected_comment = self.comment_list.get(selected_index)
            self.comment_list.insert("end", f"{selected_comment} -> {reply}")
            self.reply_var.set("")

root = tk.Tk()
comment_section = CommentSection(root)
root.mainloop()
