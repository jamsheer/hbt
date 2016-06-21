from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
from .models import Name
from rest_framework import viewsets
from .serializers import NameSerializer

class NameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Name.objects.all().order_by('-entry_date')
    serializer_class = NameSerializer

def thanks(request):
    template = loader.get_template('ygag/thanks.html')
    context = {
        'name_text': request.session['name_text'],
    }
    return HttpResponse(template.render(context, request))

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name_text=request.POST.get('name_text', '')
            name_obj=Name()
            name_obj.name_text=name_text
            name_obj.save()
            request.session['name_text'] = name_text
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'ygag/index.html', {'form': form})