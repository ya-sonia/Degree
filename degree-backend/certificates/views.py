from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import Student


def certificate_view(
    request,
    registration_no
):

    student = get_object_or_404(
        Student,
        registration_no=registration_no
    )

    return render(
        request,
        'certificates/certificate.html',
        {
            'student': student
        }
    )