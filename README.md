# SHPE Member Portal

This project is a Django-based web application designed for local SHPE (Society of Hispanic Professional Engineers) chapter members. 
The portal allows members to track their status, including membership activity, dues payments, and eligibility for chapter-related scholarships.

## Usage

- **Member Registration**: Members can sign up and log in to view their status.
- **Admin Approvals**: Admins can log in to the admin panel to review dues payments and convention attendance proof uploads.
- **Scholarship Applications**: Members can apply for scholarships if they meet eligibility criteria.

## Features
- **Individual Student Account with User Authentication
**To Do
- **Membership Status Tracking**: Members can view their membership status and confirm if they are in good standing based on dues payments.
- **Dues Payment Verification**: Admins can verify member payments, ensuring that only paid members have access to certain benefits.
- **Proof of Convention Attendance**: Members can upload images or files as proof of attendance for the national convention, helping the chapter keep records of active participation.
- **Scholarship Eligibility**: Members who meet participation requirements (such as dues and convention attendance) will be marked as eligible for departmental scholarships.

## Project Structure

The Django project includes several apps and components:
- **Members**: Contains member information, dues payment status, and profile management.
- **Scholarship**: Tracks eligibility criteria and manages scholarship eligibility.
- **File Uploads**: Allows members to upload proof of purchase files for the national convention, along with flight and hotel expenses.
- **Admin Portal**: Admin interface to approve dues payments and track member statuses.

## Getting Started

### Technologies, Frameworks, and Languages

- Django & Django Template Language (DTL)
- Bootstrap CSS
- MySQL
- Python
- HTML

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Yizushdz/SWE_Project.git
   cd SWE_Project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Configure your database settings in `settings.py`.
   - Run the migrations:
     ```bash
     python manage.py migrate
     ```

4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the portal by navigating to `http://127.0.0.1:8000/` in your browser.


## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed description of changes.

## License

This project is licensed under the MIT License.
