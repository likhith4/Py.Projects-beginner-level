with open("story.txt","r") as f:
    story=f.read()
words=set() #using set to get only unique words which will cut off all the duplicate ones.
start_of_word=-1
target_start="<"
target_end=">"
for i,char in enumerate(story):
    if char == target_start:
        start_of_word=i
    
    if char == target_end and start_of_word!=-1:
        word=story[start_of_word:i+1] #string slicing will not include start of word i+1 will include the char at i th value
        words.add(word)
        start_of_word=-1
print(words)

