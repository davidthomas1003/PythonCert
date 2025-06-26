# PythonCert
This is where I will share my Notes and Assignments from my Python Certification

Notes:

--------------------------------------------------------------------------------------------------

Anaconda Intro:

Open anaconda prompt

conda deactivate - leaves base environment
conda activate   - enters base environment
python           - checks current python version
	>>> quit()   - leaves python interpreter

conda create --name py39 python=3.9  - creates a new environment named "py39" and changes the python version to 3.9
	conda activate py39 - activates this environment

conda list - shows all python packages installed in the base environment

conda install jupyter - installs the jupyter package
conda install notebook - installs the notebook package

python HelloPython.py - runs the python script "HelloPython.py


----------------------------------------------------------------------------------------------------

Jupyter Notebook Intro:

jupyter notebook - opens up jupyter notebook

Click "New" then click "Python [conda env:base] - opens up a new python file in base environment

Shift + Enter - Executes the current cell you are in
Enter  - creates another line

Jupyter notebook saves files as '.ipynb' you can download as '.py' by clicking "File" then "Save and Export Notebook As" then "Executable Script"

Markdown:
# sample text - makes it so the output text is bigger (multiple "#" can be inserted to make it smaller and smaller)

Code:
print('sample text') - prints sample text to screen
# sample text - allows for a single-line comment
'''sample 
text''' - allows for multi-line comment

----------------------------------------------------------------------------------------------------
Data Types:

PEMDAS is used in python
Integers - whole number, allows arithmetic operations
	ex. 2+2=4  10-2=8 3*2=6
	division can be either "/" (normal division) or "//" (which discards fractions and always rounds down)
	ex. 4/5=0.8  4//5=0
	remainder operator is "%" and will only give the reaminer back from divide
	ex. 15%5=3
	exponent operator is "**" and will exponent value
	ex. 2**2=4
Complex Numbers - represented by the sum of a real part and an imaginary part
	ex. 1+2j  10+13j  1.2+45.3j   where    j=-1
	"//" will not work with complex numbers
	"%" will not work with complex numbers
Boolean Types - Variables only take two values: True or False
	True = 1    False = 0
	Case sensitive: False is not false
	ex. 10==10 : True    7>10 : False    10>7 : True
	bool() function:
		rules:
			1) Any non-zero number is True
			2) Any non-empty string is True
			3) Any non-empty data structure is True
			4) Keywords False and None are False
		Is 7 True or False?  -->  its True
	
Useful Functions:
float(23) - converts 23 to 23.0 which is a float
int(24.9) - converts 24.9 to 24 which is an int
complex(2,3) - converts (2,3) to 2+3j which is a complex number
abs(-2.3) - returns the absolute value from -2.3 which is 2.3
divmod(10,3) - divids the number in parenthesis and returns the quotient and remainder which is (3,1)
pow(2,3) - returns 2 to the power of 3 which is 8
round(24.9) - round 24.9 to 25, this rounds both up and down

Variables: - Data changes in a python program and refers to an object which is any kind of datatype
	namespace: Keeps variables unique and are unique in their own namespace unless a namespace is called into another namespace
	naming rules: 
		Only letters, numbers and under-scores (_)
		Begin with letters and under-scores (no numbers)
		No spaces or special characters
		Case sensitive
		
		
--------------------------------------------------------------------------------------------------

Strings:
	String Creation:
		Single quotes:  'hello'
		ex. print('print this directly')
		Double quotes:  "hello"
		Triple-Single quotes: '''hello'''
		ex. print('''This is line1.
				This is line 2.''')
		Triple-Double quotes: """hello"""
		ex. a = """This is line 1.
				This is line 2.
				How are you doing"""
		\n - when inserted in a string will drop proceeding text to a new line
		\t - when inserted in a string will insert a tab
		a = 'How are y\'all doing?' - this allows for apostrophies to be added to text without exiting the string
		print('Cost\\nauticalmile') - allows for blackslash to be inserted
	String Index:
		a[0] = 'h'        a[-1] = 'o'
		a[1] = 'e'        a[-2] = 'l'
		a[2] = 'l'        a[-3] = 'l'
		a[3] = 'l'        a[-4] = 'e'
		a[4] = 'o'        a[-5] = 'h'
	String Manipulation:
		upper() \ lower() - are methods to chance case
		len() - gets the length of a string
		strip() - removes whitespace before and after a string
		replace() - replaces all or parts of a string
		split() - splits a string based on a seperator
		count() - method to count the number of occurences of a sub-string
		
		in \ not in - are keywords to determine if a sub-string exists
		slice: a[startIndex: endIndex]
			ex. a = 'Hello'
				a[1,4] -> 'ell'
		