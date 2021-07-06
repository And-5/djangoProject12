from django.utils import translation
from django.conf import settings


class LanguageCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Sets language from the cookie value.
        """
        language = settings.LANGUAGE_CODE

        if settings.LANGUAGE_COOKIE_NAME in request.COOKIES:
            language = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)

        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()

        response = self.get_response(request)
        translation.deactivate()

        return response
