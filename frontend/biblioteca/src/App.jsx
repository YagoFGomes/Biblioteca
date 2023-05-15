import React, { useEffect, useState } from "react";
import api from "../services/api";
import headers from "../services/token";

import Nav from "../components/Nav/Nav";
import Main from "../components/Main/Main";

export default function App() {

  // const [user, setUser] = useState();

  // useEffect(() => {
  //   api
  //     .get("/livros/",  { headers })
  //     .then((response) => {
  //       setUser(response.data)
        
  //       response.data.forEach(element => {
  //         console.log(element)
  //       });
  //     })
  //     .catch((err) => {
  //       console.error("ops! ocorreu um erro" + err);
  //     });
  // }, []);
  
  return (
    <div >
      <Nav></Nav>
      <Main></Main>

    </div>
  );
}