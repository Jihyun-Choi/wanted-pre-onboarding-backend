from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView

from recruitment.models import JobApplication
from recruitment.serializers import JobApplicationSerializer


class JobApplicationCreateAPIView(CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def post(self, request, *args, **kwargs):
        """POST: /recruitment/apply/
        JobApplication 생성
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            return Response(
                {"detail": "이미 해당 채용공고에 지원하셨습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
