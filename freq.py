def most_frequent(string):
    freq={}
    for x in string:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    sorted_freq=sorted(freq.items(),key=get_count,reverse=True)
    print(sorted_freq)
    for x,count in sorted_freq:
        print(x,count)
def get_count(item):
    return item[1]
string=input()
most_frequent(string)
