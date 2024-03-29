from django.core.mail import send_mail


def pattiemtsAccountCreateMail(email, password):
    send_mail(
        "Gulshan Clinick",
        f"Hello! Your Patients sucessfully admited. please login our website  with our provided cradential and see update about patients Password: {password} and Email: {email}",
        "hassanrakibul926@gmail.com",
        [email],
        fail_silently=False,
    )

def paymentConfirmMail(email, PatientsId, service, paymentType, costOfTreatment):
    send_mail(
        "Gulshan Clinick",
        f"Your Payment Successfully Paid,  Patient Id: {PatientsId},  Service Name: {service},  Payment Type: {paymentType},  Total Amount: {costOfTreatment}tk",
        "hassanrakibul926@gmail.com",
        [email],
        fail_silently=False,
    )


def DoctorAccountCreateMail(email, password):
    send_mail(
        "Gulshan Clinick",
        f"Hello! Doctor. Your account successfully ceated please go heath care website and login by using email and password and get update abour work. Password: {password} and Email: {email}",
        "hassanrakibul926@gmail.com",
        [email],
        fail_silently=False,
    )