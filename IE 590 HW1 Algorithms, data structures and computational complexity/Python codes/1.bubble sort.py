inp = [3,8,23,6,3,5,6,54,3,78,69,1,2] #accept an array named inp
def bubble_sort(inp):
    n = len(inp) #Cal length of array
    for n in range(n,1,-1):
        for i in range(n-1):
            if inp[i] < inp[i+1]:# compare ith with (i+1)th index of inp
                inp[i+1], inp[i] = inp[i], inp[i+1] #swapping of elements of array

    return inp
output = bubble_sort(inp) #store the output of function in variable named output
print(output)
