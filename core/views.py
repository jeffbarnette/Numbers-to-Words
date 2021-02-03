import json

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

from .processors import validate_number, transform_number_to_words

def service_test(request):
    """Function to test to see if everything is working"""
    return HttpResponse('<h3>Service is running!</h3>', status=200)

@csrf_exempt
def num_to_english(request):
    """Function to get number string from request and return response"""
    if request.method == 'GET':
        # querystring ?number=123456789
        number = request.GET.get('number')

    elif request.method == 'POST':
        # Get JSON payload from request body
        json_data = json.loads(request.body)

        try:
            number = json_data['number']
        except KeyError:
            # Invalid or missing key name
            error_message = 'Invalid key provided!'
            return HttpResponseServerError(
                json.dumps({'status': error_message}, indent=4), status=422)
    else:
        # Invalid methods
        error_message = 'Method Not Allowed'
        return HttpResponseServerError(
            json.dumps({'status': error_message}, indent=4),status=405)      

    # Validate number
    if number and validate_number(number):
        words = transform_number_to_words(number)

        if not words:
            # Words were not returned
            error_message = f'Cannot convert {len(number)} numbers to words!'
            return HttpResponseServerError(
                json.dumps({'status': error_message}, indent=4), status=422)
    
        if 'Error' in words:
            # Number string was invalid
            return HttpResponseServerError(
                json.dumps({'status': words}, indent=4), status=422)
    else:
        # Number was invalid
        error_message = 'A valid number was not provided!'
        return HttpResponseServerError(
            json.dumps({'status': error_message}, indent=4), status=422)
    
    response_data = {
        'status': 'OK',
        'num_in_english': words
    }
    return HttpResponse(json.dumps(response_data, indent=4), status=200)