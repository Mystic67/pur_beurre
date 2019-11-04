# Generated by Django 2.2.5 on 2019-11-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150, verbose_name='Nom du produit')),
                ('generic_name_fr', models.CharField(max_length=300, verbose_name='Nom générique')),
                ('brands', models.CharField(max_length=150, verbose_name='Marque')),
                ('nutrition_grade_fr', models.CharField(max_length=10, verbose_name='Nutri-score')),
                ('nova_groups', models.CharField(max_length=10, verbose_name='Groupe Nova')),
                ('ingredients_text_fr', models.CharField(max_length=2000, verbose_name="Liste d'Ingredients")),
                ('url', models.URLField(max_length=255, verbose_name='URL vers le produit')),
                ('image_url', models.URLField(max_length=255, verbose_name="URL vers l'image du produit")),
                ('categories', models.ManyToManyField(related_name='categories', to='store.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Substitutes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('prod_base', models.ForeignKey(on_delete=True, related_name='prod_base', to='store.Products')),
                ('prod_substitute', models.ForeignKey(on_delete=True, related_name='prod_substitute', to='store.Products')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='substitutes',
            field=models.ManyToManyField(related_name='substitute', through='store.Substitutes', to='store.Products'),
        ),
        migrations.CreateModel(
            name='Nutriments_for_100g',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Non du nutriments')),
                ('quantity', models.CharField(max_length=10, verbose_name='Quantité pour 100g')),
                ('product', models.ManyToManyField(related_name='Produit', to='store.Products')),
            ],
        ),
    ]
