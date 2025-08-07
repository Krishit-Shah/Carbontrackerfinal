from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Household, EnergyUsage, Transportation, Diet, Waste


class UserRegistrationForm(UserCreationForm):
    """Form for user registration"""
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class HouseholdForm(forms.ModelForm):
    """Form for household information"""
    class Meta:
        model = Household
        fields = ['name', 'address', 'city', 'state', 'pincode', 'family_size']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter household name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter complete address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'state': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('', 'Select State'),
                ('Andhra Pradesh', 'Andhra Pradesh'),
                ('Arunachal Pradesh', 'Arunachal Pradesh'),
                ('Assam', 'Assam'),
                ('Bihar', 'Bihar'),
                ('Chhattisgarh', 'Chhattisgarh'),
                ('Goa', 'Goa'),
                ('Gujarat', 'Gujarat'),
                ('Haryana', 'Haryana'),
                ('Himachal Pradesh', 'Himachal Pradesh'),
                ('Jharkhand', 'Jharkhand'),
                ('Karnataka', 'Karnataka'),
                ('Kerala', 'Kerala'),
                ('Madhya Pradesh', 'Madhya Pradesh'),
                ('Maharashtra', 'Maharashtra'),
                ('Manipur', 'Manipur'),
                ('Meghalaya', 'Meghalaya'),
                ('Mizoram', 'Mizoram'),
                ('Nagaland', 'Nagaland'),
                ('Odisha', 'Odisha'),
                ('Punjab', 'Punjab'),
                ('Rajasthan', 'Rajasthan'),
                ('Sikkim', 'Sikkim'),
                ('Tamil Nadu', 'Tamil Nadu'),
                ('Telangana', 'Telangana'),
                ('Tripura', 'Tripura'),
                ('Uttar Pradesh', 'Uttar Pradesh'),
                ('Uttarakhand', 'Uttarakhand'),
                ('West Bengal', 'West Bengal'),
                ('Delhi', 'Delhi'),
                ('Jammu and Kashmir', 'Jammu and Kashmir'),
                ('Ladakh', 'Ladakh'),
                ('Chandigarh', 'Chandigarh'),
                ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
                ('Daman and Diu', 'Daman and Diu'),
                ('Lakshadweep', 'Lakshadweep'),
                ('Puducherry', 'Puducherry'),
                ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
            ]),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 6-digit pincode'}),
            'family_size': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20}),
        }


class EnergyUsageForm(forms.ModelForm):
    """Form for energy usage data"""
    class Meta:
        model = EnergyUsage
        fields = ['fuel_type', 'consumption', 'unit', 'month']
        widgets = {
            'fuel_type': forms.Select(attrs={'class': 'form-control'}),
            'consumption': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'unit': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('kWh', 'kWh (Electricity)'),
                ('kg', 'kg (LPG, Charcoal)'),
                ('liter', 'Liter (Kerosene)'),
                ('m3', 'm³ (Biogas)'),
                ('kg', 'kg (Firewood)'),
            ]),
            'month': forms.DateInput(attrs={'class': 'form-control', 'type': 'month'}),
        }


class TransportationForm(forms.ModelForm):
    """Form for transportation data"""
    class Meta:
        model = Transportation
        fields = ['vehicle_type', 'distance_km', 'frequency_per_week', 'month']
        widgets = {
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'distance_km': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Distance in kilometers'}),
            'frequency_per_week': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '7', 'placeholder': 'Times per week'}),
            'month': forms.DateInput(attrs={'class': 'form-control', 'type': 'month'}),
        }


class DietForm(forms.ModelForm):
    """Form for dietary consumption data"""
    class Meta:
        model = Diet
        fields = ['food_type', 'consumption_kg', 'month']
        widgets = {
            'food_type': forms.Select(attrs={'class': 'form-control'}),
            'consumption_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Consumption in kg'}),
            'month': forms.DateInput(attrs={'class': 'form-control', 'type': 'month'}),
        }


class WasteForm(forms.ModelForm):
    """Form for waste generation data"""
    class Meta:
        model = Waste
        fields = ['waste_type', 'quantity_kg', 'month']
        widgets = {
            'waste_type': forms.Select(attrs={'class': 'form-control'}),
            'quantity_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Quantity in kg'}),
            'month': forms.DateInput(attrs={'class': 'form-control', 'type': 'month'}),
        }


class BulkDataForm(forms.Form):
    """Form for bulk data entry"""
    month = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'month'}),
        input_formats=['%Y-%m'],
        label='Select Month'
    )
    
    # Energy fields
    electricity_kwh = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'placeholder': 'Electricity in kWh'}),
        label='Electricity (kWh)'
    )
    lpg_kg = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'placeholder': 'LPG in kg'}),
        label='LPG (kg)'
    )
    
    # Transport fields
    car_km = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Car distance in km'}),
        label='Car Distance (km/week)'
    )
    bike_km = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Bike distance in km'}),
        label='Bike Distance (km/week)'
    )
    bus_km = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Bus distance in km'}),
        label='Bus Distance (km/week)'
    )
    
    # Diet fields
    rice_kg = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Rice in kg'}),
        label='Rice (kg)'
    )
    wheat_kg = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Wheat in kg'}),
        label='Wheat (kg)'
    )
    milk_kg = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Milk in kg'}),
        label='Milk (kg)'
    )
    
    # Waste fields
    organic_waste_kg = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Organic waste in kg'}),
        label='Organic Waste (kg)'
    )
    plastic_waste_kg = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'placeholder': 'Plastic waste in kg'}),
        label='Plastic Waste (kg)'
    ) 