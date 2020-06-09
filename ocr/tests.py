from django.test import TestCase

from .models import Post

# Create your tests here.
class OcrModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='first file')
        Post.objects.create(description='some description')

    def test_title_content(self):
        ocr = Post.objects.get(id=1)
        expected_object_name = f'{ocr.title}'
        self.assertEquals(expected_object_name, 'first file')

    def test_desription_content(self):
        ocr = Post.objects.get(id=2)
        expected_object_name = f'{ocr.description}'
        self.assertEquals(expected_object_name, 'some description')