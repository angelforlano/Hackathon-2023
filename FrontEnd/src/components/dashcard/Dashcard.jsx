import Iframe from "react-iframe";
import './Dashcard.css';

function Dashcard() {
  return (
    <>
    <div className="cont-dashcard">
      <p className="cont-dashcard-text">Mapa</p>
        <Iframe className="dashcard" src="https://charts.mongodb.com/charts-hackathon-2023-uxipt/embed/charts?id=6491bcb6-3e11-4ad8-888c-d9baa7beb917&maxDataAge=3600&theme=light&autoRefresh=true"/>
    </div> 
    </>
   
  )
}

export default Dashcard