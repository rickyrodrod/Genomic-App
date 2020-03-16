"""
03/16/2020 Ricky Rodriguez
Donato lab
The goal of this script is to:
    1. input a list of special strains (GSPR)
    2. execute query pan genome for each of the special strains against the susceptible
       strains in the same antibiotic (GSPS)
    3. move the .csv files to the correct folder in output
"""
import os

if __name__ == "__main__":
    run_auto_query()



def create_all_strains():
    """
    This function creates a list of all the .gff files in
    the current folder
    """
    allStrains = []
    for fileName in os.listdir(os.getcwd()):
        if fileName.endswith('.gff'):
            allStrains.append(fileName)
    return allStrains

def create_all_strains2(gsps):
    """
    This function creates the allStrains list by inputting a valid string
    in format: "filename.gff, next.gff, andSoOn.gff"
    """
    other_strains = gsps.strip().split(",")
    return other_strains

def create_file_path(specialStrains,antibiotic,file):
    """

    """
    currentDir = os.getcwd().split('/')
    del currentDir[-1]

    if len(specialStrains.split(',')) > 1:
        #group query
        newPath = currentDir[:]
        newPath.insert(3,'output')
        newPath.append(antibiotic)
        if file:
            newName = newPath[4][:5] + '_' + newPath[5] + '_group_statistics.csv'
            newPath.append(newName)
        newPath = '/'.join(newPath)
    else:
        #single query
        special = specialStrains.split('_')
        special = special[0]
        newPath = currentDir[:]
        newPath.insert(3,'output')
        newPath.append(antibiotic)
        newPath.append('individual')
        if file:
            newName = newPath[4][:5] + '_' + newPath[5] + '_' + special + '_stats.csv'
            newPath.append(newName)
        newPath = '/'.join(newPath)
    return newPath

def create_special_strains(special_string):
    #remove new line characters and split off antibiotic
    specialStrains = special_string.strip().split(",")
    return specialStrains

def execute_query(special, allStrains):
    """
    This function executes query_pan_genome from roary where special is a
    string of .gff files for set 1 and allStrains is a list of .gff files
    for set 2.
    """
    print('execute_query: called with {}'.format(special))
    #convert string of speical strains to list
    specialTemp = special.split(',')

    #eliminate special strains from allStrains by creating other
    other = []
    for i in range(len(allStrains)):
        match = False
        j = 0
        while not match and j < len(specialTemp):
            if allStrains[i] == specialTemp[j]:
                match = True
            else:
                j += 1
        #check why loop ended
        if not match and j >= len(specialTemp):
            other.append(allStrains[i])
    other = ','.join(other)
    os.system('query_pan_genome -a difference --input_set_one {} --input_set_two {}'.format(special,other))

def move_output(specialStrains,antibiotic):
    """
    This function inputs a string of strains separated by commas and moves the output
    from roary to the output file tree.
    create_file_path is called in this function
    """
    os.rename('set_difference_unique_set_one_statistics.csv',create_file_path(specialStrains,antibiotic,True))
    print('file moved to output folder')
def run_auto_query(antibiotic, organism, gspr, gsps):
    #1. prompt the user for special strains
    specialStrains = create_special_strains(gspr)
    #2. create a list of all strains
    allStrains = create_all_strains2(gsps)
    #3. for every item in specialStrains, execute query vs. other strains
    #   and move output file to correct dir
    for i in range(len(specialStrains)):

        execute_query(specialStrains[i][1], allStrains)
        filePath = create_file_path(specialStrains[i][1],specialStrains[i][0],False)
        if not os.access(filePath, os.R_OK):
            os.makedirs(filePath)
            print ('folder made at: {}'.format(filePath))
            move_output(specialStrains[i][1], specialStrains[i][0])
