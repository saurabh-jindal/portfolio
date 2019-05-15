
# from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import contact
from .forms import Contact_Form 
# from django.core.urlresolvers import reverse

# Create your views here


def index(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact_obj = contact(name = name, email = email, message = message)
            contact_obj.save()
            # return redirect('post_details', pk=post.pk)
            return HttpResponseRedirect(reverse('home:thanks'))

        else:
            form = Contact_Form()    

    
    context = locals()
    template = 'index.html'
    return render(request, template, context)


def thanks(request):
    return render(request, 'thanks.html')


# def service(request):
#     pass

# def contribution(request):
#     pass    


# def portfolio(request):
#     pass


# def contact(request):
#     pass

