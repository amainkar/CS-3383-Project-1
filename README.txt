Group: Atharva Mainkar, Jaziel Contreras, Andrew Garcia, Juan Avalos

INSTRUCTIONS TO COMPILE PYTHON FILE TO BINARY EXECUTABLE

Some Basic assumptions:

You are on Windows

You have Python installed

You have pip installed,(comes with python installation)

You have Administrator privilages on your machine

The text file to scan is in the same directory as the python file

Instructions:

1.Go to the search bar and type in cmd (command prompt).
2.Open the command prompt using administrator privilages.
3.Navigate to your desired dirctory where the python file exists.
4.Run the following command "pip install pyinstaller"
5.Let pip completely install the package.
6.Then run the command "pyinstaller --oneflag runNFA.py" in the command prompt.
7.Let it complete running.
8.In your directory, there will be a folder called "dist".
9.Copy the "runNFA.exe" application from "dist" to the directory where the textfile exists.
10.Then from within the comamnd prompt type in "runNFA" and press enter.