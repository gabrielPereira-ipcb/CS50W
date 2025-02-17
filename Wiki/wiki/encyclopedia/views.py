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

    else:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

