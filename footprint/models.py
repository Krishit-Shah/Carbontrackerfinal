from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Household(models.Model):
    """Model to store household information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    family_size = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}'s Household"


class EnergyUsage(models.Model):
    """Model to store energy consumption data"""
    FUEL_CHOICES = [
        ('electricity', 'Electricity'),
        ('lpg', 'LPG'),
        ('kerosene', 'Kerosene'),
        ('biogas', 'Biogas'),
        ('firewood', 'Firewood'),
        ('charcoal', 'Charcoal'),
    ]
    
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)  # kWh, kg, liters, etc.
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.household.name} - {self.fuel_type} - {self.month}"


class Transportation(models.Model):
    """Model to store transportation data"""
    VEHICLE_CHOICES = [
        ('car_petrol', 'Car (Petrol)'),
        ('car_diesel', 'Car (Diesel)'),
        ('car_cng', 'Car (CNG)'),
        ('car_electric', 'Car (Electric)'),
        ('bike_petrol', 'Bike (Petrol)'),
        ('bike_electric', 'Bike (Electric)'),
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('metro', 'Metro'),
        ('auto', 'Auto Rickshaw'),
        ('cycle', 'Cycle'),
        ('walk', 'Walking'),
    ]
    
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    distance_km = models.DecimalField(max_digits=8, decimal_places=2)
    frequency_per_week = models.PositiveIntegerField(default=1)
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.household.name} - {self.vehicle_type} - {self.month}"


class Diet(models.Model):
    """Model to store dietary consumption data"""
    FOOD_CHOICES = [
        ('rice', 'Rice'),
        ('wheat', 'Wheat'),
        ('pulses', 'Pulses'),
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('milk', 'Milk & Dairy'),
        ('eggs', 'Eggs'),
        ('chicken', 'Chicken'),
        ('mutton', 'Mutton'),
        ('fish', 'Fish'),
        ('processed_food', 'Processed Food'),
    ]
    
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    food_type = models.CharField(max_length=20, choices=FOOD_CHOICES)
    consumption_kg = models.DecimalField(max_digits=8, decimal_places=2)
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.household.name} - {self.food_type} - {self.month}"


class Waste(models.Model):
    """Model to store waste generation data"""
    WASTE_CHOICES = [
        ('organic', 'Organic Waste'),
        ('plastic', 'Plastic Waste'),
        ('paper', 'Paper Waste'),
        ('glass', 'Glass Waste'),
        ('metal', 'Metal Waste'),
        ('electronic', 'Electronic Waste'),
    ]
    
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=20, choices=WASTE_CHOICES)
    quantity_kg = models.DecimalField(max_digits=8, decimal_places=2)
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.household.name} - {self.waste_type} - {self.month}"


class CarbonFootprint(models.Model):
    """Model to store calculated carbon footprint"""
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    total_footprint = models.DecimalField(max_digits=10, decimal_places=2)  # in kg CO2e
    energy_footprint = models.DecimalField(max_digits=10, decimal_places=2)
    transport_footprint = models.DecimalField(max_digits=10, decimal_places=2)
    diet_footprint = models.DecimalField(max_digits=10, decimal_places=2)
    waste_footprint = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['household', 'month']

    def __str__(self):
        return f"{self.household.name} - {self.month} - {self.total_footprint} kg CO2e"


class SustainabilityTip(models.Model):
    """Model to store sustainability tips"""
    CATEGORY_CHOICES = [
        ('energy', 'Energy'),
        ('transport', 'Transportation'),
        ('diet', 'Diet'),
        ('waste', 'Waste Management'),
        ('general', 'General'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    impact_kg_co2 = models.DecimalField(max_digits=8, decimal_places=2, help_text="Potential CO2 savings in kg")
    indian_context = models.BooleanField(default=True, help_text="Tip specific to Indian context")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 