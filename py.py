import re
file = open('beemovie.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())


def longboi():
    longest = ""
    l = len(words)
    for i in words:
        if len(i) >= len(longest):
            longest = i
    print (longest)

longboi()
