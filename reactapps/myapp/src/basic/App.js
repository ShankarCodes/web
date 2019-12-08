
import {Clock,Welcome,NameForm} from './basic.js'
import React from 'react';
import './App.css';


class App extends React.Component
{
 render()
  {
    
    return <div><Welcome name="shankar"/>
    <Welcome name={"roopa"}/>
    <Welcome name={"hari"}/>
    <Clock/><Clock/>
    <Clock/>
    <Clock/>
    <NameForm/>
    
    </div>
  }
}
export default App;

