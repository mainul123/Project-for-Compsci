# Project-for-Compsci
Final Project for Compsci 127, by Mainul Nishan and Myles Austin

### Topic: Choice 1
Working with inverted indexes developed from files. 

### Intended Extension(s):
 - Using a graph library to provide visualizations
 - Storing and utilizing word information (i.e., position, occurrences)
 - Word Stemming
### Test instructions/information
  - If not already present run: sudo apt-get install python3-matplotlib 
  OR install matplotlib into your environment.
  - The main packages used are: numpy 1.13.3,  matplotlib 2.1.1
  - A majority of testing was performed in Thonny, with the required package installed.
  - THE FILE TO BE RUN IS TITLED 'projecttests.py'.
  - The file also uses the following csv's: english.csv, finaldata.csv
  
  - Please note that due to the size of the finaldata.csv's information, the stemming process may be slow.
  - Upon running the file, first the iindex will be made, then the iindex will be stemmed, then the graph will be generated.
  - The graph will show the frequency of a word in the songs in finaldata.csv, vs. the respective artist.
  - When reaching the last step, the program will as for user input in the form of a single word.
  - This word will be the one used in the formation of the graph, using the iindex as information.
  - In addition, the artists and the occurrences will be printed just before the graph is generated, in case something goes
  wrong with the matplot library. 
  
### Languages/Formats to be used:

 - Python
 - CSV Tables

### Project Description

In this project, we aim to use the designs and techniques we have learned already regarding inverted indices, and expand upon them. We aim to add several features to the functions, including a stemming algorithm, graphs, and word information storage. It is in the realm of possibility that we might add supplementary features, such as formatting in Flask or the deciphering of other file types.

