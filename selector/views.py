from django.shortcuts import render,render_to_response

# Create your views here.
from selector.forms import ContactForm
def startpage(request):
	if request.method == 'POST':
		return HttpResponseRedirect('/results/')

	
	return render_to_response('startpage.html',{'name':'python'})

def results(request):
	# form = ContactForm()
	# if request.method == 'POST':
	# 	form = ContactForm(request.POST) # A form bound to the POST data
 #        if form.is_valid(): # All validation rules pass
 #            # Process the data in form.cleaned_data
 #            # ...

 #            # print form.cleaned_data['my_form_field_name']

 #            return HttpResponseRedirect('/thanks/') # Redirect after POST
 #    	else:
 #       		form = ContactForm()
 	return HttpResponseRedirect('/thanks/')

