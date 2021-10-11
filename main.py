from tkinter import Tk, Label, Text, DISABLED, NORMAL, END, Scrollbar, Entry, Button
from tkinter.constants import WORD
from chat import get_response, bot_name

BG_GRAY = "#ABB2B9"
WHITE_TEXT_COLOR = "#FFFFFF"
BLACK_TEXT_COLOR = "#000000"
BG_COLOR = "#EAECEE"
BG_Skyblue = "#1cdbfc"

FONT = "FiraCode 14"
FONT_BOLD = "FiraCode 14 bold"


class ChatApplication:
    """app window"""

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        """TODO: Docstring for run."""
        self.window.mainloop()

    def _setup_main_window(self):
        """TODO: Docstring for _setup_main_window."""
        self.window.title("CSE 410 ChatBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # Head label
        head_label = Label(self.window, bg=BG_COLOR, fg=BLACK_TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relheight=0.012, relwidth=1, rely=0.07)

        # text width
        self.text_widget = Text(self.window, width=20, height=2,
                                bg=BG_COLOR, fg=BLACK_TEXT_COLOR, font=FONT, padx=5, pady=5, wrap=WORD)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # # scroll bar
        # scrollbar = Scrollbar(self.text_widget)
        # scrollbar.place(relheight=1, relx=0.974)
        # scrollbar.configure(command=self.text_widget.yview)

        # bottom leabel
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#1cdbfc",
                               fg=BLACK_TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06,
                             rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD,
                             width=20, bg=BG_GRAY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        """TODO: Docstring for _on_enter_pressed.

                                        :arg1: TODO
                                        :returns: TODO

                                        """
        msg = self.msg_entry.get()
        self._insert_message(msg, "Me")

    def _insert_message(self, msg, sender):
        """TODO: Docstring for _insert_message.

                                        :arg1: TODO
                                        :returns: TODO

                                        """
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response((msg))}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
