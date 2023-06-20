import Iframe from "react-iframe";
import './Dashcard.css';
import { Button } from "react-bootstrap";

function Dashcard() {
  return (
    <>
    <div className="cont-dashcard">
      <p className="cont-dashcard-text">Resultats</p>
        <Iframe className="dashcard" src="https://charts.mongodb.com/charts-hackathon-2023-uxipt/embed/charts?id=6491bcb6-3e11-4ad8-888c-d9baa7beb917&maxDataAge=3600&theme=light&autoRefresh=true"/>
     
    <div className="cont-indicators">
      <p className="txt-indicator">Indicador 1</p>
      <p className="txt-indicator">Indicador 2</p>
      <p className="txt-indicator">Indicador 3</p>
      <p className="txt-indicator">Indicador 4</p>
      </div>
      
      <Button className="butn-details">Veure més detalls</Button>
      </div>
    </>
   
  )
}

export default Dashcard