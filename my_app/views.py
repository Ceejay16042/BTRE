from django.shortcuts import render
from listings.models import listing, Realtor
from listings.choices import state_choices, price_choices, bedroom_choices

def index(request):
    listings = listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context_dict = {
        'listings': listings, 
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
}
    return render(request, 'index.html', context_dict)


def about(request):
    #get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
     
     #get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'about.html', context)

def base(request):
    return render(request, 'base.html')
