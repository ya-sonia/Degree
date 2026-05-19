import pandas as pd

from django.core.management.base import BaseCommand

from certificates.models import Department


class Command(BaseCommand):

    help = 'Import departments from excel'

    def handle(self, *args, **kwargs):

        file_path = 'NIT Srinagar.xlsx'

        df = pd.read_excel(
            file_path,
            header=None
        )

        df.columns = [
            'english_name',
            'hindi_name'
        ]

        df = df.dropna()

        skip_rows = [
            'Engineering Departments',
            'Science Departments',
            'Humanities Departments'
        ]

        for _, row in df.iterrows():

            english_name = str(
                row['english_name']
            ).strip()

            hindi_name = str(
                row['hindi_name']
            ).strip()

            if english_name in skip_rows:
                continue

            Department.objects.get_or_create(
                english_name=english_name,
                hindi_name=hindi_name
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Departments Imported Successfully'
            )
        )