# Smart Campus Services Portal

## Overview
The Smart Campus Services Portal is a web application designed to enhance the campus experience for students and staff. It provides functionalities such as user authentication, service booking, timetable viewing, maintenance issue reporting, and an admin dashboard with analytics.

## Features
- **User Authentication**: Secure sign-in and sign-up processes with email and password restrictions.
- **Service Booking**: Users can view available services and confirm bookings.
- **Timetable Viewing**: Access to class schedules for students.
- **Maintenance Issue Reporting**: Users can report maintenance issues directly through the portal.
- **Admin Dashboard**: An analytics dashboard for administrators to manage users and bookings.

## Technologies Used
- **Backend**: Python with Flask framework
- **Frontend**: HTML, CSS, and JavaScript
- **Database**: (Specify the database used, e.g., SQLite, PostgreSQL)

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd Smart-Campus-Services-Portal
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python run.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000` to access the portal.

## Directory Structure
```
Smart-Campus-Services-Portal
├── app
│   ├── __init__.py
│   ├── auth
│   ├── booking
│   ├── timetable
│   ├── maintenance
│   ├── admin
│   ├── static
│   └── templates
├── requirements.txt
├── run.py
└── README.md
```

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.