from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Article
import pandas as pd
from sklearn.utils import shuffle

import json

fake_data = pd.read_csv("data/archive/Fake.csv")
true_data = pd.read_csv("data/archive/True.csv")
fake_data["label"] = 0
true_data["label"] = 1
frames = [fake_data, true_data]
data = pd.concat(frames)
data.drop(["subject", "date"], axis=1, inplace=True)
df = shuffle(data)
df.reset_index(inplace=True, drop=True)

df.to_json("data.json", orient="records")
 
# Reading from file
f = open("data.json", "r")
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