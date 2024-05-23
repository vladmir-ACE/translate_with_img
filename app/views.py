from django.shortcuts import render, redirect,get_object_or_404,reverse
from django.views import View
from .models import Translate
from .forms import TranslateForm

class TranslateCreateView(View):
    def get(self, request):
        form = TranslateForm()
        return render(request, 'translate_form.html', {'form': form})

    def post(self, request):
        form = TranslateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('translate_list')
        return render(request, 'translate_form.html', {'form': form})

class TranslateListView(View):
    def get(self, request):
        translates = Translate.objects.all()
        return render(request, 'translate_list.html', {'translates': translates})
    
import os
from django.conf import settings

def translate_delete(request, pk):
    translate = get_object_or_404(Translate, pk=pk)
    if request.method == 'POST':
       
        if translate.image:
           
            image_path = os.path.join(settings.MEDIA_ROOT, str(translate.image))
            
            if os.path.exists(image_path):
                os.remove(image_path)
    
        translate.delete()
        return redirect(reverse('translate_list'))
    return render(request, 'translate_confirm_delete.html', {'translate': translate})
