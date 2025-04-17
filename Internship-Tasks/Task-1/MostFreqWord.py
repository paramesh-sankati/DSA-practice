'''
What is the most frequent word in the following paragraph?

paragraph = 'I love teaching. If you do not love teaching what else
can you love. I love Python if you do not love something which can
give you all the capabilities to develop an application what else can
you love.

'''
p='''I love teaching. If you do not love teaching what else
can you love . I love Python if you do not love something which can
give you all the capabilities to develop an application what else can
you love'''
def most_freq_word(p):
    most=0
    dici={i:p.split().count(i) for i in p.split()}
    for k,v in dici.items():
        if v>most:
            ans=k
            most=v
    return ans

print(most_freq_word(p))
