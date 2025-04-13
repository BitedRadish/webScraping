def count_vowels(str):
    cnt=0
    for s in str:
        if(s in ["a","e","i","o","u"]):
            cnt+=1
    print(cnt)

count_vowels("Python is awesome")