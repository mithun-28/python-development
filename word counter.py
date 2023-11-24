# Word counter

word_count = 0

with open('sample.txt','r') as txt:
    for lines in txt:
        words = lines.split()
        word_count += len(words)
    print("Word count = ",word_count)
      
