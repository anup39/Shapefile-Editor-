from django.shortcuts import render
from django.http import HttpResponse
from shapeEditor.shared.models import Shapefile
from shapeEditor.shapefiles.forms import ImportShapefileForm
from shapeEditor.shapefiles import shapefileIO
from django.http import HttpResponseRedirect

# Create your views here.

def list_shapefiles (request):
    shapefiles = Shapefile.objects.all().order_by('filename')
    return render(request, "list_shapefiles.html",{'shapefiles' : shapefiles})

def import_shapefile(request):
    if request.method == "GET":
        form = ImportShapefileForm()
        return render(request,"import_shapefile.html",{'form' : form,'errMsg' : None})

    elif request.method == "POST":
        errMsg = None 
        form = ImportShapefileForm(request.POST,request.FILES)
        if form.is_valid():
            shapefile = request.FILES['import_file']
            # The logic to set wheather the shapefile is zip or not or to know the extension of file inside it
            errMsg = shapefileIO.import_data(shapefile)
            if errMsg == None:
                return HttpResponseRedirect("/")
        return render(request, "import_shapefile.html",{'form' : form,'errMsg' : None})
