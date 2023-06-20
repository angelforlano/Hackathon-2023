import { BrowserRouter, Route, Routes } from "react-router-dom"
import Home from "../pages/home/Home"
import Dashboard from "../pages/dashboard/Dashboard"
function Router() {
  return (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/dashboard" element={<Dashboard />}></Route>
        </Routes>
    </BrowserRouter>
  )
}

export default Router