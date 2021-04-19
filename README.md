# Dataset_filter_sgems

## Object

The object of this program is to get datafiles that are ready to import in sgems.

	1. You start with your datafile as a text file seperated by tab.
	2. Ask some parameters from the user.
	3. Create folders to organize the data.
	4. Create different files per aquifer. A file for each hcov unit and a file for each head hcov unit.
	5. Create a file per aquifer file, that in the previous step was created, for each year that is present.
	6. If there are more than one value for the same filter, the mean is calculated (to consider multiple measurements per year)
	7. For each (x,y) location one value is calculated when for examples multiple filters have the same x and y coordinate but different depth of the filter
		- mindepth: work with the value that has the least depth
		- maxvalue: work with the maximum value of the parameter
	8. Create the file for sgems. Each line contains the x and y coordinate, the value of the parameter and the index number (to couple the extra data after the proces).
	9. Possibility to rerun the program.

## Input 

Which column contains the hcov code?

	Give the column number that contains the hcov code.
	
Which column contains the 'datum monstername'? 

	Give the column number that contains the ‘datum monstername’.
	
Which column contains the permkey value? 

	Give the column number that contains the permkey value.

Which column contains the As value? 
 	  
	Give the column number that contains the As value.

Which column contains the x value? 

	Give the column number that contains the x value.

Which column contains the y value? 

	Give the column number that contains the y value.

Which column contains the z value? 

	Give the column number that contains the z value, the depth of the filter.

Are there already maps? 

	This asks if there are already folders with the filtering of the dataset. If it’s the first time you run the project, answer with ‘no’. Otherwise answer ‘yes’.

Which is the input file? 

	Give the path of the dataset. The program is tested for a text input file with a tab as separator. 
 
 	1. Select the txt dataset
  
	2. Press ‘Pad kopiëren’ in the menu of the folder
 	  
	3. Paste it in the terminal where you run the program 

From which file do you want to make a kriging map? (aquiferall/aquiferheadhcov-year) 
  
	Give the name of the file.

Do you want to work with mindepth or maxvalue? 
  
	If you want to work with the value that has the lowest depth at the same (x,y) location you choose mindepth.
  
	If you want to work with the max value at the same (x,y) location you choose maxvalue.

Do you want to make a second map? If yes, from which file? If no, type no. 
  
	If yes, then give the name of the file.
  
	If no, type no.

Do you want to work with mindepth or maxvalue? 
  
	If you want to work with the value that has the lowest depth at the same (x,y) location you choose mindepth.
  
	If you want to work with the max value at the same (x,y) location you choose maxvalue.
