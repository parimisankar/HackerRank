'''
Given a number, you have to write it in words
'''
def cent(number,main_dict):
    
    array, length = [],len(str(number))
    
    g1 = [i for i in [number//100 * 100, number%100] if i != 0]
    
    g2 = [(number//(10 ** i) % 10) * (10 ** i) for i in range(2, -1,-1)]
    
    g = g1 if g1[-1] in main_dict else g2
    
    for n,i in enumerate(g):
        if (n == 0 and length == 3) or (i not in main_dict):
            array.append(main_dict[int(str(i)[0])])
        array.append(main_dict[i] if i in main_dict else main_dict[10 ** (length - 1)])
    
    return main_dict[number] if number in main_dict.keys() else ' '.join(array)

def convert(number):
    
    main_dict = {0:"",
                 1:"One",
                 2:"Two",
                 3: "Three",
                 4:"Four",
                 5:"Five",
                 6:"Six",
                 7:'Seven',
                 8:'Eight',
                 9:'Nine',
                 10:'Ten',
                 11:"Eleven",
                 12:"Twelve",
                 13:'Thirteen',
                 14:'Fourteen',
                 15:'Fifteen',
                 16:'Sixteen',
                 17:'Seventeen',
                 18:'Eighteen',
                 19:'Nineteen',
                 20:'Twenty',
                 30:'Thirty',
                 40:'Forty',
                 50:'Fifty',
                 60:'Sixty',
                 70:'Seventy',
                 80:'Eighty',
                 90:'Ninety',
                 100:'Hundred'
                }
    
    things = [(number//(10 ** i))%1000 for i in range(21, -3, -3)] #trillions, billions, millions, thousand, _blank_
    
    things = [(cent(things[i],main_dict) + " " + ['Sextillion','Quintillion','Quadrillion','Trillion','Billion','Million','Thousand',''][i]).strip() for i in range(len(things)) if things[i] != 0]
    
    return ' '.join(things)

for _ in range(int(input())):
    print(convert(int(input())))