from django.shortcuts import render
from django.http import JsonResponse
from .oai_queries import get_completion
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        print(response)
        return JsonResponse({'response': response})
    return render(request, 'query.html')


# @api_view(['GET'])
# def get_chatGPT_response(request):
#     return Response("I am feeling lucky.")

