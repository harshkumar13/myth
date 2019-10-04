from tom_observations.facility import GenericObservationFacility, GenericObservationForm
from django import forms

class MyObservationFacilityForm(GenericObservationForm):
    exposure_time = forms.IntegerField()
    exposure_count = forms.IntegerField()



class MyObservationFacility(GenericObservationFacility):
    name = 'MyFacility'
    observation_types = [('Observation', 'Custom Observation'), ('SPECTRA', 'Spectroscopy')]

    SITES = {
    'Itagaki': {
        'latitude': 32.8,
        'longitude': 78.9,
        'elevation': 4500
        }
    }
    

    def data_products(self, observation_id, product_id=None):
        return

    def get_form(self, observation_type):
        return MyObservationFacilityForm

    def get_observation_status(self, observation_id):
        return ['IN_PROGRESS']

    def get_observation_url(self, observation_id):
        return ''

    def get_observing_sites(self):
        return  self.SITES

    def get_terminal_observing_states(self):
        return ['IN_PROGRESS', 'COMPLETED']

    def submit_observation(self, observation_payload):
        print(observation_payload)
        return [1]

    def validate_observation(self, observation_payload):
        pass
