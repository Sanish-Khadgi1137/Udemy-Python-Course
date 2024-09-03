"""#way of using code that other developers has written. Most commom way 
to do this is using pacakages of code, here will show integrating exisiting
 package of code in our project
 
 #search package on https://pypi.org/
 
 #packages have to be installed by  """
"""
#this will not run because there is not matplotlib installed in selected interpreter nor virtual environment 

import matplotlib.pyplot as plt

x = [24,25,26]
y = [23,24,25]

plt.plot(x,y)
plt.show()

#after creating virtual environment activate using new termial; on waiting few seconds there will
#  be update of "Scripts" folder of virtual enviroment which enable running vene

print("hello world")

"""






################################################3
"""
unable to activate virtual environment?
see window Powershell Execution policies 
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4

Make LocalMachine:RemoteSigned

if activated get name of venv before path
eg: (tutorial-env) PS C:\\Users\Salin\Desktop\codo\virtualenvironmenttes>
   
    #escape backslashs(additional backslash)at first of path to get rid of unicode error while commemting the path

here (tutorial-env) is name of virtual environment

now you can download packages to selected virtual environment

"""

"""
import matplotlib.pyplot as plt
#matplotlib was down loaded by running "pip install mathplotlib"

x = [24,25,26]
y = [23,24,25]

plt.plot(x,y)
plt.show()

"""

"""when virtual environment is installed to a folder it work for all the file of that folder
and show that virtual environment in interpreter if only you are inside that folder
and no need to select interpreter if there is venv(intalled package) in that folder; run 
in any interpreter 

see installed package inside (venv)\Library
"""

#using package pretytable
from prettytable import PrettyTable #"prettytable" is package and "PrettyTable" is class
#we can see source code of prettytable in library\prettytable

table=PrettyTable()#we make object "table"

#adding data into table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
#we access the "add_column" method from class "PrettyTable" through object "table" 

#accessing attribute "align" from class "PrettyTable"
table.align = "l"

print(table)