from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, SpamFlag
from .serializers import UserSerializer, SpamFlagSerializer
from django.db.models import Q

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MarkSpamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=400)
        
        spam, created = SpamFlag.objects.get_or_create(phone_number=phone_number)
        if not created:
            spam.flagged_count += 1
            spam.save()
        return Response({'message': 'Number marked as spam', 'spam_count': spam.flagged_count})

class SearchView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query')
        if not query:
            return Response({'error': 'Query parameter is required'}, status=400)

        if query.isdigit():
            # Search by phone number
            results = SpamFlag.objects.filter(phone_number__icontains=query)
        else:
            # Search by name
            results = User.objects.filter(
                Q(username__istartswith=query) | Q(username__icontains=query)
            )

        data = [{'name': r.username, 'phone_number': r.phone_number} for r in results]
        return Response(data)
    