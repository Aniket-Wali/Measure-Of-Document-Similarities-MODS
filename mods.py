import math
import backend as bk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import shutil
import string
from os import listdir
import os
import sys
import matplotlib as mplot

##################################
# read a text file ##
##################################
def read_file(filename):

    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print ("Error opening or reading input file: ", filename)
        sys.exit()


#################################################
# split the text lines into words ##
#################################################
translation_table = str.maketrans(string.punctuation + string.ascii_uppercase,
                                     " " * len(string.punctuation) + string.ascii_lowercase)


def get_words_from_line_list(text):

    text = text.translate(translation_table)
    word_list = text.split()
    return word_list


##############################################
# count frequency of each word
##############################################
def count_frequency(word_list):

    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D


#############################################
#compute word frequencies for input file
#############################################
def word_frequencies_for_file(filename):

    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    return freq_mapping


def inner_product(D1, D2):
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += D1[key] * D2[key]
    return sum


def vector_angle(D1, D2):

    numerator = inner_product(D1, D2)
    denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))
    return math.acos(numerator / denominator)

def list_files1(directory):
    return (f for f in listdir(directory) if not f.startswith('.'))

def main(usr):
    Tk().withdraw()
    filename_1 = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    os.system('clear')
    st = os.getcwd() + '/'
    directory = st + 'records'
    files = list_files1(directory)
    copy = False
    file = None
    for f in files:
        filename_2 = f
        if os.path.basename(filename_1) == filename_2:
            print ("Your assignment is already uploaded...")
            return None
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(directory + '/' + filename_2)
        distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
        if distance < 0.688132:
            copy = True
            file = filename_2
            break

    if copy:
        print("Copied Document submission!!!")
        fl1 = os.path.basename(filename_1)
        shutil.copy(filename_1, directory)
        bk.cheatRecord(fl1, file, usr)
    else:
        filename = os.path.basename(filename_1)
        bk.addDataRecord(filename, usr)
        shutil.copy(filename_1, directory)
        print ("File Upload Successfully...")