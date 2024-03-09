from django.views import View
from django.shortcuts import render
from .my_functions import titleCase
from my_objects import Car, Motorcycle

def title_name(the_name: str):
    return the_name.title()

class HomePageView(View):
    def get(self, request):

        my_name = "TOMMY"
        
        new_name = title_name(my_name)

        name_list = ["TOMMY", "Tom", "Thomas", "Luke"]
        title_list = titleCase(name_list)  
        second_name = name_list[1]

        statement = "The original name was " + my_name + " but the title name is " + new_name + ". The second name in the list is " + second_name

        car1 = Car(make="Toyota", model="Highlander", year=2016, sound="Toot toot")
        car2 = Car(make="Subaru", model="Crosstrek", year=2017, sound="Rawrrr")
        moto1 = Motorcycle(make="Honda", model="Rukus", year=2010, sound="Vroom Vroom")




        context = {
            'hi': 'Hello World!',
            'name': statement,
            'list': name_list,
            'titleList': title_list,
            'car1': car1,
            'car2': car2,
            'moto1':moto1  
        } 

        return render(request, 'my_app/index.html', context)
