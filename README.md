# Work Schedule Planner

## Description
The Work Schedule Planner is a Python script designed to help you organize your daily routine around your work schedule. By providing details such as your work start time, commute time, and desired sleep duration, the script calculates the optimal bedtime, wake-up time, and departure time. It even allows you to customize your schedule if you prefer to arrive early at work.

---

## Features
- Input validation for time entries to ensure accurate scheduling.
- Calculates:
  - Optimal bedtime
  - Wake-up time
  - Time to leave the house
  - Work arrival time
- Customizable option to arrive early at work.
- User-friendly interface with clear prompts.

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/AZaUk/work-schedule-planner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd work-schedule-planner
   ```
3. Run the script:
   ```bash
   python work_schedule_planner.py
   ```
4. Follow the prompts to input your:
   - Work start time (in 24-hour format)
   - Commute time (in minutes)
   - Whether you want to arrive early (y/n) and, if yes, how early (in minutes)
   - Preparation time (in minutes)
   - Desired sleep duration (in hours)
5. Review your personalized schedule provided by the script.

---

## Example
**Input:**
```
What time do you need to be at work?
 Enter time in 24h format (05, 08, 14): 08
How many minutes does it take you to get to work?
30
Would you like to arrive at your workplace early?
 y or n: y
How early would you like to arrive to your workplace?
In minutes: 15
How much time do you need to wake up and prepare for work? (In minutes):
45
Lastly, how many hours of sleep do you desire? (In hours):
7
```

**Output:**
```
You should arrive at 7:45 o'clock
You need to leave house at 7:15 o'clock
You need to wake up at 6:30 o'clock
You need to go to bed at 23:30 o'clock
```

---

## Requirements
- Python 3.6 or higher

---

## Contributing
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
The script was originally written in August 2020.

