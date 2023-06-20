import React from 'react';
import Footer from 'react';
import faInstagram from './assets/images/faInstagram.png';
import faFacebook from './src/assets/images/faInstagram.png'; 
import faPinterest from '../src/assets/images.faPinterest.png';

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
         <img icon={faFacebook} />
         <img icon={faInstagram} />
         <img icon={faPinterest} />
      </div>

      <p>Copyright © 2023 LocalShop. All Rights Reserved.</p>
    </div>
  )
}

export default Footer