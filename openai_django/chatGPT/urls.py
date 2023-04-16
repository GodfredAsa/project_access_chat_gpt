from django.urls import path
import  chatGPT.chat_gpt_views as views 
# import  .chat_gpt_views as views 

urlpatterns = [
    path('chat', views.get_chatGPT, name="some-else"),
    path('message', views.get_message, name="some-else"),

]