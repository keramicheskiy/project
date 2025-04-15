from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.core.models import Equipment, Organization, Location, Faculty
from apps.core.serializers import EquipmentSerializer, OrganizationSerializer, LocationSerializer, FacultySerializer


@api_view(["GET"])
def get_equipments(request):
    equipments = Equipment.objects.all()
    serializer = EquipmentSerializer(equipments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    serializer = EquipmentSerializer(equipment)
    return Response(serializer.data)


@api_view(["POST", "GET"])
def create_equipment(request):
    if request.method == 'POST':
        serializer = EquipmentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        return Response(EquipmentSerializer.fields)


###

@api_view(["GET"])
def get_organizations(request):
    equipments = Organization.objects.all()
    serializer = OrganizationSerializer(equipments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_organization(request, pk):
    equipment = get_object_or_404(Organization, pk=pk)
    serializer = OrganizationSerializer(equipment)
    return Response(serializer.data)


@api_view(["POST", "GET"])
def create_organization(request):
    if request.method == "POST":
        serializer = OrganizationSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        return Response(OrganizationSerializer.fields)


###

@api_view(["GET"])
def get_locations(request):
    equipments = Location.objects.all()
    serializer = LocationSerializer(equipments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_location(request, pk):
    equipment = get_object_or_404(Location, pk=pk)
    serializer = LocationSerializer(equipment)
    return Response(serializer.data)


@api_view(["POST", "GET"])
def create_location(request):
    if request.method == "POST":
        serializer = LocationSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        return Response(LocationSerializer.fields)

###

@api_view(["GET"])
def get_faculties(request):
    equipments = Faculty.objects.all()
    serializer = FacultySerializer(equipments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_faculty(request, pk):
    equipment = get_object_or_404(Faculty, pk=pk)
    serializer = FacultySerializer(equipment)
    return Response(serializer.data)


@api_view(["POST", "GET"])
def create_faculty(request):
    if request.method == "POST":
        serializer = FacultySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        return Response(FacultySerializer.fields)


