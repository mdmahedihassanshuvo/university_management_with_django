import React from "react";
import Header from "../shared/header/Header";
import Footer from "../shared/footer/Footer";
import "bootstrap/dist/css/bootstrap.min.css";
import { Outlet } from "react-router-dom";


const Main = () => {
  return (
    <div>
        <Header />
        <Outlet/>
        <Footer />
    </div>
  );
};

export default Main;
