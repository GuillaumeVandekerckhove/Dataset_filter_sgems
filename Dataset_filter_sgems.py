import pandas as pd
import numpy as np
import os
import glob

#Get the path of the project
outputfile = os.getcwd()

#Ask the different parameters from the user
column = input("Which column contains the hcov code? ")
column2 = input("Which column contains the 'datum monstername'? ")
pk = input("Which column contains the permkey value? ")
As = input("Which column contains the As value? ")
x = input("Which column contains the x value? ")
y = input("Which column contains the y value? ")
z = input("Which column contains the z value? ")
folder = input("Are there already maps? ")
inputfile = input("Which is the input file? ")

#Make an integer of the input numbers
column = int(column)
column2 = int(column2)
pk = int(pk)
As = int(As)
x = int(x)
y = int(y)
z = int(z)

#Make some adaptions to the pathline
inputfile = inputfile.replace("\\", "/")
inputfile = inputfile.replace('"', '')
outputfile = outputfile.replace("\\", "/")
outputfile = outputfile.replace('"', '')


def maps():
    """Create the folders to organize the data.

    If it's the first time you run the program, different folders are created to organize the data in the future
    steps.
    The different folders are;
    aquiferall - contains the data per aquifer code
    aquiferhead - contains the data per head aquifer unit, for example hcov 0100, 0110, 0120, 0130, 0131, 0132, ...
                  is grouped in the aquifer code 100)
    year - contains the data per year for each file in the folder aquiferall and aquiferhead
    results - contains the error file and the results file per year (per filter there is one value)
    results 2d - contains the 2d datasets (one value per x,y location) with also the file that will be used as input in
                 pysgems.
    """

    if folder == "no":
        os.mkdir("aquiferall")
        os.mkdir("aquiferhead")
        os.mkdir("year")
        os.mkdir("results")
        os.mkdir("results2d")
    else:
        None

def read_col(fname, col, convert, sep='\t'):
    """Read text files with columns separated by `sep`.

    fname - file name
    col - index of column to read
    convert - function to convert column entry with
    sep - column separator
    If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.
    """
    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

def fileperaquifer():
    """Create the different aquifer files."""
    res = read_col(inputfile, column, int)
    unique = set(res)
    unique = sorted(unique)

    # Remove the first 0: 0100 -> 100
    for i in unique:
        if len([i]) > 2:
            unique = [str(i).lstrip('0')]

    def name_list():
        """Get the name for the file from the file that contains all the hcov codes.

        Return:
        name - aquifercode

        """

        file = open('C:/Users/guill/Documents/UGent/stage_dov_2021/Data/hcov_code/HCOV-versie1.txt', 'r') # open the file that contains all the hcov codes
        lines = file.readlines() # run through all the different lines
        for line in lines: # select one line, than the next, ...
            parts = line.split(sep='\t')  # split line into parts
            aquiferCode = parts[0] # get the aquifercode
            if i == int(aquiferCode): # if the aquifer code of the inputfile is the same as the aquifercode of the total list of aquifercodes, then the name is that aquifer code
                name = parts[0]
                return name
        file.close()


    file = open(inputfile, 'r')
    lines = file.readlines()
    # make a list with all the lines with the same aquifer code
    for i in unique:
        list1 = []
        name_list()
        for line in lines:
            parts = line.split()
            aquiferCode = parts[column]
            if i == int(aquiferCode):
                list1.extend([line])
        # save the list with each element as a different line, for each element in unique there is a different file
        np.savetxt(outputfile + '/aquiferall/' + name_list()+'.txt', list1, delimiter="\n", fmt="%s")
    file.close()

    file = open(inputfile, 'r')
    lines = file.readlines()
    # create the files per aquifer head unit
    for i in unique:
        list2 = []
        i = str(i)
        if len(i) == 1:
            name = '0'
            for line in lines:
                parts = line.split()
                aquiferCode = parts[column]
                aquiferCode = str(aquiferCode)
                if len(aquiferCode) == 1:
                    aquiferCode = aquiferCode.lstrip('0')
                    if len(i) == 1:
                        if i[0:1] == aquiferCode[0:1]:
                            list2.extend([line])
            np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
        if len(i) == 3:
            if i[0:1] == '1':
                name = '100'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:1] == '2':
                name = '200'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:1] == '3':
                name = '300'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:1] == '4':
                name = '400'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:1] == '5':
                name = '500'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:1] == '6':
                name = '600'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:1] == '7':
                name = '700'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:1] == '8':
                name = '800'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:1] == '9':
                name = '900'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 3:
                            if i[0:1] == aquiferCode[0:1]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
        if len(i) == 4:
            if i[0:2] == '10':
                name = '1000'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 4:
                            if i[0:2] == aquiferCode[0:2]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:2] == '11':
                name = '1100'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 4:
                            if i[0:2] == aquiferCode[0:2]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:2] == '12':
                name = '1200'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 4:
                            if i[0:2] == aquiferCode[0:2]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
            if i[0:2] == '13':
                name = '1300'
                for line in lines:
                    parts = line.split()
                    aquiferCode = parts[column]
                    aquiferCode = str(aquiferCode)
                    if len(aquiferCode) > 2:
                        aquiferCode = aquiferCode.lstrip('0')
                        if len(aquiferCode) == 4:
                            if i[0:2] == aquiferCode[0:2]:
                                list2.extend([line])
                np.savetxt(outputfile + '/aquiferhead/' + name + '.txt', list2, delimiter="\n", fmt="%s")
    file.close()

def fileperaquiferperyear():
    """Create a file per year per aquifer code."""
    datafiles1 = glob.glob("C:/Users/guill/Documents/UGent/stage_dov_2021/Data/vmm/Data_kempen/aquiferall//*.txt") # all the files in the folder aquiferall
    datafiles2 = glob.glob("C:/Users/guill/Documents/UGent/stage_dov_2021/Data/vmm/Data_kempen/aquiferhead//*.txt") # all the files in the folder aquiferhead
    def joinStrings(stringList):
        """Add strings together to get one string."""
        return ''.join(string for string in stringList)

    datafilesperaquifer = []
    # create a list with all the datafiles per aquifer
    for i in datafiles1:
        result1 = [a.replace('\\','/', 1) for a in i]
        result1 = joinStrings(result1)
        datafilesperaquifer.extend([result1])
    for i in datafiles2:
        result2 = [a.replace('\\', '/', 1) for a in i]
        result2 = joinStrings(result2)
        datafilesperaquifer.extend([result2])


    for i in datafilesperaquifer:
        inputfile2 = i
        # create the name for the file (aquiferhead or aquiferall + aquifercode)
        nameinput = i[-19:-4]
        nameinput = [a.strip('/') for a in nameinput]
        nameinput = [a.replace('/', '-', 1) for a in nameinput]
        nameinput = joinStrings(nameinput)


        open(outputfile + '/inputfile2', 'w').close() # create a temporary file

        # If the line of the file per aquifer code isn't empty and longer than 1 character, then the line is added to the temporary file (to avoid the empty lines)
        for line in open(inputfile2):
            if len(line) > 1 or line != '\n':
                with open("inputfile2", 'a') as file2:
                    file2.write(line)

        inputfile2 = outputfile + '/inputfile2'
        inputfile2 = inputfile2.replace("\\", "/")
        inputfile2 = inputfile2.replace('"', '')

        res = read_col(inputfile2, column2, str)

        def year():
            """Get the year per aquifer code

            Return:
            unique - a unique list of the years that occur in the temporary file (so the unique years per aquifer code)
            """
            list3 = []
            for i in res:
                result = [a.strip('/') for a in i]
                result = result[-4] + result[-3] + result[-2] + result[-1]
                list3.extend([result])
            unique = set(list3)
            unique = sorted(unique)
            return unique

        list4 = year()


        file = open(inputfile2, 'r')
        lines = file.readlines()
        # create a list with all the lines from that specific year
        for i in list4:
            name = i
            list5 = []
            for line in lines:
                parts = line.split(sep='\t')
                datum_monstername = parts[column2]
                datum_monstername = [a.strip('/') for a in datum_monstername]
                result = datum_monstername[-4] + datum_monstername[-3] + datum_monstername[-2] + datum_monstername[-1]
                if i == result:
                    list5.extend([line])
                    #save the file that contains the data with the same aquifercode and the same year
                    np.savetxt(outputfile + '/year/' + nameinput + '-' + name + '.txt', list5, delimiter="\n", fmt="%s")
        file.close()

def results(naam,mindepthormaxvalue):
    """Create the result files.

    naam: aquiferall/aquiferheadhcov-year
    mindepthormaxvalue: mindepth = work with the value of the filter that is the undeepest
                        maxvalue = work with the maximum value of the filter

    """
    map = outputfile + '/year'
    inputfile3 = map + '/' + naam + '.txt'

    # create a temporary file to avoid the empty lines
    open(outputfile + '/inputfile3', 'w').close()
    for line in open(inputfile3):
        if len(line) > 1 or line != '\n':
            with open("inputfile3", 'a') as file3:
                file3.write(line)
    inputfile3 = outputfile + '/inputfile3'
    inputfile3 = inputfile3.replace("\\", "/")
    inputfile3 = inputfile3.replace('"', '')

    respk = read_col(inputfile3,pk, str)  # get the values for the permkey
    resas = read_col(inputfile3,As, str)  # get the values for As

    unique = set(respk)  # get the unique permkeys

    file = open(inputfile3, 'r')
    lines = file.readlines()
    ind2 = list(range(0, len(respk)))  # get a list with a large range, starting at 0
    list6 = []
    error = []
    result = []
    for i in unique:
        # create a list with elements that have the same permkey
        list7 = []
        for line in lines:
            parts = line.split()
            permkey = parts[pk]
            if i == permkey:
                list7.extend([line])
        res = [i.strip("'").split("\t") for i in list7]

        if len(list7) > 1:  # if there are more than one value with the same permkey
            list6 = []
            # create a list with #elements of list 7 = [0,1,...]
            for j in ind2:
                if j <= len(list7):
                    list6.extend([j])
            list6 = list6[:-1]
            # create a list with the values for As
            valueAslist = []
            for k in list6:
                valueAs = res[k][As]  # get the value for As
                if valueAs == '':
                    error.extend([res[k]])
                else:
                    valueAslist.extend([float(valueAs)])
            # Get the mean of the As values with the same permkey
            if valueAslist != []:
                total = 0
                for ele in range(0, len(valueAslist)):
                    total = total + valueAslist[ele]
                mean = total/len(valueAslist)
                res[0][As] = mean  # replace (in the first element of the list) the value of As with the mean value
                result.extend([res[0]])  # extend the result list with the first element of list that contains the mean value for As
        else: # if there is only one solution per permkey
            res = res[0]
            result.extend([res])

    np.savetxt(outputfile + '/results/' + naam + 'results_fullyear'+'.txt', result, delimiter="\t", fmt="%s")  # save a file with the results
    np.savetxt(outputfile + '/results/' + naam + 'error_fullyear'+'.txt', error, delimiter="\t", fmt="%s")  # save a file with the errors

    inputfile4 = outputfile + '/results/' + naam + 'results_fullyear.txt'
    inputfile4 = inputfile4.replace("\\", "/")
    inputfile4 = inputfile4.replace('"', '')

    # create a temporary file to avoid the empty lines
    open(outputfile + '/inputfile4', 'w').close()
    for line in open(inputfile4):
        if len(line) > 1 or line != '\n':
            #print(line, end='')
            with open("inputfile4", 'a') as file4:
                file4.write(line)
    inputfile4 = outputfile + '/inputfile4'

    resx = read_col(inputfile4,x,str)
    resy = read_col(inputfile4,y,str)
    resz = read_col(inputfile4,z,str)
    resas = read_col(inputfile4,As,str)
    lengthx = len(resx)
    lengthy = len(resy)
    lengthz = len(resz)
    lengthas = len(resas)
    ind = list(range(0, lengthx))  # get a list with the range of coordinates, starting at 0
    # create a list with coordinates
    coordinatesxy = []
    for i in ind:
        xy = resx[i] + ' ' + resy[i]
        coordinatesxy.extend([xy])
    unique = set(coordinatesxy)
    unique = list(unique)

    file = open(inputfile4, 'r')
    lines = file.readlines()
    ind2 = list(range(0, len(coordinatesxy)))  # get a list with a large range, starting at 0
    list8 = []
    error = []
    result = []

    def mindepth():
        """If there are more than one As value with the same x and y coordinate,
        the value of As is used with the minimun depth."""
        depthlist = []
        for k in list8:
            depth = res[k][z]
            if depth == '':
                print('error')
                error.extend([res[k]])
            else:
                depthlist.extend([float(depth)])

        if depthlist != []:
            minimum = min(depthlist)
            for k in list8:
                depth = res[k][z]
                if float(depth) == minimum:
                    result.extend([res[k]])
                    break

    def maxvalue():
        """If there are more than one As value with the same x and y coordinate,
        the value of As is used with the maximum value for As."""
        valuelist = []
        for k in list8:
            value = res[k][As]
            if value == '':
                print('error')
                error.extend([res[k]])
            else:
                valuelist.extend([float(value)])

        if valuelist != []:
            maximum = max(valuelist)
            for k in list8:
                value = res[k][As]
                if float(value) == maximum:
                    result.extend([res[k]])
                    break


    for i in unique:
        # create a list with the values that have the same x and y coordinate
        list9 = []
        for line in lines:
            parts = line.split()
            xy = parts[x] + ' ' + parts[y]
            if str(i) == xy:
                list9.extend([line])
        res = [i.strip("'").split("\t") for i in list9]

        # create a list with the depths of the points and a list with the solutions sorted for depth
        depthlist1 = []
        sorted1 = []
        for i in res:
            depth1 = i[z]
            if depth1 == '':
                sorted1.extend([i])
            else:
                depthlist1.extend([float(depth1)])
        if depthlist1 != []:
            sorteddepth = sorted(depthlist1)
            for i in sorteddepth:
                for j in res:
                    depth2 = j[z]
                    if float(depth2) == i:
                        sorted1.extend([j])
                        break
        res = sorted1


        if len(list9) == 1:  # if there is only one solution for the xy coordinate, than this is the solution
            result.extend([res[0]])
        if len(list9) > 1:  # if there are more than one solution for the xy coordinate
            list8 = []
            for j in ind2:
                if j <= len(list9):
                    list8.extend([j])
            list8 = list8[:-1]
            if mindepthormaxvalue == "mindepth":
                mindepth()
            if mindepthormaxvalue == "maxvalue":
                maxvalue()


    np.savetxt(outputfile + '/results2d/' + naam + mindepthormaxvalue + 'results2d'+'.txt', result, delimiter="\t", fmt="%s")  # save a file with the results
    np.savetxt(outputfile + '/results2d/' + naam + mindepthormaxvalue + 'error2d'+'.txt', error, delimiter="\t", fmt="%s")  # save a file with the errors

    file.close()

def fileforsgems(mindepthormaxvalue):

    inputfile5 = outputfile + '/results2d/' + naam + mindepthormaxvalue + 'results2d.txt'
    inputfile5 = inputfile5.replace("\\", "/")
    inputfile5 = inputfile5.replace('"', '')

    # create a temporary file to avoid the empty lines
    open(outputfile + '/results2d_sgems', 'w').close()
    for line in open(inputfile5):
        if len(line) > 1 or line != '\n':
            with open("results2d_sgems", 'a') as file5:
                file5.write(line)

    # create a new filtered file where each line contains only the x, y, As and index value
    inputfile4 = outputfile + '/results2d_sgems'
    file = open(inputfile4, 'r')
    lines = file.readlines()
    list10 = []
    for line in lines:
        parts = line.split("\t")
        newline = parts[6] + ' ' + parts[7] + ' ' + parts[21] + ' ' + parts[0]
        list10.extend([newline])
    np.savetxt(outputfile + '/results2d/' + naam + mindepthormaxvalue + 'results2d_sgems'+'.txt', list10, delimiter="\n", fmt="%s")

    rerun = input("Do you want to make a second map? If yes, from which file? If no, type no. ")  # ask the filename that contains the data if the user want to make another map
    mindepthormaxvalue = input("Do you want to work with mindepth or maxvalue? ")  # ask which values have to be used
    # If the answer isn't no, the program is executed again
    if rerun != "no":
        results(rerun, mindepthormaxvalue)
        fileforsgems(mindepthormaxvalue)

# run the program
maps()
fileperaquifer()
fileperaquiferperyear()

naam = input("From which file do you want to make a kriging map? (aquiferall/aquiferheadhcov-year)  ")  # ask the filename that contains the data
mindepthormaxvalue = input("Do you want to work with mindepth or maxvalue? ")  # ask which values have to be used

results(naam,mindepthormaxvalue)
fileforsgems(mindepthormaxvalue)
