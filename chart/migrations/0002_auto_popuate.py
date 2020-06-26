import csv
import os
from django.db import migrations
from django.conf import settings

# csv 파일의 해당 열 번호를 상수로 정의
Date=0  # 승차권 등급
Country=1      # 생존 여부
Confirmed=2          # 이름
Recovered=3           # 성별
Deaths=4           # 나이

def add_case(apps, schema_editor):
    Covid19 = apps.get_model('chart', 'Covid19')  # (app_label, model_name)
    csv_file = os.path.join(settings.BASE_DIR, 'countries-aggregated.csv')
    with open(csv_file) as dataset:                   # 파일 객체 dataset
        reader = csv.reader(dataset)                    # 파일 객체 dataset에 대한 판독기 획득
        next(reader)  # ignore first row (headers)      # __next__() 호출 때마다 한 라인 판독
        for entry in reader:                            # 판독기에 대하여 반복 처리
            Covid19.objects.create(                       # DB 행 생성
                date=entry[Date],
                country=entry[Country],
                confirmed=int(entry[Confirmed]),      # int()로 변환
                recovered=int(entry[Recovered]),  # int()로 변환
                deaths=int(entry[Deaths]),  # int()로 변환
            )

class Migration(migrations.Migration):
    dependencies = [                            # 선행 관계
        ('chart', '0001_initial'),         # app_label, preceding migration file
    ]
    operations = [                              # 작업
        migrations.RunPython(add_case),   # add_passengers 함수를 호출
    ]