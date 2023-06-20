import React from 'react'

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
         <FontAwesomeIcon icon={faFacebook} />
         <FontAwesomeIcon icon={faInstagram} />
         <FontAwesomeIcon icon={faPinterest} />
      </div>

      <p>Copyright © 2023 LocalShop. All Rights Reserved.</p>
    </div>
  )
}

export default Footer