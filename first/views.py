from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from SimilarPlacesNetwork import helper, neuralnetwork
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from PIL import Image
import os


json_loader = helper.JsonLocationsHelper("SimilarPlacesNetwork/json/")


# Create your views here.
class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def get_locations(request, label):
    data = json_loader.get_locations_for_label(label)
    return JsonResponse(data, safe=False)


def get_all_labels(request):
    return JsonResponse(json_loader.get_all_labels(), safe=False)


def get_picture_from_id(request, id):
    image_path = os.getcwd() + "/SimilarPlaces/first/images/" + id + ".jpeg"
    try:
        with open(image_path, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response


class UserUploadedPicture(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        image = Image.open(request.data['image'])
        result = neuralnetwork.classify_image(image, json_loader.get_all_labels())
        data = json_loader.get_locations_for_label(result['label'])
        result['locations'] = data
        return JsonResponse(result, safe=False)



