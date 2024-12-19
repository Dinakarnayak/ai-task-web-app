
# AI Task Web App 🤖🌐

Welcome to the **AI Task Web App**! This web application provides a suite of AI-powered tasks, including text generation, text analysis, and image recognition. It is built using Flask for the backend and provides a simple, user-friendly interface to interact with various AI models.

![Project Screenshot](app/static/Screenshot.png) <!-- Replace with the actual path or link to your screenshot -->

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Text Generation** 📝: Generate creative and meaningful text based on input prompts.
- **Text Analysis** 📊: Analyze and extract insights from input text, including sentiment analysis.
- **Image Recognition** 🖼️: Upload images for recognition and classify objects within them.
- **Database Storage** 📥: Save results from AI tasks into a SQLite database for easy access.

## Technologies Used

### Backend
- **Flask**: A lightweight web framework for Python that powers the backend of the application.
- **SQLite**: A simple database to store task results and manage data.
- **AI Libraries**: Custom AI models or external APIs (e.g., OpenAI API, TensorFlow, or PyTorch) to process text and images.

### Frontend
- **HTML/CSS/JavaScript**: Core web technologies to create the user interface.
- **Bootstrap**: A front-end framework to design responsive and modern layouts.

## Project Structure
```
AI Task Web App/
│
├── app.py                # Python Flask application
├── templates/            # Folder for HTML templates
│   ├── index.html        # Main webpage
│   └── result.html       # Result display page
├── static/               # Folder for static files (CSS, JS, Images)
│   └── style.css         # Custom CSS for styling
└── tasks.db              # SQLite database to store results
```

## Installation

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your machine.
- **Pip**: Package installer for Python.

### Running the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/Dinakarnayak/AI-Task-Web-App.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AI-Task-Web-App
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Access the application at:
   - Frontend: [http://localhost:5000](http://localhost:5000)

## Usage
- **Text Generation**: Provide a prompt and generate creative text based on your input.
- **Text Analysis**: Input text to analyze and extract insights such as sentiment.
- **Image Recognition**: Upload an image to recognize and classify objects.
- **Results Display**: View the output of the AI tasks, and results are automatically stored in the database for easy access.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (e.g., `git checkout -b feature-branch`).
3. Commit your changes (e.g., `git commit -m 'Add some feature'`).
4. Push to the branch (e.g., `git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
Developed by Dinakar Nayak N. For inquiries, please contact me via [dinakarnayak4248@gmail.com](mailto:dinakarnayak4248@gmail.com).

[LinkedIn: Dinakar Nayak N](https://www.linkedin.com/in/dinakar-nayak-n-125762232/)

Thank you for using the **AI Task Web App**! We hope you find it useful for your AI tasks. 😊
