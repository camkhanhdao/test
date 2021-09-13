"""assignment 1.3"""
import string

def a1_3():
    uinput= input("input a letter here: ").lower().strip()
    if uinput.isalpha()!=True:
        print('You did not input a letter')
    else:
        clist = list(string.ascii_lowercase)
        if uinput in list('aeiou'):
            print(f"you enter a vowel, the letter before this vowel is {clist[clist.index(uinput)-1]}")
        elif uinout == 'y':
            print("sometimes y is a vowel, sometimes y is a consonant")
        else:
            print(f"you enter a consonant, the letter before this consonant is {clist[clist.index(uinput)-1]}")
            
            
"""assignment 2.1"""
def ma(L:list):
    Lf = [L[i] if i in (0,1) 
          else 0.5*(L[i-1]+L[i-2]) for i in range(len(L))]
    print(Lf)
    return sum([abs(l-lf) for l,lf in zip(L,Lf)])

"""assignment 2.2"""
import string 

def caesar_encryption(shift=1)-> str:
    """ This function support encryption of ascii letters, digits, punctuation and whitespace
    shift: shift value
    shift>0 -> encrypt text 
    shift<0 decrypt text
    """
    message = input(f"Input your text to {'ecrypt' if shift>0 else 'decrypt'} here:\n")
    clist = list(string.ascii_lowercase)
    
    def encrypt(var):
        index= clist.index(var.lower())+shift
        maxs=len(clist)-1
        index = index if index<maxs else index-shift-maxs
        return clist[index] if var.isupper()==False else clist[index].upper()
    
    def decrypt(var):
        index = clist.index(var.lower())+shift
        return clist[index] if var.isupper()==False else clist[index].upper()
        
    
    return f"Your {'encrypted' if shift>0 else 'decrypted'} text: {''.join(encrypt(s) if s.isalpha() else s for s in list(message)) if shift>0 else ''.join(decrypt(s) if s.isalpha() else s for s in list(message))}"

"""assignment 2.3"""
import numpy as np
array=np.array([6,8,4,9,3,7])

def umax(nums):
    Max=nums[0]
    for item in nums:
        if item>Max:
            Max=item
    return Max

def umin(nums):
    Min = nums[0]
    for item in nums:
        if item<Min:
            Min=item
    return Min

def umean(nums):
    Sum = 0
    N = 0
    for item in nums:
        Sum+=item
        N+=1
    return Sum/N

def ustd(nums):
    Sum = 0
    N = 0
    std = 0
    for item in nums:
        Sum+=item
        N+=1
    Mean = Sum/N
    for item in [(i-Mean)*(i-Mean) for i in nums]:
        std+=item
    return (std/N)**0.5

def umedian(nums):
    N=0
    for item in nums:
        N+=1
    #sort array ascending 
    for i in range(N):
        for j in range(i + 1, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    m = N-1
    if N%2 !=1:
        return (nums[N//2]+nums[m//2])/2
    else:
        return nums[N//2]
    
def upercentiles(nums,percentile=75):
    N=0
    for item in nums:
        N+=1
    #sort array ascending 
    for i in range(N):
        for j in range(i + 1, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    
    p = N*percentile/100
    if p%2>0:
        return nums[int(p)]
    else:
        return (nums[p]+nums[p+1])/2


### check result 3

umax(array)==array.max(), umin(array)==array.min()

umean(array)==array.mean(),ustd(array)==array.std()i

umedian(array)==np.median(array,axis=0)

upercentiles(array,75),upercentiles(array,25)  
