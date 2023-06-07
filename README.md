# Flask Game Blog

This is a simple blog site built using Flask, a web framework in Python, where users can read articles about games. The project aims to provide a platform for game enthusiasts to share their thoughts, insights, and reviews about different games.

## Features

- **Article Listing:** Users can browse through a list of articles on various games.
- **Article Details:** Users can view the complete details of an article, including the title, author, publication date, and content.
- **Comments:** Users can leave comments on articles to share their opinions or engage in discussions.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/flask-game-blog.git`
2. Navigate to the project directory: `cd flask-game-blog`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Set up the database:
   - Run the following commands:
     ```bash
     flask db init
     flask db migrate
     flask db upgrade
     ```
7. Start the Flask development server: `flask run`

## Usage

- Access the blog site by visiting `http://localhost:5000` in your web browser.
- Browse through the articles, read the full content, and leave comments.
- Create new articles by logging in as an administrator.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements for the project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

## Author

- [Samuel Mwendwa](https://github.com/sammyrhymes)