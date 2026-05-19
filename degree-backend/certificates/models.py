from django.db import models
from num2words import num2words

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator


# =========================================
# MONTH CHOICES
# =========================================

MONTH_CHOICES = [

    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
]


# =========================================
# MONTH TRANSLATIONS
# =========================================

MONTH_HINDI = {

    'January': 'जनवरी',
    'February': 'फरवरी',
    'March': 'मार्च',
    'April': 'अप्रैल',
    'May': 'मई',
    'June': 'जून',
    'July': 'जुलाई',
    'August': 'अगस्त',
    'September': 'सितंबर',
    'October': 'अक्टूबर',
    'November': 'नवंबर',
    'December': 'दिसंबर',
}


# =========================================
# DEGREE CHOICES
# =========================================

DEGREE_CHOICES = [

    (
        'BTECH',
        'Bachelor of Technology'
    ),

    (
        'MTECH',
        'Master of Technology'
    ),

    (
        'PHD',
        'Doctor of Philosophy'
    ),
]


# =========================================
# DEGREE HINDI
# =========================================

DEGREE_HINDI = {

    'BTECH': 'प्रौद्योगिकी में स्नातक',

    'MTECH': 'प्रौद्योगिकी में परास्नातक',

    'PHD': 'विद्यावारिधि',
}


# =========================================
# DEPARTMENT MODEL
# =========================================

class Department(models.Model):

    english_name = models.CharField(
        max_length=255,
        unique=True
    )

    hindi_name = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self):

        return (
        f'{self.english_name} '
        f'({self.hindi_name})'
    )


# =========================================
# STUDENT MODEL
# =========================================

class Student(models.Model):
    class Meta:

        ordering = ['-completion_year']

        verbose_name = 'Student Certificate'

        verbose_name_plural = 'Student Certificates'

    # =====================================
    # BASIC DETAILS
    # =====================================

    registration_no = models.CharField(
        max_length=100,
        db_index=True,
        unique=True,
        validators=[
        RegexValidator(
            regex=r'^[0-9]{4}NITSGR[0-9]+$',
            message='Example: 2020NITSGR033'
            )
        ],
        help_text='Example: 2020NITSGR033'
    )

    enrollment_no = models.CharField(
        max_length=100,
         validators=[
        RegexValidator(
            regex=r'^[A-Z]+\/[0-9]+\/[0-9]+$',
            message='Example: ITE/22/16'
        )
    ],
        help_text='Example: ITE/22/16'
    )

    english_name = models.CharField(
        max_length=255,
        help_text='Example: Sonia Yadav'
    )

    hindi_name = models.CharField(
        max_length=255,
        help_text='Example: सोनिया यादव'
    )

    # =====================================
    # DEGREE
    # =====================================

    degree = models.CharField(
        max_length=20,
        choices=DEGREE_CHOICES,
        default='BTECH'
    )

    # =====================================
    # DEPARTMENT
    # =====================================

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT
    )

    # =====================================
    # CGPA
    # =====================================

    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    # =====================================
    # COURSE COMPLETION
    # =====================================

    completion_month = models.CharField(
        max_length=20,
        choices=MONTH_CHOICES,
        default='July'
    )

    completion_year = models.PositiveIntegerField(db_index=True)

    # =====================================
    # AWARD DATE
    # =====================================

    award_date = models.DateField()

    # =====================================
    # PHOTO
    # =====================================

    student_photo = models.ImageField(
    upload_to='students/',
    validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png']
            )
        ]
    )

    # =====================================
    # TIMESTAMP
    # =====================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # =====================================
    # METHODS
    # =====================================

    @property
    def hindi_month(self):

        return MONTH_HINDI.get(
            self.completion_month,
            self.completion_month
        )

    @property
    def hindi_degree(self):

        return DEGREE_HINDI.get(
            self.degree,
            self.degree
        )

    @property
    def english_degree(self):

        return dict(
            DEGREE_CHOICES
        ).get(
            self.degree,
            self.degree
        )

    @property
    def formatted_hindi_date(self):

        month = MONTH_HINDI.get(
            self.award_date.strftime('%B')
        )

        return (
            f'{self.award_date.day} '
            f'{month} '
            f'{self.award_date.year}'
        )
        
    
    # @property
    # def formatted_english_date(self):

    #     return self.award_date.strftime(
    #         '%d %B %Y'
    #     )

    def __str__(self):

        return (
            f'{self.english_name} '
            f'({self.registration_no})'
        )
    
    @property
    def formatted_award_date(self):

        day = self.award_date.day
        month = self.award_date.strftime('%B')
        year = self.award_date.year

        # Convert day to ordinal words
        day_word = num2words(day, to='ordinal').capitalize()

        # Convert year to words
        year_word = num2words(year).replace('-', ' ').title()
        # year_word = num2words(year).title()

        return f"{day_word} day of {month} of the year {year_word}"



