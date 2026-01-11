
from rest_framework.views import APIView
from django.http import JsonResponse
from firebase import db


class JobApplicationListView(APIView):
    def get(self, request):
        job_applications = []
        collection = db.collection('job_applications').get()
        for doc in collection:
            job_data = doc.to_dict()
            job_data['id'] = doc.id  # include the id from the document
            job_applications.append(job_data)
        return JsonResponse({'job_applications': job_applications}, safe=False)


class JobApplicationDetailView(APIView):
    def get(self, request, id):
        job_application = db.collection('job_applications').document(id).get()
        if not job_application:
            return JsonResponse({'error': 'Job application not found'}, status=404)
        return JsonResponse({'job_application': job_application.to_dict()}, safe=False)


class JobApplicationCreateView(APIView):
    def post(self, request):
        try:
            job_application = db.collection(
                'job_applications').add(request.data)
            return JsonResponse({'message': 'Job application created successfully'}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class JobApplicationUpdateView(APIView):
    def put(self, request, id):
        try:
            job_application = db.collection(
                'job_applications').document(id).update(request.data)
            return JsonResponse({'message': 'Job application updated successfully'}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class JobApplicationDeleteView(APIView):
    def delete(self, request, id):
        try:
            job_application = db.collection(
                'job_applications').document(id).delete()
            return JsonResponse({'message': 'Job application deleted successfully'}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
