from django.core.mail import send_mail


def pattiemtsAccountCreateMail(email, password):
    send_mail(
        "Gulshan Clinick",
        f"Hello! Your Patients sucessfully admited. please login our website http://localhost:5173/  with our provided cradential and see update about patients Password: {password} and Email: {email}",
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
        f"Hello! Doctor. Your account successfully ceated please go this website and with with our creadential http://localhost:5173/ and get update abour work Password: {password} and Email: {email}",
        "hassanrakibul926@gmail.com",
        [email],
        fail_silently=False,
    )