from django.shortcuts import render , render_to_response
from django.db.models import Q
from .models import userdate,vacuna
# Create your views here.

def search(request):
    query=request.GET.get('q','')
    if query:
        qset =(
            Q(nombrecompleto__icontains=query),
            Q(Doc__icontains=query),
        )
        results=userdate.objects.filter(qset).distinct()
    else:
        results=[]

    return render_to_response("userdate/search",{
        "results":results,
        "query":query
    })
