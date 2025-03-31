from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from treinos.models import GymProfile

class GymProfileTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_gym_profile(self):
        """
        Testa a criação de um novo perfil de ginásio.
        """
        self.client.login(username='testuser', password='testpassword')

        url = reverse('gym_profile_form')
        response = self.client.post(url, {
            'altura': 180,  
            'peso': 75,
            'objetivos': 'ganhar_peso',
            'dias_treino': '3_4',
        })
        
        self.assertRedirects(response, reverse('home'))
        
        profile = GymProfile.objects.filter(user=self.user).first()
        self.assertIsNotNone(profile)
        self.assertEqual(profile.altura, 180)  
        self.assertEqual(profile.peso, 75)    
        self.assertEqual(profile.objetivos, 'ganhar_peso')
        self.assertEqual(profile.dias_treino, '3_4')

    def test_profile_not_duplicate(self):
        """
        Testa se um perfil de ginásio existente não é duplicado.
        """
        GymProfile.objects.create(user=self.user, altura=175, peso=70, objetivos='manter_peso', dias_treino='2_3')

        self.client.login(username='testuser', password='testpassword')

        url = reverse('gym_profile_form')
        response = self.client.post(url, {
            'altura': 180, 
            'peso': 80, 
            'objetivos': 'perder_peso', 
            'dias_treino': '4_5',
        })

        profile = GymProfile.objects.filter(user=self.user).first()
        self.assertEqual(profile.altura, 180) 
        self.assertEqual(profile.peso, 80)    
        self.assertEqual(profile.objetivos, 'perder_peso')
        self.assertEqual(profile.dias_treino, '4_5')

    def test_update_gym_profile(self):
        """
        Testa a atualização do perfil de ginásio existente.
        """
        GymProfile.objects.create(user=self.user, altura=175, peso=70, objetivos='manter_peso', dias_treino='2_3')

        self.client.login(username='testuser', password='testpassword')

        url = reverse('gym_profile_form')
        response = self.client.post(url, {
            'altura': 180, 
            'peso': 80,    
            'objetivos': 'perder_peso', 
            'dias_treino': '4_5',       
        })
        
        self.assertRedirects(response, reverse('home'))
        
        profile = GymProfile.objects.get(user=self.user)
        self.assertEqual(profile.altura, 180)
        self.assertEqual(profile.peso, 80)
        self.assertEqual(profile.objetivos, 'perder_peso')
        self.assertEqual(profile.dias_treino, '4_5')
