# terminal_progressbar
**This library build to print progress bar in terminal program run on powershell, cmd, etc...**
**Showing the progress dynamically by steps**
________________________

 this library has one class ```PrintedProgressBar```,
 to initiate object from PrintedProgressBar class need one argument called "maximum="
 needed to detect the maximum number of steps
 this class has function "print_progress()" to start printing
 and function "step()" call it if a single step of your progress is done as follows:
 ```
object = PrintedProgressBar(maximum=n, bar_width=50)
object.print_progress()

for i in range(n + 1):
    time.sleep(0.01) 
    object.step()    # call it in ondition of one step of your work is completed
    
 ```