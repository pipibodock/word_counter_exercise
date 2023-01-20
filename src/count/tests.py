from django.test import TestCase
from django.urls import reverse

from count.forms import WordCountForm
from count.services import count_text


class HomeViewTestCase(TestCase):

    def test_home_return_200_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)

    def test_home_return_expected_html(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'count/home.html')
        self.assertTrue(b'<title>Word Count' in response.content)


class CountFormTestCase(TestCase):

    def test_form_is_valid(self):
        form = WordCountForm({"body": "some body"})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = WordCountForm({"body": ""})
        self.assertFalse(form.is_valid())


class CountViewTestCase(TestCase):

    def test_get_count_page_return_200_status_code(self):
        response = self.client.get(reverse('count'))
        self.assertEqual(200, response.status_code)

    def test_post_counter_with_valid_value_return_200_status_code(self):
        response = self.client.post(reverse('count'), {"body": "dummy body"})
        self.assertEqual(200, response.status_code)


class ServiceTestCase(TestCase):

    def test_count_words_with_short_text(self):
        result = count_text("simple text")
        self.assertEqual(result, 2)

    def test_count_words_with_unique_text(self):
        result = count_text("unique")
        self.assertEqual(result, 1)

    def test_count_words_with_long_text(self):
        text_43_words = """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry.
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        """
        result = count_text(text_43_words)
        self.assertEqual(result, 43)