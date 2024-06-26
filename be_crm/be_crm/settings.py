"""
Django settings for be_crm project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/
å
For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

### Explanation of Django Settings:

#### Technical Perspective:

# 1. **Folder Structure:**
#    - The `be_crm` project follows the standard structure of a Django project, with directories for settings, URLs, WSGI application, and app configurations.

# 2. **Settings Configuration:**
#    - The `settings.py` file contains crucial configuration settings for the Django project, such as database setup, middleware, installed applications, security settings, CORS (Cross-Origin Resource Sharing) configurations, and more.

# 3. **Installed Apps:**
#    - `INSTALLED_APPS` lists all the Django apps installed in the project, including default Django apps like authentication, sessions, etc., and custom apps like `mybe` created using `startapp` command.

# 4. **Middleware:**
#    - `MIDDLEWARE` includes middleware classes that process requests and responses, performing tasks like security, session management, authentication, and CORS handling.

# 5. **Security Settings:**
#    - `SECRET_KEY` is a cryptographic key used for session signing and other security measures.
#    - `DEBUG` is set to `True` for development purposes. It should be set to `False` in production.
#    - `ALLOWED_HOSTS` specifies which host/domain names can access the Django application.

# 6. **Database Configuration:**
#    - `DATABASES` defines the database engine, name, user, password, and other settings. In this case, it's using SQLite as the default database.

# #### Non-Technical Perspective:

# 1. **Project Structure:**
#    - The project follows a structured layout, making it easy to organize and maintain code files and configurations.

# 2. **Settings Overview:**
#    - The `settings.py` file acts as the control center for the Django project, allowing customization of various aspects like database, security, and middleware.

# 3. **Installed Features:**
#    - Django comes with built-in features like authentication, sessions, and admin interface, which are automatically included in the project.
#    - Additional features can be added by installing custom apps, as listed in the `INSTALLED_APPS` section.

# 4. **Security and CORS:**
#    - Security measures like secret key, debugging settings, and allowed hosts ensure that the application is secure and accessible only from trusted sources.
#    - CORS settings allow cross-origin requests from specified origins, ensuring compatibility with frontend applications hosted on different domains.

# 5. **Database Setup:**
#    - Configuration for the default database engine (SQLite) is provided, making it easy to get started with database-backed applications.


# Contains configuration settings for your Django project.
# Includes settings such as database configuration, static files, middleware, installed applications, timezone, language, etc.
# Acts as the main configuration file for your Django project.
# You can customize various aspects of your project by modifying settings in this file.
# All Django projects have a settings.py file, and it's crucial for defining the behavior and features of your application.
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rw8*h@_mh05t)52%^9g#o&!h+90ek5#1*^kokme3c^2@fhw8*3"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ ]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "mybe",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "be_crm.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

CORS_ALLOWED_ORIGINS = ['https://localhost:8000/', 'http://localhost:3000/']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = True
CORS_ALLOW_METHODS = True

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "OPTIONS",
    "PUT",
    "DELETE",
    "HEAD",
    "PATCH",    
]

CORS_ALLOW_HEADERS = [
    "Origin",
    "Content-Type",
    "Accept",
    "Access-Control-Allow-Origin",
    "Access-Control-Allow-Methods",
    # Add other allowed headers as needed
]
# Create App: Used python manage.py startapp <app_name> command.
# Description: Created a new Django app with the specified name.
# don't for get to "install the app" see above example (ie "mybe")

REFERRER_POLICY = "no-referrer-when-downgrade"

# no-referrer: This policy specifies that no referrer information is sent in the Referer header.

# no-referrer-when-downgrade: This is the default policy. It sends the full URL (excluding the fragment) when navigating to a same-origin URL or a downgrade navigation (i.e., from HTTPS to HTTP), but it sends no referrer information when navigating from HTTPS to HTTP.

# origin: This policy sends only the origin of the referring URL in the Referer header. The URL's path, query string, and fragment are not included.

# origin-when-cross-origin: This policy sends the full URL (excluding the fragment) when navigating to a same-origin URL. When navigating to a different origin, it sends only the origin of the referring URL.

# same-origin: This policy sends the full URL (excluding the fragment) when navigating within the same origin. When navigating to a different origin, no referrer information is sent.

# strict-origin: This policy sends the origin of the referring URL for both same-origin and cross-origin requests. However, it does not include the path, query string, or fragment.

# strict-origin-when-cross-origin: This policy is similar to strict-origin, but for cross-origin requests, it sends the full URL (excluding the fragment).

# unsafe-url: This policy sends the full URL (including the fragment) in all cases, regardless of the destination.


WSGI_APPLICATION = "be_crm.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
