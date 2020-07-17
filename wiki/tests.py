from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Article

# Create your tests here.
class Wiki(TestCase):
    def test_details_page(self):
        user = User.objects.create()
        article = Article.objects.create(title="cs is cool", content="Content", author=user)

        response = self.client.get('/w/cs-is-cool', {}, True)
        self.assertContains(response, "cs is cool")
        self.assertEqual(response.status_code, 200)


    def test_details_page_edit(self):
        article = Article.objects.create()
        article.save()

        edit_post = self.client.post('/article/',
        {
            'title': 'edit title',
            'content': 'content is cool',
            'user': 'gonzo'
        })


        self.assertEqual(response.status_code, 302)

    def test_create(self):
        user = User.objects.create()
        user.save()
        article = Article.objects.create(title="cs is cool", content="Content", author=user)
        article.save()

        edit_post = self.client.post('/create/',
        {
            'title': 'edit title',
            'content': 'content is cool',
            'user': 'admin'
        })


        self.assertEqual(response.status_code, 302)
