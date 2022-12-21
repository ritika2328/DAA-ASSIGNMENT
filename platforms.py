# Function to find the minimum number of platforms needed
def getMinPlatforms(arr, dep):
    arr.sort()
    dep.sort()
    count = 0
    platform = 0
    i = j = 0
    while i < len(arr):
        if arr[i] < dep[j]:
            count = count + 1
            platform = max(platform, count)
            i = i + 1
        else:
            count = count - 1
            j = j + 1
 
    return platform
 
 
if __name__ == '__main__':
    a=int(input("Enter no.of elements : "))
    print("Enter the arrival timings : ")
    arr=[]
    for i in range(a):
        arr.append(int(input()))
    print("Enter the departure timings : ")
    dep=[]
    for i in range(a):
        dep.append(int(input()))
    print("The minimum platforms needed is", getMinPlatforms(arr, dep))
