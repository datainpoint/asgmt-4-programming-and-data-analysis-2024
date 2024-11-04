def return_shape_name(number_of_corners: int) -> str:
    shape_names = {
    0: 'Circle',
    3: "Triangle",
    4: "Rectangle",
    5: "Pentagon",
    6: "Hexagon",
    7: "Heptagon",
    8: "Octagon",
    9: "Nonagon",
    10: "Decagon"
    }
    return shape_names[number_of_corners]

def count_of_positives(x: list) -> int:
    count=0
    for i in x:
        if i>0:
            count+=1
    return count

def sum_of_negatives(x: list) -> int:
    sum1=0
    for i in x:
        if i<0:
            sum1+=i
    return sum1

def return_with_fizz_buzz_rule(x: int):
    if x//3==x/3:
        if x//5==x/5:
            return 'Fizz Buzz'
        else:
            return 'Fizz'
    elif x//5==x/5:
        return 'Buzz'
    else:
        return x

def return_first_n_fizz_buzz(n: int) -> list:
    lst=[]
    for i in range(n):
        x=i+1
        if x//3==x/3:
            if x//5==x/5:
                lst.append('Fizz Buzz') 
            else:
                lst.append('Fizz')
        elif x//5==x/5:
            lst.append('Buzz')
        else:
            lst.append(x)
    return lst

def range_fizz_buzz(start: int, stop: int) -> list:
    lst=[]
    for i in range(start,stop):
        x=i
        if x//3==x/3:
            if x//5==x/5:
                lst.append('Fizz Buzz') 
            else:
                lst.append('Fizz')
        elif x//5==x/5:
            lst.append('Buzz')
        else:
            lst.append(x)
    return lst

def retrieve_middle_elements(x: list):
    if len(x)//2==len(x)/2:
        return (int(x[len(x)//2-1]),int(x[len(x)//2]))
    else:
        return x[len(x)//2]

def median(x: list):
    x.sort()
    if len(x)//2==len(x)/2:
        return (int(x[len(x)//2-1])+int(x[len(x)//2]))/2
    else:
        return x[len(x)//2]
    
def collect_divisors(x: int) -> list:
    if x==1:
        return [1]
    lst=[]
    for i in range(1,x+1):
        if x//i==x/i:
            lst.append(i)
    return lst

def is_prime(x: int) -> bool:
    if x==1:
        return False
    else:
        lst=[]
        for i in range(1,x+1):
            if x//i==x/i:
                lst.append(i)
        return len(lst)==2