from tkinter import *
from chat import get_response,bot_name

BG_gray="#AF3F3F"
BG_color="#1C6868"
text_color="#F1EFF5"
font="Helvetica 14"
font_bold="Helvetica 14 bold"





class ChatApplication:
    def __init__(self):
        self.window=Tk()
        self._setup_main_window()
    def run(self):
        self.window.mainloop()
    def _setup_main_window(self):
        self.window.title("DBMS Assistant")
        self.window.resizable(width=False,height=False)
        self.window.configure(width=470,height=550,bg=BG_color)

        head_label=Label(self.window,bg=BG_color,fg=text_color,text="welcome",font=font_bold,pady=10)
        head_label.place(relwidth=1)

        line=Label(self.window,width=450,bg=BG_gray)
        line.place(relwidth=1,rely=0.07,relheight=0.012)

        self.text_widget=Text(self.window,width=20,height=2,bg=BG_color,fg=text_color,
                              font=font,padx=5,pady=5)
        self.text_widget.place(relheight=0.745,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor="arrow",state=DISABLED)
        # scrollbar = Scrollbar(self.text_widget)
        # Scrollbar.place(relheight=1,relx = 0.974)
        # scrollbar.configure(command=self.text_widget.yview(self))

        #bottom lebel
        bottom_label = Label(self.window, bg="#957DBB", height=80)
        bottom_label.place(relwidth= 1 , rely=0.825)
        #message
        self.msg_entry  = Entry(bottom_label, bg = "#2C3E50", fg=text_color, font=font)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self._on_enter_pressed)

        #send button
        send_button = Button(bottom_label, text="send", font=font_bold, width=20, bg= BG_gray,
                             command=lambda :self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.22)




    def _on_enter_pressed(self,event):
        msg=self.msg_entry.get()
        self._insert_message(msg, "you")
    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}:{msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        msg2 = f"{bot_name}:{get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)





if __name__=="__main__":
    app=ChatApplication()
    app.run()