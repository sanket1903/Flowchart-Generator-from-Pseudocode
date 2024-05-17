# Flowchart-Generator-from-Pseudocode
Generates Flowcharts directly from Pseudocode!

![image](https://github.com/sanket1903/Flowchart-Generator-from-Pseudocode/assets/98966681/d933cc9d-4e60-430c-87c5-c0ccf28d1cce)
# Local Installation
This project was built on Python 3.12.2

Run this to install the necessary dependencies:
pip install Pillow==9.0.0 

# Writing the Pseudocode
The Pseudocode is entered into a .txt file. It follows strict rules which must be obeyed

![Screenshot (341)](https://github.com/sanket1903/Flowchart-Generator-from-Pseudocode/assets/98966681/e8eb6b1c-861e-4e8d-8194-663985858931)

## Rules
STOP and START are automatically input by the program, so do not need to be added

Indents don't affect the program, so nothing has to be indented, and incorrect indentation is allowed

The capitalization of the keywords is extremely important. If an error occurs, double check if you have capitalized the keywords like "TO" and "FOR" properly

ELSE IF is not available, but nested IFs are possible

The ENDIF, NEXT var, and ENDWHILE blocks are mandatory

# Syntax Guide
## Input and Output:

INPUT x

OUTPUT x


INPUT X

OUTPUT var

OUTPUT "hello"

## IF statements:

IF condition THEN

ELSE

ENDIF

IF x < 3 THEN

  OUTPUT X
  
ELSE

  OUTPUT x*2
  
ENDIF

The else statement is optional (ENDIF is still necessary)

IF x < 3 THEN

 OUTPUT X
 
ENDIF

## Process-type blocks:

x = x + 1

y = x / 2


## While loops:

WHILE condition DO

ENDWHILE

WHILE x < 5 DO

  OUTPUT x
  
ENDWHILE


## For loops:

FOR var <- start TO end

NEXT var

FOR i <- 1 TO 5

  OUTPUT i
  
NEXT i



# CLI usage

To run the code, simply execute the following command:

python Converter.py


## Arguments

Arguments in the CLI are typed like so: --size=20 or --code="enter.txt"

--size is the font size used. This controls the size of the entire flowchart as well. By default it is 20px
--font is the font path. A default NotoSans font is used at "./fonts/", but can be changed for different OSs or fonts
--output is the flowchart's image file. Default is "flowchart.png"
--code is the file with the pseudocode. Defaults to "enter.txt"
--help provides CLI help

For example:

python Converter.py --code="code.txt" --size=30 --output="result.png"







