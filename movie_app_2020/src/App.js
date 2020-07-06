import React from "react";
import axios from "axios";
import Movie from "./Movies";

class App extends React.Component {
  state = {
    isLoading: true,
    movies: [],
  };
  getMovies = async () => {
    // ES6 버전
    const {
      data: {
        data: { movies },
      },
    } = await axios.get("https://yts-proxy.now.sh/list_movies.json");
    //console.log(movies);
    // {state 안의 movies : axios의 movies} -> { movies }로 단축할 수 있다.
    // this.setState({ movies:movies });
    this.setState({ isLoading: false, movies });
    // ES6 이전 버전
    // const movies = await axios.get("https://yts-proxy.now.sh/list_movies.json?sort_by=rating");
    // console.log(movies.data.data.movies);
  };
  componentDidMount() {
    this.getMovies();
  }
  render() {
    const { isLoading, movies } = this.state; // ES6에서만 작동
    return (
      <div>
        {isLoading
          ? "Loading..."
          : movies.map((movie) => (
              <Movie
                key={movie.id}
                id={movie.id}
                year={movie.year}
                title={movie.title}
                summary={movie.summary}
                poster={movie.medium_cover_image}
              />
            ))}
      </div>
    );
  }
}

export default App;
