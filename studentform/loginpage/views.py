from django.http import JsonResponse
from django.shortcuts import render
from .models import Login


def index(request):
    return render(request, 'index.html')


def student_registration_save(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        registration_num = request.POST.get('registration_num')
        email_id = request.POST.get('email_id')
        phone_num = request.POST.get('phone_num')
        address_id = request.POST.get('address_id')
        country = request.POST.get('country')

        check_reg_num = Login.objects.filter(registration_num=registration_num)
        print(check_reg_num)
        if check_reg_num:
            return JsonResponse({'error': 'registration number exists'}, status=400)
        else:
            details = Login(first_name=first_name, last_name=last_name, registration_num=registration_num,
                            email_id=email_id, phone_num=phone_num, address_id=address_id)
            details.save()

        check_phone_num = Login.objects.filter(phone_num=phone_num)
        print(check_phone_num)
        if check_phone_num:
            return JsonResponse({'error': 'phone number exists'}, status=400)
        else:
            details = Login(first_name=first_name, last_name=last_name, registration_num=registration_num,
                            email_id=email_id, phone_num=phone_num, address_id=address_id)
            details.save()

        check_email_num = Login.objects.filter(email_id=email_id)
        print(check_email_num)
        if check_email_num:
            return JsonResponse({'error': 'email_id already exists'}, status=400)
        else:
            details = Login(first_name=first_name, last_name=last_name, registration_num=registration_num,
                            email_id=email_id, phone_num=phone_num, address_id=address_id)
            details.save()

        return JsonResponse({'success': 'Data saved successfully'}, status=200)
