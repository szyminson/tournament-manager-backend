# Generated by Django 4.0.4 on 2022-04-24 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=45)),
                ('club_ceo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Duel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_description', models.TextField()),
                ('parent_duel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.duel')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('hashed_password', models.CharField(max_length=45)),
                ('user_type', models.CharField(choices=[('A', 'Administrator'), ('M', 'Moderator')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('participants_limit', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.club')),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('root_duel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.duel')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('N', 'None'), ('M', 'Male'), ('F', 'Female')], default='N', max_length=1)),
                ('date_of_birth', models.DateField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.club')),
                ('verification_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.verificationcode')),
            ],
        ),
        migrations.AddField(
            model_name='duel',
            name='participant_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_one', to='api.participant'),
        ),
        migrations.AddField(
            model_name='duel',
            name='participant_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_two', to='api.participant'),
        ),
        migrations.AddField(
            model_name='duel',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weiner', to='api.participant'),
        ),
    ]
