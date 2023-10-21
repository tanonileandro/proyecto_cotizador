from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def calcular(request):
    try:
        data = json.loads(request.body)
        resultado = {
            "dolar": data['amount'] * 2,
            "uva": data['amount'] * 3,
            "ipc": data['amount'] * 1.5,
            "average": data['amount'] * 2.5,
        }
        return JsonResponse(resultado)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


