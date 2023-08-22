import requests
import tkinter as tk
from tkinter import ttk
# function for getting data from web site
def response_from_web():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    return  response.json()

# function for getting currency index from json version
def currency_from_responce(parameter):
        currency = [i["currency"] for i in parameter]
        return currency
#UI design
windows = tk.Tk()
windows.title("CryptoCrazy")
windows.minsize(width="600",height="600")
first_label = tk.Label(text="Welcome to CryptoCrazy",font=("Arial", 20),pady=20)
first_label.pack()

#values for combobox from nested function of currency index and data from web
currency_combobox = ttk.Combobox(windows,values=currency_from_responce(response_from_web()))
currency_combobox.pack()
# define a function for return selected combobox value with bind function
def option_selected(event):
   selected_option = currency_combobox.get()
   return selected_option

currency_combobox.bind("<<ComboboxSelected>>",option_selected)

#button design: selected value from combobox and comparasion of selected value and actual currency
def button_clicked ():
    actual_value = currency_combobox.get()
    for i in response_from_web():
        if i["currency"] == actual_value:
            end_label.config(text ="{} $ ".format(i["price"]))
            break

button = tk.Button (text="Ok",command=button_clicked)
button.pack()

end_label = tk.Label(text="",font=("Arial", 20),pady=10)
end_label.pack()
windows.mainloop()
