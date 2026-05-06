from django.shortcuts import render

# Create your views here.


TAUX = 1.09
DEV1 = "EUR"
DEV2 = "USD"

def index(request):

    if request.method=='POST':
        #
        #on fait le calcul
        print(request.POST)
        print("le montant est : ",request.POST.get("montant"))
        m = float(request.POST.get("montant"))
        mc = m * TAUX
    else: # la methode est GET
        m = 10.0
        mc = 0.0

    context  = {
        "devise1":DEV1   ,
        "devise2":DEV2   ,
        "taux": TAUX  ,
        "montant": m,
        "montantConverti": mc,
    }


    return render(request,'converter/index.html', context)


