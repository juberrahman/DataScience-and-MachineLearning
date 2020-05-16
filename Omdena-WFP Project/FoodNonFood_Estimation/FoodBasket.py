import tkinter as tk

fields = ('Total No. of Affected People', 'How many are pregnant', 'How Many Are Lactating Mother',
          'How many are children below age 10','Affected Area Temperature (C)', 'Total Rice (kg)','Total Lentil (Kg)',
          'Total Oil (Kg)','Total Salt (Kg)')

def total_calories(entries):
    kcal=0.0
    # total affected:
    total_affected=0
    total_affected = float(entries['Total No. of Affected People'].get())
    print("tot_aff", total_affected)
    # compute the total calorie need
    kcal= total_affected * 2100
    # get other factors
    pregnant=0
    lactating=0
    children =0
    pregnant = float(entries['How many are pregnant'].get())
    lactating= float(entries['How Many Are Lactating Mother'].get())
    children= float(entries['How many are children below age 10'].get())
    adj_kcal=kcal+pregnant * 500 + lactating * 250+children*0
    # get temperature
    temperature=float(entries['Affected Area Temperature (C)'].get())
    if temperature <20:
      temp_adj_kcal=adj_kcal+100*(20-temperature)/5
    entries['Total Rice (kg)'].delete(0, tk.END)
    entries['Total Rice (kg)'].insert(0, round(temp_adj_kcal/(1000*1.3*3.63),2))
    entries['Total Lentil (Kg)'].delete(0, tk.END)
    entries['Total Lentil (Kg)'].insert(0, round(temp_adj_kcal/(1000*26.99),2))
    entries['Total Oil (Kg)'].delete(0, tk.END)
    entries['Total Oil (Kg)'].insert(0, round(temp_adj_kcal/(1000*63.0),2))
    entries['Total Salt (Kg)'].delete(0, tk.END)
    entries['Total Salt (Kg)'].insert(0, round(temp_adj_kcal/(1000*375.0),2))


def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=32, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Get Food Basket',
           command=(lambda e=ents: total_calories(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()