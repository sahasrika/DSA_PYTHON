DSA CODING QUESTIONS 
1.frequency mapping in dictionary 
nums=[5,6,7,7,1,2,1,1,1,5,6,7]
freq_map={}
for i in range(0,len(nums)):
  if nums[i] in freq_map:
    freq_map [nums[i]]+=1
  else:
    freq_map[nums[i]]=1
print(freq_map)

2.frequency count in alphabets using ascii values

s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]
hashlist = [0] * 26
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hashlist[index] += 1
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hashlist[index])


