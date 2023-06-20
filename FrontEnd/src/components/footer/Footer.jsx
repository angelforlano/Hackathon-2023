import React from 'react';
import './Footer.css'
import Instagram from '../../assets/images/Instagram.svg';
import Facebook from '../../assets/images/FaceBook.svg'; 
import Pinterest from '../../assets/images/Pinterest.svg';

function Footer() {
  return (
    <div className='footer-container'>
      <div className='footer-total'>
        <ul className='footer-text'>
          <li>Blog</li>
          <li>Nosaltres</li>
          <li>Cookies</li>
          <li>Privacitat</li>
          <li>Termes i condicions</li>
        </ul>
        <div className='social-icons'>
          <img className='Inastagram-logo' src={Instagram} alt='instagram-icon'/>
          <img className='FaceBook-logo' src={Facebook} alt='FaceBook-icon'/>
          <img className='Pinterest-logo' src={Pinterest} alt='Pinterest-icon'/>
        </div>

        <p className='copy-right'>Copyright © 2023 LocalShop. All Rights Reserved.</p>
      </div>
    </div>
  )
}

export default Footer