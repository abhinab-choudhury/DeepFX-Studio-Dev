# DeepFX Studio

#### Task List

- [ ] Ask if is it ok to use jQuery for Simplicity of js-backend
- [ ] Use **Supabase** for file storage and a PostgreSQL database.
- [ ] Deploy the project on **Vercel** ([Video Guide]()).
- [ ] Set up **Black** for linting in the Django project.
- [ ] Create **Docker** and **docker-compose** files for containerized deployment ([Backend Tutorial](https://www.youtube.com/watch?v=9C03V1dXxOU&list=PLbtI3_MArDOnIIJxB6xFtpnhM0wTwz0x6lll)).
- [ ] Study and implement **django-allauth** for user authentication.
- [ ] Set up **Google** and **GitHub OAuth** for user login.
- [ ] Coordinate with the team to use **TailwindCSS** for styling. [use CDN](https://www.geeksforgeeks.org/how-to-add-tailwind-css-to-html/#add-tailwind-css-to-html-using-a-cdn-link)
- [ ] Design a minimalistic **Figma template** to finalize the web layout.
- [ ] Provide Figma markup to the team for front-end development.
- [ ] Explore using the **GSAP** library for animations [use CDN](https://gsap.com/docs/v3/Installation/?tab=cdn&module=esm&method=private+registry&tier=free&club=false&require=false&trial=true) ([Tutorial](https://www.youtube.com/watch?v=9C03V1dXxOU&list=PLbtI3_MArDOnIIJxB6xFtpnhM0wTwz0x6)).
- [ ] Research a solution to remove `.html` from page URLs for cleaner routing, similar to an SPA (Single Page Application).



## Overview:

## Work Around:

To create your Django AI-based app with authentication and image manipulation, here’s a roadmap and recommended file structure to organize the code effectively. 

### Roadmap

1. **Set Up Django Project**:
   - Install Django and create your project directory.
   - Configure settings and install dependencies for auth, AI models, and image processing.
   
2. **Authentication**:
   - Implement Django’s built-in auth or use `django-allauth` for social login.
   - Set up user management features (register, login, logout, password reset).

3. **AI Model Integration**:
   - Select or build AI models for each manipulation task.
   - Use libraries like TensorFlow, PyTorch, or OpenCV to handle image processing.
   - Set up each AI feature as a modular component, either as a separate Django app or as modules within an app.

4. **Frontend/UI**:
   - Design minimalistic frontend views using Django templates or integrate a frontend framework.
   - Style your app with CSS frameworks like TailwindCSS.

5. **Deployment & Scaling**:
   - Prepare Docker configurations.
   - Use Vercel (or an alternative) for deployment and connect to your PostgreSQL database.

---

### Recommended File Structure

```plaintext
project_root/
│
├── deepfx_studio/                    # Main Django project folder
│   ├── settings.py                    # Configuration settings for the project
│   ├── urls.py                        # Main URLs for routing
│   ├── wsgi.py                        # WSGI application entry point
│   └── asgi.py                        # ASGI application entry point (for async)
│
├── authentication/                    # App for user authentication
│   ├── migrations/                    # Migrations for authentication
│   ├── templates/authentication/      # Templates for login, register, etc.
│   ├── urls.py                        # Routes for auth features
│   ├── views.py                       # Auth views (login, logout, register)
│   └── models.py                      # User-related models (if any custom fields)
│
├── ai_features/                       # App for AI image manipulation features
│   ├── migrations/                    # Migrations for AI features
│   ├── templates/ai_features/         # Templates for image processing UI
│   ├── urls.py                        # Routes for each AI feature
│   ├── views.py                       # Views for handling requests, rendering templates
│   ├── models.py                      # DB models for storing images, tasks, etc.
│   ├── tasks/                         # Folder for background tasks (e.g., Celery tasks)
│   │   ├── colorization.py            # Logic for colorizing B&W images
│   │   ├── background_removal.py      # Background removal code
│   │   ├── deepfake.py                # Deepfake generation code
│   │   └── __init__.py                # To make tasks a module
│   ├── utils/                         # Utility scripts for reusable functions
│   │   ├── image_preprocessing.py     # Preprocessing helper functions
│   │   └── post_processing.py         # Post-processing helpers
│   └── serializers.py                 # If using DRF for API views
│
├── media/                             # Uploaded images and processed results
├── static/                            # Static files (CSS, JavaScript)
├── templates/                         # Global templates (if any)
│
├── manage.py                          # Django management script
│
├── README.md                          # Project documentation
└── requirements.txt                   # Python dependencies
```

---

### Explanation of Key Folders and Files

- **`deepfx_studio/`**: The main configuration directory for your Django project.
  
- **`authentication/`**: Manages user authentication. Use views and templates here to handle sign-in, registration, etc.

- **`ai_features/`**: 
  - **`tasks/`**: Contains Python scripts for different AI-based tasks, with each task (like colorization or deepfake) as a separate file. This modularity makes it easier to debug and maintain.
  - **`utils/`**: Any helper functions, such as image preprocessing, can be stored here. This way, all AI models can access these functions without duplicating code.
  - **`views.py`**: Defines views that handle incoming requests for each feature. This is where you'll handle user inputs, load AI models, and pass processed results back to the user.
  - **`models.py`**: If you want to save images or task records in the database, define Django models here.

This structure allows each AI feature to be scalable, and organizing the AI logic separately will make it easier to update and add new features over time. Let me know if you need more detail on setting up specific files or any other part of the roadmap!

In Django, communication between apps is seamless because they share the same project environment, database, and authentication framework. Here’s how authentication can interact with the `ai_features` app for your project:

### 1. **User Access and Permissions** 

The `ai_features` app can directly use Django’s built-in authentication system to manage access to its views and features. Here are ways to integrate:

   - **Login Required Decorator**: To ensure only authenticated users access certain views, use the `login_required` decorator in `views.py` of the `ai_features` app:
     ```python
     from django.contrib.auth.decorators import login_required
     
     @login_required
     def colorize_image(request):
         # code for colorizing image
         return render(request, 'ai_features/colorize.html')
     ```

   - **User Object**: You can access the authenticated user’s object (like their ID, profile, or any custom data) from `request.user` in any view of `ai_features`. For instance:
     ```python
     def colorize_image(request):
         if request.user.is_authenticated:
             user = request.user
             # Process the image for the authenticated user
         else:
             return redirect('authentication:login')
     ```

### 2. **Cross-App URL Namespacing**

To link pages between `authentication` and `ai_features`, use Django’s URL namespacing and reverse URL resolution:
   - **Namespace URLs**: In the `urls.py` of each app, define a namespace. For example:
     ```python
     # ai_features/urls.py
     from django.urls import path
     from . import views

     app_name = 'ai_features'

     urlpatterns = [
         path('colorize/', views.colorize_image, name='colorize_image'),
     ]
     ```
   - **Reverse URL Resolution**: In `authentication` templates or views, you can use the namespaced URL to link to `ai_features`:
     ```html
     <a href="{% url 'ai_features:colorize_image' %}">Colorize Image</a>
     ```

### 3. **Session Management**

Since Django’s sessions are shared across the entire project, any user data or session variables set in `authentication` will be accessible in `ai_features`. You can save relevant session data for the user upon login and retrieve it later:
   ```python
   # In authentication/views.py
   from django.contrib.auth import login

   def custom_login(request):
       # Custom login logic
       login(request, user)
       request.session['user_preferences'] = user.preferences  # Store preferences in session
       return redirect('ai_features:home')

   # In ai_features/views.py
   def some_feature_view(request):
       user_preferences = request.session.get('user_preferences', None)
       # Use user preferences in AI model configuration
   ```

### 4. **Custom Permissions and Decorators**

If you need more granular control over access, such as restricting certain AI features based on a user’s subscription or profile status, you can create custom permissions or decorators:
   ```python
   # In ai_features/decorators.py
   from django.http import HttpResponseForbidden

   def subscription_required(function):
       def wrap(request, *args, **kwargs):
           if request.user.profile.has_subscription:
               return function(request, *args, **kwargs)
           else:
               return HttpResponseForbidden("Subscription required to access this feature.")
       return wrap
   ```
   Use this decorator on views within `ai_features`:
   ```python
   from .decorators import subscription_required

   @login_required
   @subscription_required
   def deepfake(request):
       # code for deepfake
       return render(request, 'ai_features/deepfake.html')
   ```

### 5. **API Views with Tokens (if using DRF)**

If you plan to use Django REST Framework (DRF) for an API-based setup, JWT or token-based authentication will work across apps, allowing you to secure API views in `ai_features`. 

Using Django’s authentication across apps is straightforward since all apps share a database and project-level session and user management. Let me know if you’d like specific examples of any part!
