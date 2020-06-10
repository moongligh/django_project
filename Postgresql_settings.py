DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # sql 엔진 설정
        'NAME':'django_db', # 데이터베이스 이름
        'USER':'admin_role', # 데이터베이스 연결시 사용할 유저 이름
        'PASSWORD':'q1w2e3r4', # 유저 패스워드
        'HOST':'localhost',
        'PORT':'5432'
    } 
}