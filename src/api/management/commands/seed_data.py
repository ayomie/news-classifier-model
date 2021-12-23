from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Article
import json

# JSON file
f = open ('/Users/adeot-adegboyega/Documents/projects/data-science/news-classifier-model/src/data.json', "r")
 
# Reading from file
temp_data = json.loads(f.read())
data = []
for item in temp_data:
    obj = {
        "title": item["title"],
        "text": item["text"],
        "label": item["label"]
    }
    data.append(obj)


class Command(BaseCommand):
    help = 'Create articles'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        Article.objects.all().delete()
        self.stdout.write("deleted all articles")
        brand_qs = [Article(**obj) for obj in data]
        Article.objects.bulk_create(brand_qs)
        self.stdout.write(f"created {len(data)} articles")