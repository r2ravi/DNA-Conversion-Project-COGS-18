"""A collection of functions for doing my project."""

def string_concatenator(string1, string2):
    """Combines strings together by adding them and returning the combination as an output.
    
    
    Parameters
    ----------
    string1 : string
        String that will be added to another string.
        
    string2 : string
        String that will be added to another string.
        
        
    Returns
    -------
    output : string
        String that combines both input strings, string1 and string2 with "+" operation.
    """
    
    # Saves sum of string1 and string2 to output variable
    output = string1 + string2

    # Output variable is returned by function
    return output


def DNA_to_mRNA_List(DNA_string):
    """Takes in DNA sequence string and converts it to an mRNA list.
    
    
    Parameters
    ----------
    DNA_string : string
        String that contains letters/characters of a DNA string, e.g., 'a,' t,' 'c,' and 'g.'
        
        
    Returns
    -------
    mRNA_List : list
        List that converts each and every value in input to corresponding mRNA values.
    """
    
    # Creates an empty list to which values will be appended
    mRNA_List = [];
    
    # Loops through each character of DNA string input
    for char in DNA_string:
        
        if char == 'a' or char == 'A': 
            # Characters are appended to mRNA_List 
            mRNA_List.append('U')
            
        elif char == 't' or char == 'T':
            mRNA_List.append('A')
            
        elif char == 'c' or char == 'C':
            mRNA_List.append('G')
            
        elif char == 'g' or char == 'G':
            mRNA_List.append('C')
            
    # Output mRNA_List is returned by function 
    return mRNA_List


def DNA_to_mRNA(DNA_string, separator): 
    """Takes in DNA sequence string and converts it to an mRNA string, with separation character
        in between every three characters of the string.
    
    
    Parameters
    ----------
    DNA_string : string
        String that contains letters/characters of a DNA string, e.g., 'a,' t,' 'c,' and 'g.'
        
    separator : string/character
        Character that will be inserted in between every three elements of mRNA string, e.g.,
        '-', ',', etc.
        
        
    Returns
    -------
    mRNA : string
        String that is formed by combining each element of the mRNA list of elements, along with
        a separator chosen (input by the user) between every three elements of the sequence.
    """
    
    # Previous function, DNA_to_mRNA_List() is called on to get values for mRNA_List in this 
    # function
    mRNA_List = DNA_to_mRNA_List(DNA_string)
    
    # String is initialized under variable mRNA_initial 
    mRNA_initial = mRNA_List[0]
    
    # Each element of mRNA list is looped through
    for sequence_element in mRNA_List[1:]:
        
        # Previous function, string_concatenator(), is used as each element is looped through
        mRNA_initial = string_concatenator(mRNA_initial, sequence_element)
        
    # The final output is produced by inserting the chosen separator using separator.join()
    mRNA = separator.join([mRNA_initial[i:i+3] for i in range(0, len(mRNA_initial), 3)])
        
    # Output mRNA is returned by function
    return mRNA


def DNA_to_tRNA_List(DNA_string):
    """Takes in DNA sequence string and converts it to a tRNA list.
    
    
    Parameters
    ----------
    DNA_string : string
        String that contains letters/characters of a DNA string, e.g., 'a,' t,' 'c,' and 'g.'
        
        
    Returns
    -------
    tRNAList : string
        List that converts each and every value in input to corresponding tRNA values.
    """
    
    # Previous function, DNA_to_mRNAList() is called on to get mRNA_List for conversion to tRNA
    mRNA_List = DNA_to_mRNA_List(DNA_string)
    
    # Creates an empty list to which values will be appended
    tRNA_List = []
    
    # Each element of mRNA_List is looped through
    for char in mRNA_List:
        
        if char == 'a' or char == 'A':
            # Characters are appended to tRNA_List
            tRNA_List.append('U')
            
        elif char == 'u' or char == 'U':
            tRNA_List.append('A')
            
        elif char == 'c' or char == 'C':
            tRNA_List.append('G')
            
        elif char == 'g' or char == 'G':
            tRNA_List.append('C')
            
    # Output tRNA_List is returned by function
    return tRNA_List


def DNA_to_tRNA(DNA_string, separator):
    """Takes in DNA sequence string and converts it to an mRNA string, with separation character
        in between every three characters of the string.
    
    
    Parameters
    ----------
    DNA_string : string
        String that contains letters/characters of a DNA string, e.g., 'a,' t,' 'c,' and 'g.'
        
    separator : string/character
        Character that will be inserted in between every three elements of mRNA string, e.g.,
        '-', ',', etc.
        
        
    Returns
    -------
    tRNA : string
        String that is formed by combining each element of the tRNA list of elements, along with
        a separator chosen (input by the user) between every three elements of the sequence.
    """
    
    # Previous function, DNA_to_tRNA_List is called on
    tRNA_List = DNA_to_tRNA_List(DNA_string)
    
    # String is initialized under tRNA_initial variable
    tRNA_initial = tRNA_List[0]
    
    # each element of tRNA_List is looped through
    for sequence_element in tRNA_List[1:]:
        
        # Previous function, string_concatenator, is used as each element is looped through
        tRNA_initial = string_concatenator(tRNA_initial, sequence_element)
    
    # The final output is produced by inserting the chosen separator using separator.join()
    tRNA = separator.join([tRNA_initial[i:i+3] for i in range(0, len(tRNA_initial), 3)])
    
    # Output tRNA is returned by function
    return tRNA