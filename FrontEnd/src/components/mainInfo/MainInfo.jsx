import Card from 'react-bootstrap/Card';
import MainImage from '../../assets/images/small-house.png';
import "./MainInfo.css";

function MainInfo() {
  return (
    <Card className="text-center">
      <Card.Header className='text-header-main'>- CONNECTEM COMERÇOS - </Card.Header>
      <Card.Body>
        <Card.Title className='text-header-subtitle'>Solucions Sostenibles</Card.Title>
        <Card.Text className='text-header-text'>
        Abraçar les possibilitats infinitives de la Barcelona sostenible amb LocalShop
        </Card.Text>
        <img className="MainImage" src={MainImage} alt="image brand"/>
      </Card.Body>
    </Card>
  );
}

export default MainInfo;