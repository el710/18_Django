from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

# Create your views here.
class ScheduleC(TemplateView):
    template_name = "schedule.html"
    extra_context = {"title": "Schedule", 
                     "welcome": "Today events",
                     "events": ["05:00:  wake up [Health care]",
                                "06:30: go to job [Job]",
                                "17:00: go to home [Job]",
                                "23:00:  go to bed [Health care]"
                               ]
    }

class ProjectC(TemplateView):
    template_name = "project.html"
    extra_context = {"title": "Project Shop",
                     "welcome": "Porject's list",
                     "projects": [{"name": "Health care", "events": ["05:00: wake up", "23:00: go to bed"]},
                                  {"name": "Job", "events": ["06:30: go to job", "17:00: go to home"]}  
                                ]
    }    

class CrudC(TemplateView):
    template_name = "crud.html"
    extra_context = {"title": "Manage",
                     "welcome": "Make your day"
    }
