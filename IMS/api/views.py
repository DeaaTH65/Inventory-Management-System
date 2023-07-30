from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, ProfileSerializer, PurchaseSerializer, UserSerializer, UserLoginSerializer
from app_inventory.models import Product, Purchase
from app_users.models import Profile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from rest_framework import status



@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/products',
        'GET /api/products/:id',
        'GET /api/users',
        'GET /api/users/:id',
        'GET /api/profiles',
        'GET /api/profiles/:id',
        'GET /api/purchases',
        'GET /api/purchases/:id',
        
        'GET /api/add_products',
        'GET /api/userlogin',
        'GET /api/userlogout',
    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    rooms = Product.objects.all()
    serializer = ProductSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    room = Product.objects.get(id=pk)
    serializer = ProductSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getPurchases(request):
    purchases = Purchase.objects.all()
    serializer = PurchaseSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(purchase, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def postProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def userlogin(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userlogout(request):
    logout(request)
    return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)