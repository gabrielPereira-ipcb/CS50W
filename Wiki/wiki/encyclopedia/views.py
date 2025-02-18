from django.shortcuts import render

from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry:
        return render(request, "encyclopedia/entry.html", {
            "content": markdown2.markdown(entry),
            "title": title
        })




    
def search (request):
    query = request.GET.get('q', "").strip()
    if not query:
        return index(request)
    else:
        results = []
        for title in util.list_entries():
            if query == title:
                return entry(request, query)
            elif query.lower() in title.lower():
                    results.append(title)
    if len(results) == 1 and results[0].lower() == query.lower():
        return entry(request, results[0])
    else:
        return render(request, "encyclopedia/search.html", {
"query": query,
"entries": results,
"not_found": False if len(results)>0 else True
})

def new(request):
    return render(request, "encyclopedia/new.html")

#not sure about efficente code since function 'search' does something similar about checking entry titles. 
#probably should refactor, make a new function to check that entry title similarities to the user query 
def save (request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    for entry in util.list_entries():
        if entry.lower() == title.lower():
            return render(request, "encyclopedia/error.html", {
                "message": f"Entry '{entry}' already exists"
            })
        
    util.save_entry(title, content)
    return entry(request, title)

    

    

            
                
        
            
                
            


