from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Etudiant
def index(request):
    etud = Etudiant.objects.all().values()
    template = loader.get_template('etudiant.html')
    context = {
        'etud': etud,
    }
    return HttpResponse(template.render(context, request))
def del_etud(request,id):
    e=Etudiant.objects.get(id=id)
    e.delete()
    return HttpResponseRedirect(reverse('index'))