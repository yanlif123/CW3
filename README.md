# CW3
This project codes for a Sudoku Solver. The code solves unsolved grids from an inputted file through terminal, as well as example grids included within the script.

<sub> By Charlie Creasy, Finlay, Oliver F, Jyotika Kannan </sub>


### Algorithms
The Solver contains three main methods for the solving of a grid, using three main functions:

 -**recursive_solve()**:\
This function uses the method of finding the empty location in the grid with the least possible values for that location through comparing the possible values with other known locations in the same row, column, or square. THrough this comparison, many possible values for each cell are eliminated, and reduces the number of recursions neccesary. This increases the solvers efficiency. This method is then repeated exhaustedly iterating through all possible solutions, until a solved grid is found and returned.

 -**wavefront()** or **list_solve()**:\
Wavefront uses the wavefront propogation method, where we find the locations in the grid with the least possible values, i.e. one possible value - as these values are placed in their locations in the grid, they are simultaneously elimated from the list of possible values for other unknown cells in the same row, column or square. This process is then repeated until a solved grid found, and returned.

 -**main()**:\
The function main extends the recursive_function for the user. Through this funtion, the user can call for the following flags:  **-explain**', **- file input output**, **-hint N**, and **-profile**. These flags can be run simultaneously.
  Individually, when the flags are called:
  - **explain**   
    prints the solution to the inputted grid and a set of instructions for solving the puzzzle
  - **file input output**  
    reads a grid from an inputted file, solves the grid, and saves the grid to another file named 'OUTPUT'.
  - **hint N**   
    returns a partially filled grid by 'N' number of values.
  - **profile** 
    measures the time performance of the solver, for grids of various sizes and difficulties. It then averages the performance of the solver, summarises the results and returns a plot conveying these results.
  
  
### Usage

1) To choose the algorithm with which to solve the grid:
    - open python script
    - edit within the function 'solve()':
      - for the **recursive** method: uncomment 'return recursive_solve(...)'. comment out other return lines for the 'solve' function \
      - for the **wavefront** method: uncomment either 'return wavefront(...)', or 'return list_solve(...)'. comment out the other two return lines under            the 'solve' function
        
        
2) Run the file from terminal. 


3) To call for a flag:

    In terminal, print "CW3.py -flag inputfile.txt output.txt"
    
    i.e.\
    -for **explain**  (to print solution and set of instructions to solve):\
     In terminal, print "CW3.py -explain inputfile.txt output.txt
     
    -for **file INPUT OUTPUT**  (to read sudoku grid from inputted file and save solved grid to output file):\
     In terminal, print "CW3.py -file input.txt output.txt"
     
     -for **hint N**  (return a grid filled with *n* previously unknown locations):\
     In terminal, print "CW3.py -hint N input.txt output.txt"\
     e.g. for a number of 5 hints:\
     In terminal, print "CW3.py -hint 5 input.txt output.txt"
     
     -for **profile**  (measure time performance for solver over various grids, return a plot of average performance):\
     In terminal, print "CW3.py -profile input.txt output.txt"
     
     
 4) To call for multiple flags:
 
    In terminal, the desired flags must be called in this order:\
    -hint  -explain  -file 
    
    i.e.\
     -for hint + file:\
      print "CW3.py -hint 5 -file input.txt output.txt'
      
     -for hint + explain:\
      print "CW3.py -hint 5 -explain input.txt output.txt"
      
     -for explain + file:\
      print "CW3.py -explain -file input.txt output.txt'
      
     -for hint + explain + file\
      print "Script.py -hint 5 -explain -file input.txt output.txt'
        
        
       
        
  

  
  
