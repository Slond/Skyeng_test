from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    picture = models.URLField(default='https://place-hold.it/100x60')
# Так как наше приложение русскоязычное, следует дополнить каждую модель:
# class Meta, с переменными verbose_name - это даст Django знать, как правильно склоняется название модели;
# ```def __str__``` - это даст более понятное описание модели, при использовании из Shell и не только.

class Company(models.Model):
    id = models.IntegerField(primary_key=True) #Это избыточное поле, т.к. Django по умолчанию создает первичный ключ ```id```. Далее аналогично
    title = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    posted = models.DateField()

# Можно лучше: в каждой модели есть одинаковое поле ```title```, и появятся ```class Meta``` и ```def __str__```. По принципам DRY оптимальнее будет сделать родительский класс с этими полями, и затем наследоваться от него.



