from django.core.mail import send_mail


def pattiemtsAccountCreateMail(email, password):
    send_mail(
        "Gulshan Clinick",
        f"Hello! Your Patients sucessfully admited. please login our website http://localhost:5173/  with our provided cradential and see update about patients Password: {password} and Email: {email}",
        "hassanrakibul926@gmail.com",
        [email],
        fail_silently=False,
    )