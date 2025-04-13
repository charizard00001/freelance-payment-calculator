# Freelance Payment Calculator
[Live Link](https://freelance-payment-calculator-8wac897jv-charizard0001s-projects.vercel.app/)

A full-stack application that helps freelancers calculate their earnings in INR based on their hourly rate in USD. The app fetches real-time exchange rates and provides calculations for hourly, daily, weekly, and monthly earnings.

## Features

- Real-time USD to INR exchange rate
- Calculate earnings in INR based on:
  - Hourly rate in USD
  - Working hours per day
  - Working days per week
- Clean, responsive UI
- Easy deployment on Vercel

## Tech Stack

- Backend: Python (FastAPI)
- Frontend: HTML, CSS, JavaScript
- Deployment: Vercel

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd freelance-payment-calculator
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn backend.app:app --reload
   ```

4. Open your browser and navigate to `http://localhost:8000`

## Deployment Instructions

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy the application:
   ```bash
   vercel
   ```

4. Follow the prompts to complete the deployment.

## Project Structure

```
project-root/
│
├── backend/
│   ├── app.py               # Main FastAPI application
│   ├── calculation.py       # Earnings calculation logic
│   └── currency_exchange.py # Exchange rate fetching
│
├── frontend/
│   ├── index.html          # Main UI
│   ├── styles.css          # Styling
│   └── script.js           # Frontend logic
│
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel configuration
└── README.md              # Project documentation
```

## API Endpoints

- `POST /calculate`: Calculate earnings based on input parameters
  - Request body:
    ```json
    {
        "hourly_rate_usd": float,
        "hours_per_day": float,
        "working_days_per_week": int
    }
    ```
  - Response:
    ```json
    {
        "hourly_rate_inr": float,
        "daily_earnings": float,
        "weekly_earnings": float,
        "monthly_earnings": float
    }
    ```

## License

MIT 
