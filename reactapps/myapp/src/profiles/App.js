import { Account } from './Acc.js'
import React from 'react';
import './style1.css';
import 'bootstrap/dist/css/bootstrap.css';
class App extends React.Component {
    render() {
        const ur = ["https://www.sideshow.com/storage/product-images/903429/thanos_marvel_feature.jpg",
            "https://www.sideshow.com/storage/product-images/904599/iron-man-mark-lxxxv__silo.png",
            "https://www.hindustantimes.com/rf/image_size_960x540/HT/p2/2019/01/25/Pictures/_1e3fee26-2078-11e9-abd9-895ad40f6f04.jpg",
        "https://comicvine1.cbsistatic.com/uploads/original/11133/111331200/6384517-thor%20image%20-%20copy.png"]
        return <div>
            <Account name={"shankar"} url={ur[0]}></Account>
            <Account name={"Roopa"} url={ur[3]}></Account>
            <Account name={"Hari"} url={ur[2]}></Account>
        </div>
    }

}
export default App