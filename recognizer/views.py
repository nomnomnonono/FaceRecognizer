from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .forms import UploadImgForm
from mymodel.recognizer import recognizer


def index(request):
    params = {
        "form": UploadImgForm()
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(params, request))


def predict(request):
    if not request.method == 'POST':
        raise redirect('recognizer:index')

    form = UploadImgForm(request.POST, request.FILES)

    if not form.is_valid():
        raise ValueError('Form is invalid.')

    img = form.cleaned_data['img']
    pred, prob = recognizer(img)
    template = loader.get_template('predict.html')
    params = {
        'pred': pred,
        'prob': prob
    }
    return HttpResponse(template.render(params, request))
