from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import *
from django.http import JsonResponse
import datetime
from django.shortcuts import render
import json, sys

'''
get all API endpoints
method: GET
'''


@api_view(['GET'])
def api_endpoints(request):
    api_urls = {
        'All Reservations': 'api/reservations/all',
        'All Vacancies Detail': 'api/vacancies/all',

    }

    return Response(api_urls)


'''
get all the reservations from all the customers
method: GET
'''


@api_view(['GET'])
def get_all_reservations(request):
    reservations = RESERVATION.objects.all()
    reservations_serializer = ReservationSerializer(reservations, many=True)
    return Response(reservations_serializer.data)


'''
get all the vacancies available
method: GET
'''


@api_view(['GET'])
def get_all_vacancies(request):
    vacanies = VACANCY.objects.all()
    vacanies_serializer = VacancySerializer(vacanies, many=True)

    return Response(vacanies_serializer.data)


def load_vacancy_limit_data(request):
    start_date = datetime.date(2021, 11, 28)
    number_of_days = 360
    date_list = []
    for day in range(number_of_days):
        a_date = (start_date + datetime.timedelta(days=day)).isoformat()
        date_list.append(a_date)

    for i in date_list:
        obj = VACANCY_LIMIT()
        obj.DATE = i
        obj.LIMIT = str(random.randint(2, 6))
        obj.save()


def home(request):
    from datetime import datetime
    reservation_data = []
    post_obj = RESERVATION.objects.all()
    for obj in post_obj:
        data_dict = dict()
        # data_dict['id'] = obj.id
        data_dict['start_date'] = str(obj.START_DATE.DATE)
        data_dict['end_date'] = str(obj.END_DATE)
        data_dict['start_date_format'] = datetime.strptime(data_dict['start_date'], '%Y-%m-%d').strftime('%m/%d/%Y')
        data_dict['end_date_format'] = datetime.strptime(data_dict['end_date'], '%Y-%m-%d').strftime('%m/%d/%Y')
        data_dict['reservation_status'] = obj.STATUS
        data_dict['reserved_by'] = obj.RESERVED_BY
        data_dict['total_amount'] = obj.TOTAL_AMOUNT
        reservation_data.append(data_dict)
    print(reservation_data)
    return render(request, 'index.html', {"reservation_data": reservation_data})


def save(request):
    from datetime import datetime
    print("ccc")
    post = json.loads(request.POST['reservation_create_list'])
    start_date = list(map(lambda x: x['start_date'], post))
    start_date = datetime.strptime(start_date[0], '%Y-%m-%d').date()
    end_date = list(map(lambda x: x['end_date'], post))
    end_date = datetime.strptime(end_date[0], '%Y-%m-%d').date()
    duration = (end_date - start_date).days
    total_price = int(duration*500)
    print(total_price)

    start_date_match = VACANCY_LIMIT.objects.get(DATE=start_date)
    start_date_match_id = start_date_match.id
    vacancy_limit = start_date_match.LIMIT
    new_vacancy_limit = int(vacancy_limit) - 1
    print(start_date_match_id)
    print("old", vacancy_limit)
    print("new", new_vacancy_limit)
    reservation_obj = RESERVATION()
    reservation_obj.START_DATE = start_date_match
    reservation_obj.END_DATE = end_date
    reservation_obj.STATUS = 1
    reservation_obj.RESERVED_BY = 'Mahabub'
    reservation_obj.TOTAL_AMOUNT = total_price
    reservation_obj.save()
    vacancy_limit_obj = VACANCY_LIMIT.objects.get(DATE=start_date)
    vacancy_limit_obj.LIMIT = new_vacancy_limit
    vacancy_limit_obj.save()
    data_dict = dict()
    data_dict["status"] = "202"
    data_dict["message"] = "data saved"
    return JsonResponse(data_dict)
