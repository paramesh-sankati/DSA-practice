'''
Q6. Clean the following text. After cleaning, count three most
frequent words in the string.
 sentence = &#39;&#39;&#39;%I $am@% a %tea@cher%, &amp;and&amp; I
lo%#ve %tea@ching%;. There $is nothing; &amp;as&amp; mo@re
rewarding as educa@ting &amp;and&amp; @emp%o@wering
peo@ple. ;I found tea@ching m%o@re interesting
tha@n any other %jo@bs. %Do@es thi%s mo@tivate
yo@u to be a tea@cher!?&#39;&#39;&#39;

print(clean_text(sentence)); I am a teacher and I love teaching
There is nothing as more rewarding as educating and
empowering people I found teaching more interesting than any
other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3, &#39;I&#39;), (2,
&#39;teaching&#39;), (2, &#39;teacher&#39;)]

'''
s='''I $am@% a %tea@cher%, &and& I
lo%#ve %tea@ching%;. There $is nothing; &as& mo@re
rewarding as educa@ting &and& @emp%o@wering
peo@ple. ;I found tea@ching m%o@re interesting
tha@n any other %jo@bs. %Do@es thi%s mo@tivate
yo@u to be a tea@cher!?'''

def clean_sentence(s):
    cleaned_sentence=''
    for i in s:
        if i.isalpha() or i.isspace():
            cleaned_sentence+=i
    return cleaned_sentence

def most_freq_word(p):
    most=0
    dici={i:p.split().count(i) for i in p.split()}
    for k,v in dici.items():
        if v>most:
            ans=k
            most=v
    return ans

t=clean_sentence(s)
print(t)
print(most_freq_word(t))
