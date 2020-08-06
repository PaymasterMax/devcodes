import os
import django_heroku , dj_database_url
import dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ghr%=q!3afx83t+1dojl%j15mta%6!v@bpx2l5p+ki2i!)zqs3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG = True
ALLOWED_HOSTS = ['herokudjangoapp.herokuapp.com' , "devcodes.herokuapp.com"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'login.apps.LoginConfig',
    'signup.apps.SignupConfig',
    'uprofile.apps.UprofileConfig',
    'questions.apps.QuestionsConfig',
    "peer.apps.PeerConfig",
    'chatroom.apps.ChatroomConfig',
    'social_django',
    "cloudinary",
]
cloudinary.config(
    cloud_name = "hti2kicdw",
    api_key = "744951147868868",
    api_secret = "R4355opHqPb1UxeGgFR1aABDUyI"
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'devcodes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR , "home/templates"),
                os.path.join(BASE_DIR , "login/templates"),
                os.path.join(BASE_DIR , "signup/templates"),
                os.path.join(BASE_DIR , "uprofile/templates"),
                os.path.join(BASE_DIR , "questions/templates"),
                os.path.join(BASE_DIR , "peer/templates"),
                os.path.join(BASE_DIR , "chatroom/templates"),
                os.path.join(BASE_DIR , "bugs/templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.linkedin.LinkedinOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

WSGI_APPLICATION = 'devcodes.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devcodes',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'',
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR , "static_root")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR , "home/static"),
    os.path.join(BASE_DIR , "login/static"),
    os.path.join(BASE_DIR , "signup/static"),
    os.path.join(BASE_DIR , "uprofile/static"),
    os.path.join(BASE_DIR , "questions/static"),
    os.path.join(BASE_DIR , "peer/static"),
    os.path.join(BASE_DIR , "chatroom/static"),
    os.path.join(BASE_DIR , "bugs/static"),
]
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_GITHUB_KEY = '2cfb028f2d5e0c6f70d1'
SOCIAL_AUTH_GITHUB_SECRET = 'd9e6170c11b6b42a2a541344c57b6b604136fc05'

SOCIAL_AUTH_FACEBOOK_KEY = '579932866026329'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = "ea51c6d0b68c888851a2b9f958042db6"  # App Secret

SOCIAL_AUTH_LINKEDIN_KEY = '78mzuv48xtznlx'  # App ID
SOCIAL_AUTH_LINKEDIN_SECRET = "6rIEsN16ZlZsePAh"  # App Secret

django_heroku.settings(locals())
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , "media_root")
