import text2emotion as te
from matplotlib import pyplot as plt

data = list()
text = "Picture is deceiving. Biggest container is much smaller that it looks. Disappointing. I’ll be returning these. Need big containers as well as small ones. This won’t do."
#Call to the function
res=te.get_emotion(text)
persen = te.get_percent_emotion(text)
for k,v in res.items():
    data.append(v)
print (persen)
emotions = ['HAPPY','ANGRY','SUPRISE','SAD','FEAR']

fig = plt.figure(figsize=(10,7))
plt.pie(data, labels=emotions, normalize=False)
plt.show()