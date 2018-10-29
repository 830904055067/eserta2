from django.shortcuts import render
from .models import Aktiviti                 #library utk import database

# Create your views here.


#Home penganjur
def home(request):
	
	#list of records
	a=Aktiviti.objects.all()
	for ak in a:
		print(ak.tajuk,ak.tempat,ak.penceramah)

	#add  data
	akt = Aktiviti(tajuk="Mari mengaji", tempat="Surau", penceramah="Ustaz Azhar Idrus", hadpeserta=0,)
	akt.save()

	return render(request,'penganjur/home.html')

#delete penganjur
def delete_penganjur(request,pk):

	#dptkn id aktiviti dan cari rekod
	aktiviti= get_object_or_404(Aktiviti,pk)

	#confirm delete
	aktiviti.delete()

	return render(request,'penganjur/home.html')
