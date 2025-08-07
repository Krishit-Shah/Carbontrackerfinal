from decimal import Decimal
from datetime import date
from .models import EnergyUsage, Transportation, Diet, Waste, CarbonFootprint


class CarbonCalculator:
    """Class to calculate carbon footprint using Indian emission factors"""
    
    # Indian emission factors (kg CO2e per unit)
    ENERGY_EMISSION_FACTORS = {
        'electricity': 0.82,  # kg CO2e per kWh (Indian grid average)
        'lpg': 2.31,         # kg CO2e per kg
        'kerosene': 2.53,    # kg CO2e per liter
        'biogas': 0.5,       # kg CO2e per m3
        'firewood': 1.5,     # kg CO2e per kg
        'charcoal': 2.93,    # kg CO2e per kg
    }
    
    TRANSPORT_EMISSION_FACTORS = {
        'car_petrol': 0.2,      # kg CO2e per km
        'car_diesel': 0.18,     # kg CO2e per km
        'car_cng': 0.12,        # kg CO2e per km
        'car_electric': 0.05,   # kg CO2e per km (assuming Indian grid)
        'bike_petrol': 0.08,    # kg CO2e per km
        'bike_electric': 0.02,  # kg CO2e per km
        'bus': 0.04,            # kg CO2e per km
        'train': 0.02,          # kg CO2e per km
        'metro': 0.015,         # kg CO2e per km
        'auto': 0.06,           # kg CO2e per km
        'cycle': 0,             # kg CO2e per km
        'walk': 0,              # kg CO2e per km
    }
    
    FOOD_EMISSION_FACTORS = {
        'rice': 2.5,           # kg CO2e per kg
        'wheat': 1.4,          # kg CO2e per kg
        'pulses': 0.9,         # kg CO2e per kg
        'vegetables': 0.4,     # kg CO2e per kg
        'fruits': 0.3,         # kg CO2e per kg
        'milk': 1.4,           # kg CO2e per kg
        'eggs': 4.8,           # kg CO2e per kg
        'chicken': 6.9,        # kg CO2e per kg
        'mutton': 24.0,        # kg CO2e per kg
        'fish': 3.0,           # kg CO2e per kg
        'processed_food': 2.0, # kg CO2e per kg
    }
    
    WASTE_EMISSION_FACTORS = {
        'organic': 0.5,        # kg CO2e per kg
        'plastic': 2.7,        # kg CO2e per kg
        'paper': 0.8,          # kg CO2e per kg
        'glass': 0.3,          # kg CO2e per kg
        'metal': 1.2,          # kg CO2e per kg
        'electronic': 4.5,     # kg CO2e per kg
    }
    
    @classmethod
    def calculate_energy_footprint(cls, household, month):
        """Calculate energy-related carbon footprint"""
        energy_usage = EnergyUsage.objects.filter(
            household=household, 
            month=month
        )
        
        total_footprint = Decimal('0.0')
        for usage in energy_usage:
            factor = cls.ENERGY_EMISSION_FACTORS.get(usage.fuel_type, 0)
            footprint = usage.consumption * Decimal(str(factor))
            total_footprint += footprint
            
        return total_footprint
    
    @classmethod
    def calculate_transport_footprint(cls, household, month):
        """Calculate transportation-related carbon footprint"""
        transport_data = Transportation.objects.filter(
            household=household, 
            month=month
        )
        
        total_footprint = Decimal('0.0')
        for transport in transport_data:
            factor = cls.TRANSPORT_EMISSION_FACTORS.get(transport.vehicle_type, 0)
            # Calculate monthly distance
            monthly_distance = transport.distance_km * transport.frequency_per_week * 4.33
            footprint = monthly_distance * Decimal(str(factor))
            total_footprint += footprint
            
        return total_footprint
    
    @classmethod
    def calculate_diet_footprint(cls, household, month):
        """Calculate diet-related carbon footprint"""
        diet_data = Diet.objects.filter(
            household=household, 
            month=month
        )
        
        total_footprint = Decimal('0.0')
        for diet in diet_data:
            factor = cls.FOOD_EMISSION_FACTORS.get(diet.food_type, 0)
            footprint = diet.consumption_kg * Decimal(str(factor))
            total_footprint += footprint
            
        return total_footprint
    
    @classmethod
    def calculate_waste_footprint(cls, household, month):
        """Calculate waste-related carbon footprint"""
        waste_data = Waste.objects.filter(
            household=household, 
            month=month
        )
        
        total_footprint = Decimal('0.0')
        for waste in waste_data:
            factor = cls.WASTE_EMISSION_FACTORS.get(waste.waste_type, 0)
            footprint = waste.quantity_kg * Decimal(str(factor))
            total_footprint += footprint
            
        return total_footprint
    
    @classmethod
    def calculate_total_footprint(cls, household, month):
        """Calculate total carbon footprint for a household"""
        energy_footprint = cls.calculate_energy_footprint(household, month)
        transport_footprint = cls.calculate_transport_footprint(household, month)
        diet_footprint = cls.calculate_diet_footprint(household, month)
        waste_footprint = cls.calculate_waste_footprint(household, month)
        
        total_footprint = (
            energy_footprint + 
            transport_footprint + 
            diet_footprint + 
            waste_footprint
        )
        
        return {
            'total': total_footprint,
            'energy': energy_footprint,
            'transport': transport_footprint,
            'diet': diet_footprint,
            'waste': waste_footprint,
        }
    
    @classmethod
    def get_indian_average_footprint(cls):
        """Get average Indian household carbon footprint (per person per month)"""
        # Based on Indian household averages
        return {
            'low_income': 150,    # kg CO2e per person per month
            'middle_income': 300, # kg CO2e per person per month
            'high_income': 600,   # kg CO2e per person per month
        }
    
    @classmethod
    def get_footprint_category(cls, footprint_per_person):
        """Categorize footprint as low, medium, or high"""
        if footprint_per_person <= 200:
            return 'low', 'Excellent! You have a low carbon footprint.'
        elif footprint_per_person <= 400:
            return 'medium', 'Good effort! There\'s room for improvement.'
        else:
            return 'high', 'Your footprint is high. Consider making changes.'


def create_sample_tips():
    """Create sample sustainability tips for Indian context"""
    tips_data = [
        {
            'title': 'Switch to LED Bulbs',
            'description': 'Replace traditional bulbs with LED bulbs. They use 75% less energy and last 25 times longer. In India, this can save ₹500-1000 per year on electricity bills.',
            'category': 'energy',
            'impact_kg_co2': 50.0,
            'indian_context': True,
        },
        {
            'title': 'Use Solar Water Heater',
            'description': 'Install a solar water heater. In sunny India, you can meet 60-80% of your hot water needs with solar energy, reducing LPG consumption significantly.',
            'category': 'energy',
            'impact_kg_co2': 200.0,
            'indian_context': True,
        },
        {
            'title': 'Opt for Public Transport',
            'description': 'Use buses, trains, or metro instead of personal vehicles. Delhi Metro alone has helped reduce 2.5 million tons of CO2 emissions annually.',
            'category': 'transport',
            'impact_kg_co2': 100.0,
            'indian_context': True,
        },
        {
            'title': 'Cycle for Short Distances',
            'description': 'Use a bicycle for distances under 5 km. It\'s healthy, saves money on fuel, and produces zero emissions. Many Indian cities now have dedicated cycling lanes.',
            'category': 'transport',
            'impact_kg_co2': 30.0,
            'indian_context': True,
        },
        {
            'title': 'Reduce Meat Consumption',
            'description': 'Try meatless Mondays or reduce meat consumption. Traditional Indian vegetarian diets are not only healthy but also have a lower carbon footprint.',
            'category': 'diet',
            'impact_kg_co2': 80.0,
            'indian_context': True,
        },
        {
            'title': 'Buy Local and Seasonal',
            'description': 'Purchase fruits and vegetables from local markets. This reduces transportation emissions and supports local farmers. Seasonal produce is also cheaper and fresher.',
            'category': 'diet',
            'impact_kg_co2': 40.0,
            'indian_context': True,
        },
        {
            'title': 'Compost Kitchen Waste',
            'description': 'Start composting kitchen waste. In India, 60% of household waste is organic. Composting reduces methane emissions and creates natural fertilizer for your garden.',
            'category': 'waste',
            'impact_kg_co2': 25.0,
            'indian_context': True,
        },
        {
            'title': 'Use Cloth Bags',
            'description': 'Carry cloth bags for shopping. India generates 3.3 million tons of plastic waste annually. Using cloth bags reduces plastic waste and saves money.',
            'category': 'waste',
            'impact_kg_co2': 15.0,
            'indian_context': True,
        },
        {
            'title': 'Install Rainwater Harvesting',
            'description': 'Set up rainwater harvesting at home. In water-scarce regions of India, this can reduce dependence on energy-intensive water supply systems.',
            'category': 'general',
            'impact_kg_co2': 60.0,
            'indian_context': True,
        },
        {
            'title': 'Use Traditional Cooling Methods',
            'description': 'Use traditional methods like clay pots, bamboo screens, and proper ventilation instead of air conditioning when possible. This can reduce electricity consumption by 30-40%.',
            'category': 'energy',
            'impact_kg_co2': 120.0,
            'indian_context': True,
        },
    ]
    
    return tips_data 