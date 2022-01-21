'''Semantic Similarity: starter code author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''
''' Continued by Rayhaneh Behravesh'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    sum1=0
    sum2=0

    dot=[]
    for keys,values in vec1.items():
        m=vec2.get(keys)
        if m!=None:
            dot.append(values*m)


    sum1=norm(vec1)
    sum2=norm(vec2)

    mag=sum1*sum2
    dot_prod=sum(dot)
    return dot_prod/mag



def build_semantic_descriptors(sentences):
    ''''[["i", "am", "a", "sick", "man"],
         ["i", "am", "a", "spiteful", "man"],'''

    new=[]
    new2=[]
    dict={}
    dict1={}
    L=sentences
    for i in L:
        new=[]

        for j in i:
            new2=[]
            if j in new:
                pass
            else:
                new.append(j)
                if j in dict:
                    for s in i:
                        if s in new2:
                            pass
                        else:
                            new2.append(s)
                            if s in dict[j] and s!=j:
                                dict[j][s]+=1
                            elif s!=j:
                                dict[j].update({s:1})


                else:
                    k=[]
                    for h in i:
                        if h not in k and h!=j:
                            k.append(h)


                    dict[j]=dict.fromkeys(k,1)




    return dict





def build_semantic_descriptors_from_files(filenames):
    text=""
    for f in filenames:
        n=open(f, "r", encoding="latin1")
        text+=n.read()

    punc=[",", "-", "--", ":", ";"]
    ending= ["!","?"]
    text=text.lower()


    for i in punc:
        if i == "--" or i=="-":
            text=text.replace(i," ")
        else:
            text=text.replace(i,"")



    text.replace("\n"," ")

    for j in ending:
        text=text.replace(j,".")

    text=text.split(".")
    # print(text)

    i = 0
    while i < len(text):
        if not text[i]:
            del text[i]
        else:
            i += 1

    for i in range(len(text)):
        text[i]=text[i].split()
    # print(text)
    semantic_descriptors=build_semantic_descriptors(text)
    return semantic_descriptors

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):

    L=semantic_descriptors

    if word in L:
        pass
    else:
        return choices[0]

    # for i in choices:
    #     if i in L:
    #         pass
    #     else:
    #         mod_choice[:]
    #         mod_choices.remove(i)
    # if len(mod_choice)==0:
    #     return choice[0]
    i=0
    while i<len(choices):
        if choices[i] in L:
            break
        i+=1
        if i==len(choices):
            return choices[0]


    max=-1
    for i in choices:
        if i in L:
            v1=L[i]
            v2=L[word]
            res=similarity_fn(v1,v2)
        else:
            res=-1

        if max<res:
            max=res
            answer = i

    return answer





def run_similarity_test(filename, semantic_descriptors, similarity_fn):

    n=open(filename, "r", encoding="latin1")
    text=n.read()

    text=text.split("\n")


    for i in range(len(text)):
        text[i]=text[i].split()

    outcome=[]
    for i in text:
        for j in i:
            if i.count(j)==2:
                correct=j
                choices=i[1:]
                choices.remove(j)
                ans=most_similar_word(i[0],choices,semantic_descriptors,similarity_fn)
                if ans ==correct:
                    outcome.append(1)
                else:
                    outcome.append(0)
                break

    return sum(outcome)/len(outcome)*100
'''

[["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],

if L[i].count(j)!=0:
'''

if __name__ == "__main__":
    # print(split_to_list(["book.txt","sw.txt"]))
    # L=build_semantic_descriptors_from_files(["book.txt","sw.txt"])

    # print(most_similar_word("cat",["cat","dog","horse"],L,cosine_similarity))
    # print(most_similar_word("stone", ["rock","chair"],L,cosine_similarity))
    print(run_similarity_test("test.txt",L,cosine_similarity))











