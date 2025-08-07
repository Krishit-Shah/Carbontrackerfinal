from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum, Avg
from django.utils import timezone
from datetime import datetime, date
from decimal import Decimal
import json

from .models import (
    Household, EnergyUsage, Transportation, Diet, Waste, 
    CarbonFootprint, SustainabilityTip
)
from .forms import (
    UserRegistrationForm, HouseholdForm, EnergyUsageForm, 
    TransportationForm, DietForm, WasteForm, BulkDataForm
)
from .utils import CarbonCalculator, create_sample_tips


def home(request):
    """Home page view"""
    return render(request, 'footprint/home.html')


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'footprint/register.html', {'form': form})


@login_required
def dashboard(request):
    """Main dashboard view"""
    try:
        household = Household.objects.get(user=request.user)
    except Household.DoesNotExist:
        return redirect('setup_household')
    
    # Get current month's footprint
    current_month = date.today().replace(day=1)
    try:
        current_footprint = CarbonFootprint.objects.get(
            household=household, 
            month=current_month
        )
    except CarbonFootprint.DoesNotExist:
        current_footprint = None
    
    # Get historical data for charts
    footprints = CarbonFootprint.objects.filter(
        household=household
    ).order_by('month')[:12]  # Last 12 months
    
    # Get tips
    tips = SustainabilityTip.objects.filter(indian_context=True)[:5]
    
    # Calculate per person footprint
    if current_footprint:
        per_person = current_footprint.total_footprint / household.family_size
        category, message = CarbonCalculator.get_footprint_category(per_person)
    else:
        per_person = 0
        category = 'unknown'
        message = 'No data available for current month.'
    
    context = {
        'household': household,
        'current_footprint': current_footprint,
        'footprints': footprints,
        'tips': tips,
        'per_person': per_person,
        'category': category,
        'message': message,
    }
    
    return render(request, 'footprint/dashboard.html', context)


@login_required
def setup_household(request):
    """Setup household information"""
    if request.method == 'POST':
        form = HouseholdForm(request.POST)
        if form.is_valid():
            household = form.save(commit=False)
            household.user = request.user
            household.save()
            messages.success(request, 'Household setup completed!')
            return redirect('dashboard')
    else:
        form = HouseholdForm()
    
    return render(request, 'footprint/setup_household.html', {'form': form})


@login_required
def add_energy_data(request):
    """Add energy usage data"""
    household = get_object_or_404(Household, user=request.user)
    
    if request.method == 'POST':
        form = EnergyUsageForm(request.POST)
        if form.is_valid():
            energy_data = form.save(commit=False)
            energy_data.household = household
            energy_data.save()
            messages.success(request, 'Energy data added successfully!')
            return redirect('dashboard')
    else:
        form = EnergyUsageForm()
    
    return render(request, 'footprint/add_energy_data.html', {'form': form})


@login_required
def add_transport_data(request):
    """Add transportation data"""
    household = get_object_or_404(Household, user=request.user)
    
    if request.method == 'POST':
        form = TransportationForm(request.POST)
        if form.is_valid():
            transport_data = form.save(commit=False)
            transport_data.household = household
            transport_data.save()
            messages.success(request, 'Transportation data added successfully!')
            return redirect('dashboard')
    else:
        form = TransportationForm()
    
    return render(request, 'footprint/add_transport_data.html', {'form': form})


@login_required
def add_diet_data(request):
    """Add dietary consumption data"""
    household = get_object_or_404(Household, user=request.user)
    
    if request.method == 'POST':
        form = DietForm(request.POST)
        if form.is_valid():
            diet_data = form.save(commit=False)
            diet_data.household = household
            diet_data.save()
            messages.success(request, 'Diet data added successfully!')
            return redirect('dashboard')
    else:
        form = DietForm()
    
    return render(request, 'footprint/add_diet_data.html', {'form': form})


@login_required
def add_waste_data(request):
    """Add waste generation data"""
    household = get_object_or_404(Household, user=request.user)
    
    if request.method == 'POST':
        form = WasteForm(request.POST)
        if form.is_valid():
            waste_data = form.save(commit=False)
            waste_data.household = household
            waste_data.save()
            messages.success(request, 'Waste data added successfully!')
            return redirect('dashboard')
    else:
        form = WasteForm()
    
    return render(request, 'footprint/add_waste_data.html', {'form': form})


@login_required
def bulk_data_entry(request):
    """Bulk data entry form"""
    household = get_object_or_404(Household, user=request.user)
    
    if request.method == 'POST':
        form = BulkDataForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            
            # Save energy data
            if form.cleaned_data['electricity_kwh']:
                EnergyUsage.objects.create(
                    household=household,
                    fuel_type='electricity',
                    consumption=form.cleaned_data['electricity_kwh'],
                    unit='kWh',
                    month=month
                )
            
            if form.cleaned_data['lpg_kg']:
                EnergyUsage.objects.create(
                    household=household,
                    fuel_type='lpg',
                    consumption=form.cleaned_data['lpg_kg'],
                    unit='kg',
                    month=month
                )
            
            # Save transport data
            if form.cleaned_data['car_km']:
                Transportation.objects.create(
                    household=household,
                    vehicle_type='car_petrol',
                    distance_km=form.cleaned_data['car_km'],
                    frequency_per_week=1,
                    month=month
                )
            
            if form.cleaned_data['bike_km']:
                Transportation.objects.create(
                    household=household,
                    vehicle_type='bike_petrol',
                    distance_km=form.cleaned_data['bike_km'],
                    frequency_per_week=1,
                    month=month
                )
            
            if form.cleaned_data['bus_km']:
                Transportation.objects.create(
                    household=household,
                    vehicle_type='bus',
                    distance_km=form.cleaned_data['bus_km'],
                    frequency_per_week=1,
                    month=month
                )
            
            # Save diet data
            if form.cleaned_data['rice_kg']:
                Diet.objects.create(
                    household=household,
                    food_type='rice',
                    consumption_kg=form.cleaned_data['rice_kg'],
                    month=month
                )
            
            if form.cleaned_data['wheat_kg']:
                Diet.objects.create(
                    household=household,
                    food_type='wheat',
                    consumption_kg=form.cleaned_data['wheat_kg'],
                    month=month
                )
            
            if form.cleaned_data['milk_kg']:
                Diet.objects.create(
                    household=household,
                    food_type='milk',
                    consumption_kg=form.cleaned_data['milk_kg'],
                    month=month
                )
            
            # Save waste data
            if form.cleaned_data['organic_waste_kg']:
                Waste.objects.create(
                    household=household,
                    waste_type='organic',
                    quantity_kg=form.cleaned_data['organic_waste_kg'],
                    month=month
                )
            
            if form.cleaned_data['plastic_waste_kg']:
                Waste.objects.create(
                    household=household,
                    waste_type='plastic',
                    quantity_kg=form.cleaned_data['plastic_waste_kg'],
                    month=month
                )
            
            messages.success(request, 'Bulk data added successfully!')
            return redirect('calculate_footprint', month=month.strftime('%Y-%m'))
    else:
        form = BulkDataForm()
    
    return render(request, 'footprint/bulk_data_entry.html', {'form': form})


@login_required
def calculate_footprint(request, month=None):
    """Calculate carbon footprint for a specific month"""
    household = get_object_or_404(Household, user=request.user)
    
    if month:
        try:
            month_date = datetime.strptime(month, '%Y-%m').date().replace(day=1)
        except ValueError:
            messages.error(request, 'Invalid month format.')
            return redirect('dashboard')
    else:
        month_date = date.today().replace(day=1)
    
    # Calculate footprint
    footprint_data = CarbonCalculator.calculate_total_footprint(household, month_date)
    
    # Save or update footprint
    footprint, created = CarbonFootprint.objects.update_or_create(
        household=household,
        month=month_date,
        defaults={
            'total_footprint': footprint_data['total'],
            'energy_footprint': footprint_data['energy'],
            'transport_footprint': footprint_data['transport'],
            'diet_footprint': footprint_data['diet'],
            'waste_footprint': footprint_data['waste'],
        }
    )
    
    # Get per person footprint
    per_person = footprint.total_footprint / household.family_size
    category, message = CarbonCalculator.get_footprint_category(per_person)
    
    # Get Indian averages
    indian_averages = CarbonCalculator.get_indian_average_footprint()
    
    context = {
        'household': household,
        'footprint': footprint,
        'per_person': per_person,
        'category': category,
        'message': message,
        'indian_averages': indian_averages,
        'month': month_date,
    }
    
    return render(request, 'footprint/calculate_footprint.html', context)


@login_required
def tips(request):
    """Sustainability tips page"""
    category = request.GET.get('category', '')
    
    if category:
        tips = SustainabilityTip.objects.filter(
            category=category, 
            indian_context=True
        )
    else:
        tips = SustainabilityTip.objects.filter(indian_context=True)
    
    context = {
        'tips': tips,
        'selected_category': category,
    }
    
    return render(request, 'footprint/tips.html', context)


@login_required
def reports(request):
    """Generate reports and analytics"""
    household = get_object_or_404(Household, user=request.user)
    
    # Get last 12 months of data
    footprints = CarbonFootprint.objects.filter(
        household=household
    ).order_by('month')[:12]
    
    # Calculate averages
    if footprints:
        avg_total = footprints.aggregate(Avg('total_footprint'))['total_footprint__avg']
        avg_energy = footprints.aggregate(Avg('energy_footprint'))['energy_footprint__avg']
        avg_transport = footprints.aggregate(Avg('transport_footprint'))['transport_footprint__avg']
        avg_diet = footprints.aggregate(Avg('diet_footprint'))['diet_footprint__avg']
        avg_waste = footprints.aggregate(Avg('waste_footprint'))['waste_footprint__avg']
    else:
        avg_total = avg_energy = avg_transport = avg_diet = avg_waste = 0
    
    # Get Indian averages
    indian_averages = CarbonCalculator.get_indian_average_footprint()
    
    context = {
        'household': household,
        'footprints': footprints,
        'avg_total': avg_total,
        'avg_energy': avg_energy,
        'avg_transport': avg_transport,
        'avg_diet': avg_diet,
        'avg_waste': avg_waste,
        'indian_averages': indian_averages,
    }
    
    return render(request, 'footprint/reports.html', context)


@login_required
def api_footprint_data(request):
    """API endpoint for chart data"""
    household = get_object_or_404(Household, user=request.user)
    
    footprints = CarbonFootprint.objects.filter(
        household=household
    ).order_by('month')[:12]
    
    data = {
        'labels': [f.month.strftime('%b %Y') for f in footprints],
        'datasets': [
            {
                'label': 'Total Footprint',
                'data': [float(f.total_footprint) for f in footprints],
                'borderColor': '#28a745',
                'backgroundColor': 'rgba(40, 167, 69, 0.1)',
            },
            {
                'label': 'Energy',
                'data': [float(f.energy_footprint) for f in footprints],
                'borderColor': '#ffc107',
                'backgroundColor': 'rgba(255, 193, 7, 0.1)',
            },
            {
                'label': 'Transport',
                'data': [float(f.transport_footprint) for f in footprints],
                'borderColor': '#17a2b8',
                'backgroundColor': 'rgba(23, 162, 184, 0.1)',
            },
            {
                'label': 'Diet',
                'data': [float(f.diet_footprint) for f in footprints],
                'borderColor': '#dc3545',
                'backgroundColor': 'rgba(220, 53, 69, 0.1)',
            },
            {
                'label': 'Waste',
                'data': [float(f.waste_footprint) for f in footprints],
                'borderColor': '#6c757d',
                'backgroundColor': 'rgba(108, 117, 125, 0.1)',
            },
        ]
    }
    
    return JsonResponse(data)


def setup_sample_data(request):
    """Setup sample data for demonstration"""
    if request.method == 'POST':
        # Create sample tips
        tips_data = create_sample_tips()
        for tip_data in tips_data:
            SustainabilityTip.objects.get_or_create(
                title=tip_data['title'],
                defaults=tip_data
            )
        
        messages.success(request, 'Sample data created successfully!')
        return redirect('dashboard')
    
    return render(request, 'footprint/setup_sample_data.html') 