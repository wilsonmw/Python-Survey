from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    try:
        request.session['count']
    except:
        request.session['count']=0
    return render(request, 'survey_app/index.html')

def process(request):
    request.session['count'] = request.session['count']+1
    if request.method == "POST":
        request.session['name']=request.POST['name']
        request.session['location']=request.POST['location']
        request.session['language']=request.POST['language']
        request.session['comment']=request.POST['comment']
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    return render(request, 'survey_app/results.html')

def goback(request):
    return redirect('/')
