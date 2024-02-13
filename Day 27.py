from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100,height=100)
window.config(padx=20,pady=20)

def m_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    km_result_label.config(text=f"{km}")

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=m_to_km)
calculate_button.grid(column=1,row=2)




window.mainloop()





# def add(*args):
#     a = 0
#     for i in args:
#         a += i
#     print(a)
# add(1,2,3,45)