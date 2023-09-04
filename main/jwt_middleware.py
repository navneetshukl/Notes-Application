from django.shortcuts import redirect, render
from django.urls import reverse
import jwt,utils
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the JWT token from the cookie
        token = request.COOKIES.get('jwt_token')

        if token:
            try:
                # Decode the JWT token
                payload = jwt.decode(token, utils.SECRET_KEY, algorithms=['HS256'])

                # Attach the payload to the request for easy access in views
                request.user_data = payload
            except jwt.ExpiredSignatureError:
                redirect_url=reverse("signin")
                return HttpResponseRedirect(redirect_url)
            except jwt.DecodeError:
                return JsonResponse({'error': 'Invalid token'}, status=401)

        response = self.get_response(request)
        return response
