import json
def parseData(request):
    data = request.POST["data"]
    data = json.loads(data)
    for i in data:
        fold = folder()
        fold.title = i["title"]
        fold.description = i["body"]
        fold.save()
    return redirect("/")