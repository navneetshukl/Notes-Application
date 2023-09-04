import datetime
import hashlib
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import jwt, utils


SECRET_KEY = utils.SECRET_KEY


#! Signup Method using JWT
@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        db = utils.Connect_To_DB()
        collection = db["user"]

        # Check if the username already exists in your MongoDB collection
        if not collection.find_one({"email": email}):
            # Hash the password securely
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Create a new user document in MongoDB with the hashed password
            user = {"name": name, "email": email, "password": hashed_password}
            collection.insert_one(user)

            # Generate a JWT token
            payload = {
                "name": name,
                "email": email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            # Store the token in a cookie
            response = JsonResponse({"message": "User Registered Successfully"})
            response.set_cookie("jwt_token", token)

            return response
        else:
            return JsonResponse({"error": "Email already exists"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


def Home(request):
    user_data = request.user_data

    if user_data:
        name = user_data.get("name")
        email = user_data.get("email")
        print(f"Name {name} and Email is {email}")
        context={
            "name":name,
            "email":email
        }

    return render(request,"all.html",context)


#! Signin Method using JWT
@csrf_exempt
def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        db = utils.Connect_To_DB()
        collection = db["user"]
        user = collection.find_one({"email": email})

        if user:
            # Compare the provided password with the hashed password stored in the database
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if user["password"] == hashed_password:
                # Generate a JWT token
                payload = {
                    "name": user["name"],
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

                # Store the token in a cookie
                response = JsonResponse(
                    {"message": "User Login Successfully", "name": user["name"]}
                )
                response.set_cookie("jwt_token", token)

                return response
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        else:
            return JsonResponse({"error": "User not found"}, status=400)

#! Insert Notes in Database
def create(request):
    if request.method == "GET":
        return render(request, "create.html")
    elif request.method == "POST":
        user_data=request.user_data
        
        if user_data:
            email = user_data["email"]
            title = request.POST.get("title")
            description = request.POST.get("description")
            db = utils.Connect_To_DB()
            collection = db["notes"]
            data={
                "email":email,
                "title":title,
                "description":description
            }
            collection.insert_one(data)
            return redirect("/create/")
        else:
            return JsonResponse({"Message":"Error at Server"})
        
