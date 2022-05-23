from django.shortcuts import render

# Create your views here.

course_list = [
    {
        'id': 1,
        'title': "Operating System",
        'notice': [
            {
                'id': 1,
                'title': "notice1"
            }
        ]
    },
    {
        'id': 2,
        'title': "DBMS",
        'notice': [
            {
                'id': 1,
                'title': "notice3"
            }
        ]
    },
    {'id': 3,
     'title': "Software Engineering",
     'notice': [
         {
             'id': 1,
             'title': "notice3"
         }
     ]
     },
    {'id': 4,
     'title': "Project Management",
     'notice': [
         {
             'id': 1,
             'title': "notice3"
         }
     ]
     },
     {'id': 5,
     'title': "Green Computing",
     'notice': [
         {
             'id': 1,
             'title': "notice2"
         }
     ]
     },
]


def home(request):
    return render(request, 'login.html',)


def dashboard(request):

    return render(request, 'dashboard.html', {'courses': course_list})

def course_details(request,course_id):
    course = course_list[course_id-1]
    return render(request,'course_detail.html', {'course': course})
