from django.views import View
from django.shortcuts import render, redirect

def title_name(the_name: str):
    return the_name.title()

class HomePageView(View):
    def get(self, request):

        my_name = "TOMMY"

        new_name = title_name(my_name)
     
        return render(request, 'my_app/index.html',{'hi':'Hello World!', 'name':new_name})