
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'Orange':'Sour'})
    #HttpResponse("This is my first page ")

def count(request):

    fulltex = request.GET["fulltext"]
   # print (fulltex)
    wordlist = fulltex.split()
    wordict = {}
    for word in wordlist:
        if word in wordict:
            wordict[word] += 1
        else:
            wordict[word] = 1
    sortedwords= sorted(wordict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltex, 'CT': len(wordlist), 'worddict': sortedwords})

def about(request):
    return render(request, 'about.html', {'Apple': 'Sweet'})
