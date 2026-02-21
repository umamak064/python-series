sentence=input("Enter here: ").lower()
sentence_words=sentence.split()
print(sentence_words)
word={}
for i in sentence_words:
    if i in word:
        word[i]=word[i]+1
    else:
        word[i]=1  
print(word)        
