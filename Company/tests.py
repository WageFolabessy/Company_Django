from django.test import TestCase, Client
from django.urls import reverse
from .models import Company
from .forms import CompanyForm

class CompanyTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.company = Company.objects.create(name='Test Company', field='Test Field')

    def test_index_view(self):
        response = self.client.get(reverse('company:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Company')

    def test_detail_view(self):
        response = self.client.get(reverse('company:detail', args=[self.company.name]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Company')

    def test_create_or_store_view(self):
        response = self.client.post(reverse('company:store'), {'name': 'New Company', 'field': 'New Field'})
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(Company.objects.filter(name='New Company').exists())

    def test_edit_or_update_view(self):
        response = self.client.post(reverse('company:update', args=[self.company.name]), {'name': 'Test Company', 'field': 'Updated Field'})
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.company.refresh_from_db()
        self.assertEqual(self.company.field, 'Updated Field')

    def test_delete_view(self):
        response = self.client.post(reverse('company:delete', args=[self.company.name]))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertFalse(Company.objects.filter(name='Test Company').exists())

    def test_company_form(self):
        form = CompanyForm({'name': 'Test Form Company', 'field': 'Test Form Field'})
        self.assertTrue(form.is_valid())
