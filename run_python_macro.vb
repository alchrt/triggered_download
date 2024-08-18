Sub python_file_update()

' This macro follows the solution applied in this post: https://waterprogramming.wordpress.com/2022/03/29/running-a-python-script-using-excel-macros/

' Declaring all variables
Dim objShell As Object
Dim PythonExe, PythonScript As String

    ' Creating a new Shell Object
    Set objShell = VBA.CreateObject("Wscript.shell")
    
    ' Path to the Python Exe and script
    PythonExe = """C:\...\python.exe"""     ' path to the Python Exe file
    PythonScript = """C:\...\python-script.py"""     ' path to the Python script: either """C:\...\csv_download.py""" or """C:\...\processed_csv.py"""
    
    ' Running the Python script
    objShell.Run PythonExe & PythonScript
    Application.Goto Reference:="python_file_update"
    
End Sub
