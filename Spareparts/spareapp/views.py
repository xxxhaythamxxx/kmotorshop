from django.shortcuts import get_object_or_404, redirect, render, HttpResponse, HttpResponseRedirect
from .models import *
from django.views import View
from .cart import *
# Create your views here.

# Creo el diccionario para los formularios en común de todos los templates
def same():
    # Consigo TODOS los spares
    allSparesall=spare.objects.all()
    # Consigo TODAS las categorias
    allCategories=category.objects.all()
    # Consigo TODOS los motores
    allEngines=engine.objects.all()
    # Conseguir TODOS los carros por fabricante
    onlyManufCars=car.objects.all().values("car_manufacturer").distinct()
    # Conseguir TODOS los carros
    allCars=car.objects.all()
    # Conseguir TODOS los repuestos por nombre
    allSpares=spare.objects.values("spare_name","spare_category").order_by("spare_name").distinct()
    dicc={"allSparesall":allSparesall,"allCategories":allCategories,"allCars":allCars,"onlyManufCars":onlyManufCars,"allEngines":allEngines,"allSpares":allSpares}
    return dicc

dic=same().copy()

# Código para saber si usa el input o el filtro
def selectf(request):

    # if request.method=="POST":
    #     list = request.POST.getlist('toAdd')
    #     delist = request.POST.getlist("toDel")
    #     if delist:
    #         carrito = Cart(request)
    #         for a in delist:                
    #             spare_part = get_object_or_404(spare, id = a)
    #             carrito.remove(spare_part)
    #     if list:
    #         carrito = Cart(request)
    #         for a in list:                
    #             spare_part = get_object_or_404(spare, id = a)
    #             carrito.add(spare_part)
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if request.method=="GET":
        search=request.GET.get("engine_id")
        # Si usaron el filter
        if search:
            # Valor del modelo del motor
            engModel=request.GET.get("engine_id")  
            # Valor del carro enviado     
            carManu=request.GET.get("car_id")    
            #Valor del modelo del carro enviado       
            carModel=request.GET.get("car_model_id")    
            comp=spare.objects.filter(engine_info__engine_ide__icontains=engModel,car_info__car_manufacturer__icontains=carManu,car_info__car_model__icontains=carModel).order_by("id")  # Creo un Query de spare que tenga el valor del motor pasado
            engcomp=engine.objects.filter(engine_ide__icontains=engModel,car_engine_info__car_manufacturer__icontains=carManu)
            dic.update({"spare":comp,"mig":engModel,"engcomp":engcomp})
            return render(request,"spareapp/findfil.html",dic)
        # Si se usa el buscador por código de repuesto
        else:   
            valor=request.GET.get("search")
            if valor:
                # Compara el codigoRepuesto con valor
                comp=spare.objects.filter(spare_code__icontains=valor).order_by("id") 
                dic.update({"spare":comp,"mig":valor})
                return render(request,"spareapp/find.html",dic)
            else:
                return False


def home(request):

    # if request.method=="POST":
    #     list = request.POST.getlist('toAdd')
    #     delist = request.POST.getlist("toDel")
    #     if delist:
    #         carrito = Cart(request)
    #         for a in delist:                
    #             spare_part = get_object_or_404(spare, id = a)
    #             carrito.remove(spare_part)
    #     if list:
    #         carrito = Cart(request)
    #         for a in list:                
    #             spare_part = get_object_or_404(spare, id = a)
    #             carrito.add(spare_part)
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if request.method=="GET":

        if selectf(request)==False:
            b = []
            a = car.objects.all().values("car_manufacturer").order_by("car_manufacturer")
            for v in a:
                v = v["car_manufacturer"]
                b.append(v)
            b = (set(b))
            dic.update({"manu":b})
            return render(request,"spareapp/home.html",dic)
        else:
            return selectf(request)

def find(request):
    return render(request,"spareapp/find.html")

def sparedetails(request,val):
    return render(request,"spareapp/sparedetails.html")

def brand(request,val):
    if selectf(request)==False:
        pr=spare.objects.values("id","spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_brand__icontains=val).distinct()
        dic.update({"spare":pr,"mig":val})
        return render(request,"spareapp/brand.html",dic)
    else:
        return selectf(request)

def name(request,val):
    if selectf(request)==False:
        pr=spare.objects.values("id","spare_photo","spare_code","spare_brand","spare_name","car_info__car_manufacturer").filter(spare_name__icontains=val).distinct()
        dic.update({"spare":pr,"mig":val})
        return render(request,"spareapp/name.html",dic)
    else:
        return selectf(request)

def trunc(val):
    allen = car.objects.filter(car_manufacturer__icontains=val).values("car_model").order_by("car_model")
    b=[]
    for a in allen:
        a = a["car_model"].split(" ")[0]
        b.append(a+" .")
    b = list(set(b)) 
    return b

def manuf(request,val):
    if selectf(request)==False:
        tr = trunc(val)
        pr=car.objects.filter(car_manufacturer__icontains=val)
        dic.update({"car":pr,"mig":val,"tr":tr})
        return render(request,"spareapp/manuf.html",dic)
    else:
        return selectf(request)

def allmodel(request,val):
    if selectf(request)==False:
        rep = spare.objects.filter(car_info__car_model__icontains=val).distinct()
        dic.update({"spare":rep,"mig":val})
        return render(request,"spareapp/allmodel.html",dic)
    else:
        return selectf(request)

def allmanu(request,val):
    
    if selectf(request)==False:
        rep = spare.objects.filter(car_info__car_manufacturer__icontains=val).distinct()
        dic.update({"spare":rep,"mig":val})
        return render(request,"spareapp/allmanu.html",dic)
    else:
        return selectf(request)

def model(request,val):

    if selectf(request)==False:
        pr=engine.objects.filter(car_engine_info__car_model__icontains=val)
        dic.update({"engine":pr,"mig":val})
        return render(request,"spareapp/model.html",dic)
    else:
        return selectf(request)