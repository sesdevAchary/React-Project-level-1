import React , { useState } from 'react'


function WordLetterCounter(){
    const [text, setText] = 
        useState(""); 
     wordCount = text 
        .split(/\s+/) 
        .filter(Boolean).length; 
     letterCount = text.length; 

    const handleTextChange = (e)=>{
        setText(e.target.value)
    }
    return(
        <div>
            <textArea 
            placeholder="type here something"

            onchange ={ handleTextChange} //for event handling

            value={text} // capturing user input from here
            rows={5} 
            cols={50} 
            
            
            
            />
           <p> 
                Word Count: 
                {wordCount} 
            </p> 
            <p> 
                Letter Count:{" "} 
                {letterCount} 
            </p> 
             </div>
    )
}
export default WordLetterCounter