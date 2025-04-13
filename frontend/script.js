document.addEventListener('DOMContentLoaded', () => {
    const calculateBtn = document.getElementById('calculate-btn');
    const hourlyRateInput = document.getElementById('hourly-rate');
    const hoursPerDayInput = document.getElementById('hours-per-day');
    const workingDaysInput = document.getElementById('working-days');

    calculateBtn.addEventListener('click', async () => {
        const hourlyRate = parseFloat(hourlyRateInput.value);
        const hoursPerDay = parseFloat(hoursPerDayInput.value);
        const workingDays = parseInt(workingDaysInput.value);

        if (isNaN(hourlyRate) || isNaN(hoursPerDay) || isNaN(workingDays)) {
            alert('Please enter valid numbers for all fields');
            return;
        }

        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    hourly_rate_usd: hourlyRate,
                    hours_per_day: hoursPerDay,
                    working_days_per_week: workingDays
                })
            });

            if (!response.ok) {
                throw new Error('Failed to calculate earnings');
            }

            const data = await response.json();
            updateResults(data);
        } catch (error) {
            alert('Error calculating earnings: ' + error.message);
        }
    });

    function updateResults(data) {
        document.getElementById('hourly-rate-inr').textContent = formatCurrency(data.hourly_rate_inr);
        document.getElementById('daily-earnings').textContent = formatCurrency(data.daily_earnings);
        document.getElementById('weekly-earnings').textContent = formatCurrency(data.weekly_earnings);
        document.getElementById('monthly-earnings').textContent = formatCurrency(data.monthly_earnings);
    }

    function formatCurrency(amount) {
        return '₹' + amount.toLocaleString('en-IN', {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });
    }
}); 