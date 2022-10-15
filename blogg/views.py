from django.shortcuts import render, get_object_or_404
from .models import Blogg

# Create your views here.

def all_bloggs(request):
    bloggs = Blogg.objects.order_by('-date')
    return render(request, 'blogg/all_bloggs.html', {'bloggs': bloggs})

    #return render(request, 'blogg/all_bloggs.html')
def detail(request, blogg_id):
    blogg = get_object_or_404(Blogg, pk=blogg_id)
    return render(request, 'blogg/detail.html', {'blogg': blogg})
