import pandas as pd

emotions = pd.read_csv('Emotions.csv')

csv_contents = []
i = 0
for emotion in emotions['synonyms']:
    array_of_emotions = emotion.split(', ')
    set_of_emotions = set(array_of_emotions)
    final_emotions = []
    for soe in set_of_emotions:
        if str(soe)!="":
            final_emotions.append(soe)
    i = i + 1
    csv_contents.append([emotions['name'][i - 1], final_emotions])

print(csv_contents)
pd.DataFrame(csv_contents).to_csv("file.csv")
