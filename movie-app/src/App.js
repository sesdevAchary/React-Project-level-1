import './App.css' ; // importing the css app//
import {usestate} from 'react'// to manage states in functional component e.g.-> function app() //
import ReactPlayer from 'react-player'; // component for playing video around different source //
import movieTrailer from 'movie-trailer'; // fetches the URL of the given movie trailer //


// functional component //
function App (){
     const[ movie,setMovie]= usestate("oppenheimer")
     const [ trailer,setTrailer] = usestate("")
}

function setVideo(){
    movieTrailer(movie).then((res)=>{
        setTrailer(res);
    });
}