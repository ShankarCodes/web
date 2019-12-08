import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';

//import { Form, FormControl, Button } from 'react-bootstrap';

class Account extends React.Component {

    render() {
        const url = "https://www.sideshow.com/storage/product-images/903429/thanos_marvel_feature.jpg"
        const styl = { display: 'inline-block' }
        const plac = {
            fontSize: '26px',
            margin: '15px 10px 10px 10px',
            borderBottom: '5px solid black',
            borderTop: '5px solid black',
            width:'200px', 
          }
        return <div>
            <div style={styl}>
        <h1 style={plac} >Hello,{this.props.name}</h1>
            </div>
            <div style={styl}>
                <img src={this.props.url} height={100} width={200}></img>
            </div>
            <br />

        </div>
    }
}
export {Account}
