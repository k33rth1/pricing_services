# pricing_services
TITLE - pricing services

DESCRIPTION - This repository gives the information about the price of a particular product from an ecommerce website.
**Project Name: PriceTracker**

**Project Description:**

PriceTracker is a web application designed to help users monitor and track prices of items from various online stores. The application allows users to set price alerts for specific items and receive notifications when the prices drop below a certain threshold.

**Key Features:**

1. **Item Price Tracking:** Users can add items from supported online stores by providing the item URL. The application fetches the current price of the item and stores it for tracking.

2. **Price Alerts:** Users can create price alerts for specific items. They can set a desired price limit, and whenever the price of the item drops below this limit, the user receives an email notification.

3. **User Registration and Authentication:** Users can register for an account and log in securely to access the application features.

4. **Store Management:** Admin users can manage supported stores by adding, editing, or deleting store information. This includes details like store name, URL prefix, tag name, and query parameters for scraping.

5. **Email Notifications:** The application integrates with the Mailgun API to send email notifications to users when price alerts are triggered.

**Technologies Used:**

- **Backend:** Python with Flask framework for handling server-side logic.
- **Database:** MongoDB for storing item, store, user, and alert information.
- **Web Scraping:** Beautiful Soup for parsing HTML content and extracting item prices from online stores.
- **Frontend:** HTML, CSS, and JavaScript for building the user interface and interactivity.
- **Authentication:** User passwords are securely hashed using PBKDF2-SHA512 encryption.
- **Email Service:** Mailgun API for sending email notifications to users.
- **Data Modeling:** Data classes and inheritance used for modeling items, stores, users, and alerts.
- **Utilities:** Custom utility functions for email validation, password hashing, and password verification.
- **Error Handling:** Custom exception classes for handling user-related errors.
- **Session Management:** Flask session management for maintaining user sessions.

**Project Structure:**

- **common:** Contains database configuration and utilities for database operations.
- **models:** Includes data models for items, stores, users, and alerts.
- **libs:** Contains external libraries and utilities for integrating with external services like Mailgun.
- **views:** Flask blueprints for defining routes and views related to item alerts and store management.
- **users.py:** Flask blueprint for user registration and authentication.
- **stores.py:** Flask blueprint for managing supported stores.
- **alerts.py:** Flask blueprint for creating, editing, and deleting price alerts.
- **utils.py:** Utility functions for email validation, password hashing, and password verification.
- **mailgun.py:** Integration with the Mailgun API for sending email notifications.
- **database.py:** Database configuration and helper functions for database operations.
- **app.py:** Main application file for initializing Flask app and registering blueprints.

PriceTracker provides a convenient way for users to stay informed about price changes for their favorite items and helps them make informed purchasing decisions.
