import "./Navbar.css";
import homeIcon from "../../assets/images/local-shop.png";
import hamburgerIcon from "../../assets/images/hamburger.png";


function NavbarLocal() {
  return (
    <>
    <div className="contain-nav">
      <img className="img-nav-local" src={homeIcon}/>
      <img className="img-nav-hamburger" src={hamburgerIcon}/>
    </div>
    </>
  )
}

export default NavbarLocal