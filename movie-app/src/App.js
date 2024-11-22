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
// the jsx code //

return(
    /* The return statement indicates that this is part of a React component's render method. The component is rendering a top-level <div> with the class name App*/
    <div className="App">
        <div className = "searchBox">
            <label>
                search any movie:{" "}
            </label>
            <inout type="text" onchange ={(e)=>{setMovie(e.target.value)}} />
             
             <button onClick={()=>{setVideo()}}></button>
            
        </div>
        <ReactPlayer url = {trailer} controls = {true}/>
    </div>
);
}
export default App;