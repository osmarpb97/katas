import re
from collections import Counter

def top_3_words(text):
    words = Counter(re.findall("'*[a-z][a-z']*",text.lower())).most_common(3)
    return([word for word,cnt in words])