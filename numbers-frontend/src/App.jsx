import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import AccordionConteiner from './components/conteiner/accordion_conteiner'
import TitleBanner from './components/pure/tittle_banner'
// import './App.css'
import './static/style/bootstrap-5.1.1.min.css';



function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <TitleBanner></TitleBanner>
      
      <div className="container py-5 ">
        <div className="row justify-content-center align-items-center">
          <div className="col-md-6">
            <div className="d-flex flex-column">
              <AccordionConteiner></AccordionConteiner>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
