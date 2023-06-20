import React from 'react';
import Footer from '../footer';
import faInstagram from '../../assets/images/faInstagram';
import faFacebook from '../../assets/images/faInstagram.png'; 
import faPinterest from '../../assets/images/faPinterest.png';

function Footer() {
  return (
    <div>
       <ul>
         <li>Blog</li>
         <li>Nosaltres</li>
         <li>Cookies</li>
         <li>Privacitat</li>
         <li>Termes i condicions</li>
      </ul>
      <div className="social-icons">
         <img className='Inastagram-logo' src={faInstagram} alt='instagram-icon'/>
         <img className='FaceBook-logo' src={faFacebook} alt='FaceBook-icon'/>
         <img className='Pinterest-logo' src={faPinterest} alt='Pinterest-icon'/>
      </div>

      <p>Copyright © 2023 LocalShop. All Rights Reserved.</p>
    </div>
  )
}

export default Footer