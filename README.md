# Web Developer Portfolio

This is a personal portfolio web application built with Python 3.12 and Django 5.
The app is designed to showcase your skills and projects as a web developer, with a user-friendly interface and responsive design.
It includes a dedicated section for listing skills and projects, where users can explore the various skills you've mastered and the projects you've worked on.

The app leverages a many-to-many relationship between skills and projects, allowing for flexible representation of how your expertise applies to different projects. Additionally, the application includes a contact form with responsive frontend validation as well as robust backend validation to ensure secure and effective communication.

## Features

- Two Django models: Skill and Project.
  - Many-to-many relationship between Skill and Project.
  - Separate sections for displaying skills and projects.
- Responsive Contact Form:
  - Includes frontend validation using JavaScript for a smooth user experience.
  - Backend validation ensures that the form submissions are secure and meet the required criteria.
- Database:
  - Uses PostgreSQL for data storage.
  - Fully integrated with Docker Compose for development, allowing for an isolated and consistent development environment.
- Dockerized Development:
  - The application uses Docker Compose to manage the development environment.
  - Easily deploy and manage the app and its dependencies using Docker.
- Management Commands:
  - Custom Django management commands are provided to populate the Skill and Project tables with dummy data.
  - Important: The Skill table must be populated before the Project table due to the many-to-many relationship.
- Figma Design File:
  - An associated Figma design file for the portfolio can be found [here](https://www.figma.com/design/wAgHnJwJZTAkGQbZA0EMc8/Portfolio-Site-v1?node-id=0-1&t=hJVMgzQHP8SZCOP7-1).

## Getting Started

### Prerequisites
- Python 3.12
- Django 5.0.7
- Docker & Docker Compose
- PostgreSQL

### Development

1. Clone the repository
   ```shell
   git clone https://github.com/jakegodsall/portfolio_site
   cd portfolio_site
   ```
2. Set up the environment.
   - Create a `.env` file in the project root (you can copy from `.env.example`) and fill in the necessary environment variables.
3. Build and run the application with Docker compose
   ```shell
   docker-compose up --build
   ```
4. Run migrations
   ```shell
   docker-compose exec web python manage.py migrate
   ```
5. Populate the database with the dummy data
   ```shell
   docker-compose exec web python manage.py load_skill_data.py
   docker-compose exec web python manage.py load_project_data.py
   ```
6. Set up npm to watch the changes in the Sass stylesheets:
   ```shell
   npm install
   npm run sass
   ```
7. Access the application at `http://localhost:8000`.

### Deployment

This section explains how to deploy using [Heroku](https://heroku.com), including adding a PostgreSQL addon, and general configuration.

1. Create a new Heroku app.
    ```shell
    heroku create portfolio_site
    ```
2. Add the PostgreSQL addon.
   ```shell
   heroku addons:create heroku-postgresql:ession-0
   ```
3. Configure the environment variables
    ```shell
    heroku config:set DJANGO_ENV=production
    ```
   Note that this `DJANGO_ENV` environment variable is used to choose the appropriate settings file:
   ```python
   # manage.py
   
   # Determine the environment
   env = os.getenv('DJANGO_ENV', 'development')  # Default to development
   # Set the settings module
   if env == 'development':
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings.development')
   elif env == 'production':
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings.production')
   else:
      raise ValueError(f"Unknown DJANGO_ENV: {env}")
   ```
   You may also need to set other environment variables such as `SECRET_KEY`, `ALLOWED_HOSTS`, etc., according to your project’s needs:
   ```shell
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```
4. Create a `Procfile` in the root of the project (already included in this repository)
   ```shell
   web: gunicorn portfolio_site.wsgi --log-file -
   ```
5. Deploy the application
   ```shell
   git add .
   git commit -m "Deploying to Heroku"
   git push heroku main
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) for more details.

