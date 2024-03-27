import tkinter as tk
import requests
from threading import Thread

api = "http://api.quotable.io/random"
quotes =[]
quote_number = 0

window = tk.Tk()
window.geometry("900x260")
window.title("Quote Generator")
window.grid_columnconfigure(0,weight=1)
window.resizable(False,False)
window.configure(bg="black")

def preload_quotes():
    global quotes

    print("Loading more quotes")
    for x in range(10):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "\n\n" + "by " + author
        print(content)

        quotes.append(quote)
    print("finished loading more quotes")

preload_quotes()
def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number = quote_number + 1
    print(quote_number)

    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=preload_quotes)
        thread.start()
#UI
quote_label = tk.Label(window,text="click on the button to generate a random number!",
                       height=6,
                       pady=10,
                       wraplength=800,
                       font=("Arial",14))
quote_label.grid(row=0,column=0,stick="WE",padx=20,pady=10)
button = tk.Button(text="generate",command=get_random_quote,bg='#0052cc',fg="#ffffff",
                   activebackground="grey",font=("Arial",14))
button.grid(row=1,column=0,stick="WE",padx=20,pady=10)

#execute the program
if __name__=="__main__":
    window.mainloop()

