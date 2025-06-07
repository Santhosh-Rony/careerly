# Job Board Website

A Django-based job board website where administrators can manually post job listings collected from the internet. The website helps freshers and job seekers find updated job opportunities easily.

## Features

### Admin Panel
- Secure admin login
- Add job posts with:
  - Job Title
  - Company
  - Job Link (external)
  - Location (optional)
  - Tags (optional)
  - Posted Date (defaults to today)

### Public Job Listing
- View all job posts, grouped by date
- Search jobs by title, company, or location
- Filter jobs by tags
- Sections for Today's Jobs, Yesterday's Jobs, and Older Jobs
- Clean, responsive design
- Easy "Apply Now" links to external job postings

## Tech Stack
- Backend: Django
- Database: PostgreSQL
- Frontend: HTML/CSS with Bootstrap 5
- Icons: Bootstrap Icons

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following content:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=jobboard
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

5. Create the PostgreSQL database:
```bash
createdb jobboard
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

9. Visit:
- Admin panel: http://localhost:8000/admin/
- Job listings: http://localhost:8000/

## Usage

1. Log in to the admin panel using your superuser credentials
2. Add job posts through the admin interface
3. View the public job listing page to see the posts organized by date
4. Use the search and filter features to find specific jobs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 