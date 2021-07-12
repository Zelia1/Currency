from currency.models import Analytics


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        response_cod = response.status_code

        Analytics.objects.create(
            path=request.path,
            status_code=response_cod,
        )

        return response
