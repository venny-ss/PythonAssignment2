text = "python is easy and python is powerful"

words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:", frequency)