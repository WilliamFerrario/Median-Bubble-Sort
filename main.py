import tkinter as tk
from tkinter import messagebox

#sort using bubble sort & get median
def sortAndFindMedian(numbers):
    sort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]

#implementation of bubble sort
def sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

#execute on ui button
def process():
    try:
        #split input by commas for array
        numberList = list(map(int, entry.get().split(',')))
        median = sortAndFindMedian(numberList)
        messagebox.showinfo("Result", f"Sorted Numbers: {numberList}\nMedian: {median}")
    except ValueError:
        messagebox.showerror("Error!", "Enter valid integers separated by commas...")

#main tkinter window
root = tk.Tk()
root.title("Number Array Input")

#entry widget
entry = tk.Entry(root, width=50)
entry.pack()

#process input
processButton = tk.Button(root, text="Enter Numbers Seperated by a comma", command=process)
processButton.pack()

#ui loop
root.mainloop()
