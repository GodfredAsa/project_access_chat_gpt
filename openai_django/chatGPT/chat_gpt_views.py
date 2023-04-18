
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base_app.oai_queries import get_completion



@api_view(['POST'])
def get_chatGPT(request):
    data = request.data
    prompt = data['prompt']
    response = get_completion(prompt)
    print(response)
    return Response([response]) if type(response) == str else Response(response)


def response_processor(response: str):
    if "\n" in response:
       return [res for res in response.split('\n') if res != ""]
    else:
        return response
    

@api_view(['GET'])
def get_message(_):
    return Response("This works Godfred")






