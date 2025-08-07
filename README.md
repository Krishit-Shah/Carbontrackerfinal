# Carbon Footprint Tracker - India

A comprehensive web application designed specifically for Indian households to track and reduce their carbon footprint. Built with Django and Bootstrap, this application provides Indian-specific calculations, tips, and recommendations for sustainable living.

## 🌟 Features

### Core Functionality
- **Carbon Footprint Calculation**: Accurate calculations using Indian emission factors
- **Multi-Category Tracking**: Energy, Transportation, Diet, and Waste management
- **Indian Context**: Tailored for Indian households with local transportation, food habits, and waste patterns
- **Personalized Dashboard**: Visual representation of carbon footprint with charts and trends
- **Sustainability Tips**: Indian-specific recommendations for reducing environmental impact

### Technical Features
- **Django ORM**: Robust data storage and management
- **Bootstrap 5**: Modern, responsive UI design
- **Chart.js**: Interactive data visualization
- **REST API**: For external data integration
- **User Authentication**: Secure user registration and login
- **Admin Panel**: Comprehensive data management interface

## 🏗️ Architecture

### Models
- **Household**: User household information and family size
- **EnergyUsage**: Electricity, LPG, and other fuel consumption
- **Transportation**: Personal vehicles, public transport, and travel patterns
- **Diet**: Food consumption patterns and dietary choices
- **Waste**: Waste generation and disposal methods
- **CarbonFootprint**: Calculated carbon footprint data
- **SustainabilityTip**: Indian-specific sustainability recommendations

### Indian-Specific Features
- **Emission Factors**: Based on India's energy mix and consumption patterns
- **Transportation Options**: Includes auto-rickshaws, metro, and Indian public transport
- **Food Categories**: Traditional Indian food items and consumption patterns
- **Waste Management**: Addresses India's unique waste composition
- **Cost Savings**: Tips with Indian Rupee savings calculations

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Carbon-Footprint-Tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Setup sample data (optional)**
   ```bash
   python manage.py runserver
   # Visit http://localhost:8000/setup-sample-data/
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## 📊 Usage

### For Users

1. **Registration**: Create an account and set up household information
2. **Data Entry**: Add monthly consumption data for:
   - Energy (electricity, LPG, etc.)
   - Transportation (personal vehicles, public transport)
   - Diet (food consumption patterns)
   - Waste (waste generation)
3. **View Results**: Get detailed carbon footprint analysis with Indian averages
4. **Get Tips**: Receive personalized sustainability recommendations
5. **Track Progress**: Monitor improvements over time with charts and reports

### For Administrators

1. **Admin Panel**: Access comprehensive data management at `/admin/`
2. **User Management**: Monitor user accounts and household data
3. **Tips Management**: Add and manage sustainability tips
4. **Data Analytics**: View aggregated carbon footprint data

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration
The application uses SQLite by default. For production, configure PostgreSQL or MySQL in `settings.py`.

## 📈 Indian Emission Factors

The application uses scientifically validated emission factors specific to India:

### Energy (kg CO₂e per unit)
- Electricity: 0.82 kg CO₂e/kWh (Indian grid average)
- LPG: 2.31 kg CO₂e/kg
- Kerosene: 2.53 kg CO₂e/liter
- Biogas: 0.5 kg CO₂e/m³
- Firewood: 1.5 kg CO₂e/kg
- Charcoal: 2.93 kg CO₂e/kg

### Transportation (kg CO₂e per km)
- Car (Petrol): 0.2 kg CO₂e/km
- Car (Diesel): 0.18 kg CO₂e/km
- Car (CNG): 0.12 kg CO₂e/km
- Car (Electric): 0.05 kg CO₂e/km
- Bike (Petrol): 0.08 kg CO₂e/km
- Bus: 0.04 kg CO₂e/km
- Train: 0.02 kg CO₂e/km
- Metro: 0.015 kg CO₂e/km
- Auto-rickshaw: 0.06 kg CO₂e/km

### Food (kg CO₂e per kg)
- Rice: 2.5 kg CO₂e/kg
- Wheat: 1.4 kg CO₂e/kg
- Pulses: 0.9 kg CO₂e/kg
- Vegetables: 0.4 kg CO₂e/kg
- Fruits: 0.3 kg CO₂e/kg
- Milk: 1.4 kg CO₂e/kg
- Chicken: 6.9 kg CO₂e/kg
- Mutton: 24.0 kg CO₂e/kg

## 🎯 Indian Context Features

### Transportation Options
- Personal vehicles (petrol, diesel, CNG, electric)
- Public transport (bus, train, metro)
- Auto-rickshaws
- Cycling and walking

### Food Categories
- Traditional Indian staples (rice, wheat, pulses)
- Dairy products
- Meat and fish
- Local and seasonal produce

### Waste Management
- Organic waste (60% of Indian household waste)
- Plastic waste
- Paper and cardboard
- Electronic waste

### Cost Savings
- Electricity bill reduction tips
- Fuel cost savings
- Sustainable shopping practices
- Traditional Indian practices

## 🔒 Security Features

- User authentication and authorization
- CSRF protection
- SQL injection prevention
- XSS protection
- Secure password handling

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📝 API Endpoints

- `GET /api/footprint-data/`: Get chart data for dashboard
- `POST /calculate/<month>/`: Calculate carbon footprint for specific month

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Indian government climate goals and policies
- Research on Indian household consumption patterns
- Traditional Indian sustainability practices
- Modern environmental science and emission factors

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🌱 Environmental Impact

This application aims to:
- Increase environmental awareness among Indian households
- Provide actionable steps for reducing carbon footprint
- Support India's goal of achieving net-zero emissions by 2070
- Promote sustainable living practices

---

**Made with ❤️ for a sustainable India** 