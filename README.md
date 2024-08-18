# PopcornPicks

**PopcornPicks** is a content-based recommender system that suggests movies similar to the ones you like. The system uses the TMDB (The Movie Database) API to fetch movie details and make recommendations.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Streamlit

### Installation

1. Clone or download this repository to your local machine:
   git clone https://github.com/yourusername/PopcornPicks)

### API Key Setup
1. Create an account on The Movie Database (TMDB).
2. Click on the API link in the left-hand sidebar under your account settings.
3. Fill out the required details to apply for an API key.
4. If asked for a website URL, you can enter "NA" if you don't have one.
5. Once you've submitted your details, you will be provided with an API key.
6. Replace YOUR_API_KEY in line 7 of app.py with your actual API key.
7. response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY&language=en-US'.format(movie_id))
8. For example, if your API key is 12345678, update line 7 as:
- response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=12345678&language=en-US'.format(movie_id))

### Running the Project
Open your terminal or command prompt from your project directory.
Run the command: streamlit run app.py
Your application will start, and you can begin using PopcornPicks to find movie recommendations!

### Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome!

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
This project uses the TMDB API for movie data.
