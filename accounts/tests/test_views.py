from django.test import TestCase
from unittest.mock import patch


class SendLoginEmailViewTest(TestCase):

	def test_redirects_to_home_page(self):
	
		# Django uses mail.outbox to ensure no email is sent
		response = self.client.post('/accounts/send_login_email', data={
			'email': 'karsa@house_of_chains.com'
		})
		
		self.assertRedirects(response, '/')
	
	@patch('accounts.views.send_mail')
	def test_sends_mail_to_address_from_post(self, mock_send_mail):
		self.client.post('/accounts/send_login_email', data={
			'email': 'karsa@house_of_chains.com'
		})	
		
		self.assertEqual(mock_send_mail.called, True)
		
		(subject, body, from_mail, to_list), kwargs = mock_send_mail.call_args
		
		self.assertEqual(subject, 'Your login link for Superlists')
		self.assertEqual(from_mail, 'noreply@superlists')
		self.assertEqual(to_list, ['karsa@house_of_chains.com'])
		
	def test_adds_success_message(self):
		response = self.client.post('/accounts/send_login_email', data={
			'email': 'karsa@house_of_chains.com'
		}, follow=True)
		message = list(response.context['messages'])[0]
		
		self.assertEqual(
			message.message,
			"Check your email, we've sent you a link you can use to log in."
		)
		self.assertEqual(message.tags, "success")
