import Iframe from "react-iframe"
import './Map.css';

function Map() {
  return (
    <div>
        <Iframe className="iframe-styles"
            src="https://charts.mongodb.com/charts-hackathon-2023-uxipt/embed/charts?id=6491b2bd-b257-4472-8599-bc6071005194&maxDataAge=86400&theme=dark&autoRefresh=true"/>
    </div>
  )
}

export default Map