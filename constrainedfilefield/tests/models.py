from django.db import models

from constrainedfilefield.fields import ConstrainedFileField, ConstrainedImageField


class TestModel(models.Model):
    the_file = ConstrainedFileField(
        null=True,
        blank=True,
        upload_to='testfile',
        content_types=['image/png'],
        max_upload_size=10240)
    the_image = ConstrainedImageField(
        null=True,
        blank=True,
        upload_to='testfile',
        content_types=['image/png'],
        min_upload_size=1024,
        max_upload_size=10240)


class TestModelJs(models.Model):
    the_file = ConstrainedFileField(
        null=True,
        blank=True,
        upload_to='testfile',
        content_types=['image/png'],
        max_upload_size=10240,
        js_checker=True)
    the_image = ConstrainedImageField(
        null=True,
        blank=True,
        upload_to='testfile',
        content_types=['image/png'],
        min_upload_size=1024,
        max_upload_size=10240,
        js_checker=True)


class TestModelNoValidate(models.Model):
    the_file = ConstrainedFileField(
        null=True,
        blank=True,
        upload_to='testfile')
    the_image = ConstrainedImageField(
        null=True,
        blank=True,
        upload_to='testfile')


class TestContainer(models.Model):
    name = models.CharField(max_length=100)


class TestElement(models.Model):
    container = models.ForeignKey(
        TestContainer,
        on_delete=models.CASCADE,
        related_name='test_elements')
    the_file = ConstrainedFileField(
        null=True,
        blank=True,
        upload_to='testfile',
        content_types=['image/png', 'image/jpeg'])
