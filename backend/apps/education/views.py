from django.shortcuts import render
from rest_framework.response import Response

from apps.education.models import Subject


# Create your views here.




@api_view(["GET"])
def get_subjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)



