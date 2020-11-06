#this python program will calculate the percent of nucleotides in a single-stranded DNA. It will also give the percent of cytosine if the ssDNA was double stranded

print("This program will help you grade lab 8 exercise 2 in BIOL 30001 lab.")
Num_Nuc = float(input("Input the number of total nucleotides: ")) #getting student data to perform calcs and check their math
Num_A = float(input("Input the number of Adenines: "))
Num_G = float(input("Input the number of Guanines: "))
Num_T = float(input("Input the number of Thymines: "))
Num_C = float(input("Input the number of Cytosines: "))
print("\n") #prints a space for cleaner output
percent_A = float(Num_A/Num_Nuc * 100) #calculates the percent of each nucleotide
percent_G = float(Num_G/Num_Nuc * 100) #yes, I know these variables aren't necessary
percent_T = float(Num_T/Num_Nuc * 100)
percent_C = float(Num_C/Num_Nuc * 100)

print("The percent of A is: %.1f" % percent_A) #prints the percent of each nucleotide to 1 decimal point
print("The percent of G is: %.1f" % percent_G)
print("The percent of T is: %.1f" % percent_T)
print("The percent of C is: %.1f" % percent_C)
print("\n")#prints a space for cleaner output

purines = float(Num_A + Num_G) #calculates the amount of purines
pyrims = float(Num_T + Num_C) #calculates the amount of pyrimidines

print("The number of purines is: %.1f" % purines) #prints the result of prior calcs
print("The number of pyrimidines is %.1f: " % pyrims)
print("\n")#prints a space for cleaner output

DS_C = float((Num_C + Num_G) / (Num_Nuc * 2)*100) #calculates what percent of the DNA would be C is the single strand was actually double stranded
DS_A = float((Num_A + Num_T) / (Num_Nuc * 2)*100) #same, but for A

print("If the strand was double stranded the percent of C would be: %.1f" % DS_C) #prints results of prior calcs
print("If the strand was double stranded the percent of A would be: %.1f" % DS_A)
