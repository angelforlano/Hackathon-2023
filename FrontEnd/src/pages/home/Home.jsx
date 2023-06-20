import Footer from "../../components/footer/Footer"
import NavbarLocal from "../../components/navbar/NavbarLocal"
import Search from "../../components/search/Search";
import MainInfo from '../../components/mainInfo/MainInfo';

function Home() {
  return (
    <div>
      <NavbarLocal />
      <MainInfo />
      <Search />
      <Footer />
    </div>
  )
}

export default Home