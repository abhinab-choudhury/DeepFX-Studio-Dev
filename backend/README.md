# DeepFX-Studio


## Source to learn:

- [Youtube Channel](https://www.youtube.com/@CodingEntrepreneurs/videos)
- [Video Link - (Crazy Video)](https://www.youtube.com/watch?v=WbNNESIxJnY&list=TLPQMjkxMDIwMjS-zePX1_L3RQ&index=6)

**DeepFX-Studio** is an AI-powered image manipulation tool that lets you perform various enhancements, such as colorizing black-and-white images and applying different artistic styles. This project is set up with **Django REST Framework** for the backend, Docker for streamlined development, and SQlite for database management.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

DeepFX-Studio is an image processing backend service that leverages AI to perform transformations on images. This includes colorizing, style transfers, and other effects. The current version is a personal development setup tailored for local testing and refinement.

## Features

DeepFX-Studio offers a robust suite of AI-driven image manipulation features designed to enhance and transform your images effortlessly. Here’s what you can expect:

1. **Neural Style Transfer**  
   Transform your images into stunning artwork by applying artistic styles inspired by famous artists. Let your creativity shine through unique visual interpretations.

2. **Colorization of Black-and-White Images**  
   Revitalize old photographs by adding realistic colors to black-and-white images, breathing new life into cherished memories.

3. **Background Removal**  
   Effortlessly separate the subject from the background, allowing for seamless editing or creative projects without distractions.

4. **Image Super-Resolution (Enhance Image Quality)**  
   Upscale low-resolution images to high-definition quality, ensuring that details remain sharp and clear, even in larger formats.

5. **Cartoonization**  
   Give your photos a fun and artistic twist by transforming them into cartoon-like images, perfect for playful presentations or social media posts.

6. **Image Inpainting (Object Removal)**  
   Quickly and effectively remove unwanted objects from images while reconstructing missing areas, allowing for clean and polished results.

7. **Age Progression and Regression**  
   Visualize aging effects by simulating younger or older versions of subjects in your images, providing fascinating insights into change over time.

8. **Image Denoising**  
   Enhance image clarity by reducing noise and artifacts, resulting in cleaner and more professional-looking visuals.

9. **Auto-Background Blur (Portrait Mode)**  
   Create a soft bokeh effect to highlight your subject, perfect for portrait photography and emphasizing key elements in your images.

10. **Photo Restoration (Black & White to Color)**  
    Restore and revitalize old or damaged photos by adding color and clarity, making them look fresh and appealing again.

11. **HDR Effect (High Dynamic Range)**  
    Enrich your images with vibrant colors and rich details through high dynamic range processing, making your visuals pop.

12. **AI-Powered Image Captioning**  
    Automatically generate descriptive captions for your images, adding context and meaning to your visual content.

## Technologies Used

- **Django** and **Django REST Framework**: For the web backend and API services.
- **Docker**: For containerization, simplifying the development and deployment process.
- **PostgreSQL**: Database management.
- **Python 3.9+**: The primary programming language.

## Setup and Installation

### Prerequisites

- Docker and Docker Compose installed on your system.
- Python 3.9+ (for local development without Docker).

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/DeepFX-Studio.git
   cd DeepFX-Studio
   ```

2. **Set Up Environment Variables**

   Create a `.env` file based on `.env.example` and configure your settings:

   ```plaintext
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

3. **Build and Start Docker Containers**

   Use Docker Compose to set up the app and database:

   ```bash
   docker-compose up --build
   ```

   This will build and start the containers and make the API accessible at `http://localhost:8000`.

4. **Apply Migrations**

   Once containers are running, apply the initial database migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create a Superuser (Optional)**

   To access the Django admin interface, you can create a superuser:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

### Running the Project Without Docker

If you want to run the project locally without Docker:

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```
## API Endpoints

**Base URL:** `http://localhost:8000/api/`

| Method | Endpoint        | Description                        |
|--------|------------------|------------------------------------|
| GET    | `/items/`       | List all items                    |
| POST   | `/items/`       | Create a new item                 |
| GET    | `/items/<id>/`  | Retrieve a specific item          |
| PUT    | `/items/<id>/`  | Update a specific item            |
| DELETE | `/items/<id>/`  | Delete a specific item            |

## Usage

To test the API, you can use:
- **cURL** or **HTTPie**: Command-line tools for HTTP requests.
- **Postman** or **Insomnia**: GUI clients for HTTP requests.

Example of a cURL request to retrieve all items:

```bash
curl -X GET http://localhost:8000/api/items/
```

## Folder Structure

```plaintext
deepfx_studio/
├── api/                     # Django app for the API
│   ├── models.py            # Data models
│   ├── serializers.py       # Serializers for JSON conversion
│   ├── views.py             # API request handlers
│   ├── urls.py              # API routes
├── deepfx_studio/           # Django project folder
│   ├── settings.py          # Project settings
│   ├── urls.py              # Project URL configuration
├── Dockerfile               # Docker setup for the app
├── docker-compose.yml       # Docker Compose setup
├── requirements.txt         # Dependencies
└── .env.example             # Sample environment file
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

