# classifier/views.py
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UploadedImage
from .serializers import ImageSerializer

class PredictObject(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            # Save the uploaded image
            uploaded_image = serializer.save()

            # Return a static value for now
            prediction = "Static Object Prediction"

            # Return the prediction in the response
            return Response({'prediction': prediction}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
