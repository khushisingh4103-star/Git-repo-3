# Functionality of programs 
In the 1st program, in try block the file "sample.txt" is opened in read mode.
And then the content of the file is printed via for loop by traversing over the content of file line by line.
In the except block, error message is written which will be printed as an output when the file is not found or if it does not exist. 

In the second program, firstly, a variable "text" is created to store the text entered by the user to wrote to the file.
And then the file is opened in write mode & write() function is used to write the user entered text inside the file.
After this another variable "add_text" is created to store the additional text entered by the user to write to the file.
Then this file is opened in append mode & again write() function is used to enter the additional text inside the file.\
Lastly, the file is opened in read mode & then the content of the file is stored inside another variable named "content" & is displayed as the final output.
