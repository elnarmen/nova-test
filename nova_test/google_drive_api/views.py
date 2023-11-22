from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from google_drive_api.serializers import FileSerializer
from google_drive_api.api_client import create_file_in_google_drive


@api_view(["POST"])
def create_file(request):
    serializer = FileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    title = serializer.validated_data.get("title")
    content = serializer.validated_data.get("content")
    print(title, content)
    try:
        create_file_in_google_drive(title, content)
        response_data = {
            "success": "File created successfully",
            "title": title,
            "content": content,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(
            {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
