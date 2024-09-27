import './App.css'
import { useState } from 'react'
import ReactPlayer from 'react-player'
import movieTrailer from 'movie-trailer'

function App(){
  const [ video,setVideo]=useState(" animal ")
  const [url,setUrl]=useState( " https://youtu.be/8FkLRUJj-o0?si=ZqtlM3QlM21T-0CO");


  function searchOperation(){
    movieTrailer(video).then(res=>{
      setUrl(res);
    });
  }


  return (
    <div className="App">
      <div className="search-box">
      <h1>Movie Trailer</h1>

      < input type =" text " onchange ={(e)=>{setVideo(e.target.value)}}/>

<button onClick={() => { searchOperation() }}>
                    Search
                </button>
            </div>

     
            <ReactPlayer url={url} controls={true} />
        </div>
    );
}

export default App;