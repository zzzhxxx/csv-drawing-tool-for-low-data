import csv
import win32ui
from matplotlib import pyplot as plt
dlg = win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir('E:/Python') 
dlg.DoModal()
filename = dlg.GetPathName() 
with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates,ch1 = [],[]
        for row in reader:
            dates.append(row[0])
            ch1.append(row[1])
fig = plt.figure(dpi=64, figsize=(20,12))
x_values=dates
y_values=ch1
plt.plot(x_values,y_values,c='red')
plt.title("CSV", fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel("", fontsize=16)
plt.tick_params(axis='both', which="major", labelsize=16) 
plt.show()
